# SeAMKedu Claude skills

Seinäjoen ammattikorkeakoulun (SEAMK) organisaatiolle tuotteistettuja Claude-skillejä (taitodokumentteja).

## Skillit

| Skill | Kuvaus |
|---|---|
| [`seamk-brandi`](skills/seamk-brandi/SKILL.md) | SEAMKin brändikäsikirjan (2025/03) mukaiset värit, typografia, tunnuksen käyttö, äänensävy ja ydinviestit. |
| [`saavutettavuus`](skills/saavutettavuus/SKILL.md) | Digipalvelulain ja EN 301 549 / WCAG 2.2 AA -vaatimukset SEAMKin ja hankkeiden materiaaleille (HTML, Word, PPT, PDF, video, some). |
| [`zenodo`](skills/zenodo/SKILL.md) | TKI-tuotosten tallennus Zenodoon DOI:lla: julkaisukelpoisuus, metatiedot, lisenssit, rahoittajatiedot ja API-skripti (oletuksena sandbox). |
| [`zenodo-julkaisu`](skills/zenodo-julkaisu/SKILL.md) | GitHub-repon julkaisu Zenodoon releasen kautta (OKM I2 -kelpoisuus) sekä Horizon Europe -hankkeiden avoimen saatavuuden tallennus ja raportointi. |
| [`nitroscope-julkaisuilmoitus`](skills/nitroscope-julkaisuilmoitus/SKILL.md) | NitroScope-hankkeen julkaisuilmoitus General Assemblylle (45 pv ennen), vastustusaikojen laskenta ja partnerilupien tarkistus. |
| [`nitroscope-rahoitusmerkinnat`](skills/nitroscope-rahoitusmerkinnat/SKILL.md) | NitroScope-tuotosten tarkistus: EU- ja SERI-merkinnät, vastuuvapauslauseke, kiitokset, nimeäminen ja OA-kelpoisuus. |

## Asennus

Pakkaa skillin kansio zipiksi (esim. `cd skills && zip -r seamk-brandi.zip seamk-brandi`) ja lataa se claude.ai:ssa kohdassa *Settings → Capabilities → Skills*, tai kopioi kansio Claude Coden `~/.claude/skills/`-hakemistoon.

## Huomio

Logotiedostot, viralliset PowerPoint-pohjat ja itse brändikäsikirja eivät sisälly tähän repoon. Ne löytyvät SEAMKin Intrasta ja Kuvapankista.
