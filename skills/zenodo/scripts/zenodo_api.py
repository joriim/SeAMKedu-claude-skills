#!/usr/bin/env python3
"""Zenodo-tallenteen luonti, lataus, julkaisu ja versiointi REST-rajapinnan kautta.

Turvallisuusoletukset:
- Kohteena on aina sandbox.zenodo.org, ellei anneta --production.
- create ja newversion tekevät vain luonnoksen. Julkaisu vaatii publish --confirm.
- Token luetaan ympäristömuuttujasta ZENODO_TOKEN, eikä sitä koskaan tulosteta.

Käyttö:
  python zenodo_api.py check    --metadata zenodo-metadata.json
  python zenodo_api.py create   --metadata zenodo-metadata.json --files a.csv README.md
  python zenodo_api.py show     --id 123456
  python zenodo_api.py publish  --id 123456 --confirm
  python zenodo_api.py newversion --id 123456 --metadata m.json --files a.csv [--keep-old-files]

Vaatii: requests (pip install requests)
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

try:
    import requests
except ImportError:  # pragma: no cover
    sys.exit("Asenna requests: pip install requests")

SANDBOX = "https://sandbox.zenodo.org/api"
PRODUCTION = "https://zenodo.org/api"

REQUIRED = ["title", "upload_type", "description", "creators", "license"]
NON_OPEN_LICENSE_MARKERS = ("-nc", "-nd")


def base_url(args) -> str:
    return PRODUCTION if args.production else SANDBOX


def session() -> requests.Session:
    token = os.environ.get("ZENODO_TOKEN")
    if not token:
        sys.exit("ZENODO_TOKEN puuttuu. Luo token Zenodossa (Applications → Personal access tokens) "
                 "ja aseta se ympäristömuuttujaan. Hiekkalaatikolla ja tuotannolla on eri tokenit.")
    s = requests.Session()
    s.headers["Authorization"] = f"Bearer {token}"
    return s


def load_metadata(path: str) -> dict:
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    return data.get("metadata", data)


def check_metadata(md: dict) -> list[str]:
    """Palauttaa listan ongelmista. Tyhjä lista = ok."""
    problems = []
    for key in REQUIRED:
        if not md.get(key):
            problems.append(f"Pakollinen kenttä puuttuu: {key}")
    if "TODO" in json.dumps(md):
        problems.append("Metatiedoissa on TODO-arvoja. Täydennä tai poista kentät.")
    if md.get("upload_type") == "publication" and not md.get("publication_type"):
        problems.append("upload_type=publication vaatii publication_type-kentän.")
    if md.get("upload_type") == "image" and not md.get("image_type"):
        problems.append("upload_type=image vaatii image_type-kentän.")
    for c in md.get("creators", []):
        name = c.get("name", "")
        if "," not in name:
            problems.append(f"Tekijän nimi muotoon 'Sukunimi, Etunimi': {name!r}")
        orcid = c.get("orcid", "")
        if orcid and (orcid.startswith("http") or len(orcid) != 19):
            problems.append(f"ORCID muotoon 0000-0000-0000-0000 ilman URL:ia: {orcid!r}")
    lic = str(md.get("license", "")).lower()
    if any(m in lic for m in NON_OPEN_LICENSE_MARKERS):
        problems.append(f"Lisenssi {lic} ei ole avoin (NC/ND). Varmista, että tämä on tarkoitus.")
    if md.get("access_right") == "embargoed" and not md.get("embargo_date"):
        problems.append("access_right=embargoed vaatii embargo_date-kentän.")
    return problems


def raise_for(resp: requests.Response, what: str) -> dict:
    if resp.status_code >= 400:
        try:
            detail = json.dumps(resp.json(), ensure_ascii=False, indent=2)
        except ValueError:
            detail = resp.text[:2000]
        sys.exit(f"{what} epäonnistui ({resp.status_code}):\n{detail}")
    return resp.json() if resp.content else {}


def upload_files(s: requests.Session, bucket: str, files: list[str]) -> None:
    for f in files:
        p = Path(f)
        if not p.is_file():
            sys.exit(f"Tiedostoa ei löydy: {f}")
        with p.open("rb") as fh:
            raise_for(s.put(f"{bucket}/{p.name}", data=fh), f"Lataus {p.name}")
        print(f"  ladattu {p.name} ({p.stat().st_size / 1e6:.2f} Mt)")


def summarize(dep: dict, prod: bool) -> None:
    md = dep.get("metadata", {})
    doi = md.get("prereserve_doi", {}).get("doi") or dep.get("doi") or "(ei vielä)"
    print(json.dumps({
        "ymparisto": "TUOTANTO" if prod else "sandbox",
        "id": dep.get("id"),
        "tila": dep.get("state"),
        "julkaistu": dep.get("submitted"),
        "doi": doi,
        "concept_doi": dep.get("conceptdoi"),
        "esikatselu": dep.get("links", {}).get("html"),
        "tiedostot": [f.get("filename") for f in dep.get("files", [])],
    }, ensure_ascii=False, indent=2))


def cmd_check(args) -> None:
    probs = check_metadata(load_metadata(args.metadata))
    if probs:
        print("Korjattavaa:")
        for p in probs:
            print(" -", p)
        sys.exit(1)
    print("Metatiedot ok.")


def cmd_create(args) -> None:
    md = load_metadata(args.metadata)
    probs = check_metadata(md)
    if probs:
        print("Metatiedoissa on korjattavaa, luonnosta ei luotu:")
        for p in probs:
            print(" -", p)
        sys.exit(1)
    md.setdefault("prereserve_doi", True)
    s = session()
    url = base_url(args)
    dep = raise_for(s.post(f"{url}/deposit/depositions", json={}), "Luonnoksen luonti")
    upload_files(s, dep["links"]["bucket"], args.files)
    dep = raise_for(s.put(f"{url}/deposit/depositions/{dep['id']}", json={"metadata": md}),
                    "Metatietojen tallennus")
    print("Luonnos luotu. Sitä EI ole julkaistu.")
    summarize(dep, args.production)


def cmd_show(args) -> None:
    s = session()
    dep = raise_for(s.get(f"{base_url(args)}/deposit/depositions/{args.id}"), "Haku")
    summarize(dep, args.production)


def cmd_publish(args) -> None:
    if not args.confirm:
        sys.exit("Julkaisu on pysyvä eikä sitä voi perua. Aja uudelleen lipulla --confirm, "
                 "kun käyttäjä on hyväksynyt tämän nimenomaisen tallenteen julkaisun.")
    s = session()
    url = base_url(args)
    dep = raise_for(s.get(f"{url}/deposit/depositions/{args.id}"), "Haku")
    probs = check_metadata(dep.get("metadata", {}))
    if probs:
        print("Luonnoksessa on korjattavaa, ei julkaistu:")
        for p in probs:
            print(" -", p)
        sys.exit(1)
    if not dep.get("files"):
        sys.exit("Luonnoksessa ei ole tiedostoja, ei julkaistu.")
    dep = raise_for(s.post(f"{url}/deposit/depositions/{args.id}/actions/publish"), "Julkaisu")
    print("JULKAISTU.")
    summarize(dep, args.production)


def cmd_newversion(args) -> None:
    s = session()
    url = base_url(args)
    r = raise_for(s.post(f"{url}/deposit/depositions/{args.id}/actions/newversion"), "Uusi versio")
    draft_url = r["links"]["latest_draft"]
    draft = raise_for(s.get(draft_url), "Luonnoksen haku")
    if not args.keep_old_files:
        for f in draft.get("files", []):
            raise_for(s.delete(f["links"]["self"]), f"Vanhan tiedoston poisto {f.get('filename')}")
    if args.files:
        upload_files(s, draft["links"]["bucket"], args.files)
    if args.metadata:
        md = load_metadata(args.metadata)
        md.pop("prereserve_doi", None)
        md.pop("publication_date", None)  # Zenodo asettaa julkaisupäivän
        probs = check_metadata(md)
        if probs:
            print("Uuden version metatiedoissa on korjattavaa (luonnos jäi Zenodoon):")
            for p in probs:
                print(" -", p)
        draft = raise_for(s.put(draft_url, json={"metadata": md}), "Metatietojen tallennus")
    else:
        draft = raise_for(s.get(draft_url), "Luonnoksen haku")
    print("Uuden version luonnos luotu. Sitä EI ole julkaistu.")
    summarize(draft, args.production)


def main() -> None:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--production", action="store_true", help="käytä zenodo.org:ia (oletus: sandbox)")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("check"); c.add_argument("--metadata", required=True); c.set_defaults(fn=cmd_check)
    c = sub.add_parser("create"); c.add_argument("--metadata", required=True)
    c.add_argument("--files", nargs="+", required=True); c.set_defaults(fn=cmd_create)
    c = sub.add_parser("show"); c.add_argument("--id", required=True); c.set_defaults(fn=cmd_show)
    c = sub.add_parser("publish"); c.add_argument("--id", required=True)
    c.add_argument("--confirm", action="store_true"); c.set_defaults(fn=cmd_publish)
    c = sub.add_parser("newversion"); c.add_argument("--id", required=True)
    c.add_argument("--metadata"); c.add_argument("--files", nargs="*", default=[])
    c.add_argument("--keep-old-files", action="store_true"); c.set_defaults(fn=cmd_newversion)

    args = p.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()
