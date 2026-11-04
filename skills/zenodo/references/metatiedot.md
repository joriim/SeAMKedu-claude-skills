# Zenodo-metatiedot — kenttäohje

Rakenne vastaa Zenodon deposit-rajapinnan `metadata`-objektia (sama, jota `.zenodo.json` käyttää). Tarkista kenttien ajantasaisuus Zenodon kehittäjädokumentaatiosta (developers.zenodo.org), jos rajapinta palauttaa validointivirheen.

## Pohja

```json
{
  "metadata": {
    "title": "Nitrogen sensor field data from Southern Ostrobothnia, growing seasons 2025–2026",
    "upload_type": "dataset",
    "description": "<p>Mitä aineisto sisältää, miten ja missä se tuotettiin, mihin sitä voi käyttää.</p><p>Produced in the TODO project, funded by TODO.</p>",
    "creators": [
      {"name": "Sukunimi, Etunimi", "orcid": "0000-0000-0000-0000", "affiliation": "Seinäjoki University of Applied Sciences"}
    ],
    "contributors": [
      {"name": "Sukunimi, Etunimi", "type": "DataCollector", "affiliation": "TODO"}
    ],
    "access_right": "open",
    "license": "cc-by-4.0",
    "keywords": ["nitrogen", "typpi", "precision agriculture", "täsmäviljely"],
    "language": "eng",
    "publication_date": "2026-11-04",
    "version": "1.0.0",
    "grants": [{"id": "10.13039/501100000780::TODO"}],
    "communities": [{"identifier": "TODO"}],
    "related_identifiers": [
      {"identifier": "https://github.com/TODO/TODO", "relation": "isSupplementedBy", "resource_type": "software"}
    ],
    "notes": "Funding acknowledgement and any usage notes.",
    "prereserve_doi": true
  }
}
```

Poista kentät, joille ei ole todellista arvoa, ennen latausta. `TODO` ei saa päätyä julkaistuun tallenteeseen.

## upload_type ja alatyypit

| Tuotos | `upload_type` | Lisäkenttä |
|---|---|---|
| Tutkimusdata, mittausaineisto | `dataset` | — |
| Ohjelmisto, skripti, Claude-skill | `software` | — |
| Raportti, artikkelikäsikirjoitus, deliverable | `publication` | `publication_type`: `report`, `article`, `preprint`, `deliverable`, `workingpaper`, `technicalnote`, `book`, `section`, `conferencepaper`, `datamanagementplan`, `other` |
| Posteri | `poster` | — |
| Esitys, diat | `presentation` | — |
| Kuva, kartta, kaavio | `image` | `image_type`: `figure`, `plot`, `diagram`, `photo`, `drawing`, `other` |
| Video, tallenne | `video` | — |
| Opetusmateriaali | `lesson` | — |
| Fyysinen näyte (metatieto) | `physicalobject` | — |
| Muu | `other` | — |

Horizon Europe -hankkeen toimitettava raportti (deliverable): `publication` + `publication_type: deliverable`.

## Tekijät ja osallistujat

- `creators` = ne, jotka ovat tehneet tuotoksen ja vastaavat siitä. Järjestys kuten viittauksessa halutaan.
- `contributors` = muut, joilla on rooli. Tyyppejä: `ContactPerson`, `DataCollector`, `DataCurator`, `DataManager`, `Editor`, `HostingInstitution`, `ProjectLeader`, `ProjectManager`, `ProjectMember`, `Researcher`, `RightsHolder`, `Sponsor`, `Supervisor`, `WorkPackageLeader`, `Other`.
- Nimi aina muodossa `Sukunimi, Etunimi`. ORCID ilman URL-etuliitettä.
- Affiliaatio: `Seinäjoki University of Applied Sciences`. Kumppanit omilla virallisilla englanninkielisillä nimillään.
- Tekoälyä ei merkitä tekijäksi. Tekoälyavusteisuus kerrotaan kuvauksessa tai `notes`-kentässä, jos se on olennaista (esim. koodin tuottaminen).

## Lisenssit

Käytä pieniä kirjaimia, kuten Zenodon lisenssiluettelossa.

| Tuotos | Suositus | Huom. |
|---|---|---|
| Raportti, posteri, esitys, kuva | `cc-by-4.0` | Horizon Europe edellyttää julkaisuille CC BY:tä tai vastaavaa |
| Data | `cc-by-4.0` tai `cc0-1.0` | CC0 helpottaa uudelleenkäyttöä; CC BY varmistaa viittauksen |
| Ohjelmisto | `mit`, `apache-2.0` | Apache-2.0, jos patenttilauseke on tarpeen |
| Julkishallinnon ohjelmisto | `eupl-1.2` | Copyleft, EU:n suosima |
| Kolmannen osapuolen sisältöä mukana | — | Lisenssi ei voi olla sallivampi kuin lähdeaineiston |

`-nc`- ja `-nd`-lisenssit eivät ole avoimia, eivätkä ne täytä Horizon Europen avoimuusvaatimusta. Käytä vain perustellusta syystä ja kerro siitä käyttäjälle.

## Rahoittaja (grants)

- Muoto: `"<rahoittajan FundRef DOI>::<sopimusnumero>"`. Euroopan komission (mm. Horizon Europe) rahoittajatunniste on `10.13039/501100000780`.
- Toimii vain rahoituksille, jotka ovat Zenodon/OpenAIREn rahoitustietokannassa. Esim. EAKR-, ESR+-, Leader- ja kansalliset hankkeet eivät yleensä ole: kirjaa rahoitus silloin `description`- tai `notes`-kenttään muodossa "Rahoittaja, ohjelma, hanketunnus".
- Älä keksi numeroa. Jos käyttäjä ei tiedä sitä, jätä kenttä pois ja kirjaa TODO hyväksyttävään taulukkoon.

## Suhteet (related_identifiers)

| Tilanne | `relation` | Esimerkki |
|---|---|---|
| Data artikkelin tueksi | `isSupplementTo` | artikkelin DOI |
| Koodi, jolla data käsiteltiin | `isSupplementedBy` / `isDerivedFrom` | GitHub-URL tai ohjelmiston DOI |
| Raportti Theseuksessa, rinnakkaistallenne Zenodossa | `isIdenticalTo` | Theseus-URN tai -URL |
| Osa suurempaa kokonaisuutta | `isPartOf` | kokoomatallenteen DOI |
| Kooste osista | `hasPart` | osan DOI |
| Viittaa | `cites` / `references` | lähteen DOI |
| Dokumentoi menetelmän | `documents` / `isDocumentedBy` | menetelmäkuvauksen DOI |

Lisää `resource_type` (esim. `publication-article`, `dataset`, `software`), kun linkki ei ole DOI.

## Muut kentät

- `access_right`: `open` (oletus), `embargoed` + `embargo_date`, `restricted` + `access_conditions`, `closed`.
- `publication_date`: ISO-muoto. Oletuksena julkaisupäivä; käytä alkuperäistä päivää, jos tallennat aiemmin julkaistua.
- `version`: semanttinen (`1.0.0`) ohjelmistoille, päivämäärä tai `v1` datalle.
- `keywords`: kaksikieliset, myös hankkeen nimi ja alue (esim. "Etelä-Pohjanmaa", "Southern Ostrobothnia").
- `subjects`: valinnainen kontrolloitu sanasto (esim. YSO-käsite URI:na).
- `locations`: datalle paikka (`lat`, `lon`, `place`). Ei tarkkoja tilasijainteja ilman lupaa.
- `dates`: aineiston keruuaika, esim. `{"type": "Collected", "start": "2025-05-01", "end": "2025-09-30"}`.
- `references`: lähdeluettelo tekstinä, yksi viite per rivi.
- `notes`: rahoitusmaininta, tekoälyavusteisuus, käyttörajoitukset.

## Kuvauksen rakenne (description)

Zenodo hyväksyy rajatun HTML:n (`<p>`, `<ul>`, `<a>`, `<strong>`, `<em>`). Suositeltu rakenne:
1. Mitä tämä on yhdellä lauseella.
2. Miten ja missä tuotettiin (menetelmä, aikaväli, alue).
3. Sisältö (tiedostot ja niiden suhde).
4. Käyttö ja rajoitukset.
5. Hanke, rahoittaja ja kiitokset.

Kirjoita selkeästi ja avaa lyhenteet (ks. `saavutettavuus`).
