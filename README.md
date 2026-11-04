# SeAMKedu Claude skills

Seinäjoen ammattikorkeakoulun (SEAMK) organisaatiolle tuotteistettuja Claude-skillejä (taitodokumentteja).

## Skillit

| Skill | Kuvaus |
|---|---|
| [`seamk-brandi`](skills/seamk-brandi/SKILL.md) | SEAMKin brändikäsikirjan (2025/03) mukaiset värit, typografia, tunnuksen käyttö, äänensävy ja ydinviestit. |
| [`saavutettavuus`](skills/saavutettavuus/SKILL.md) | Digipalvelulain ja EN 301 549 / WCAG 2.2 AA -vaatimukset SEAMKin ja hankkeiden materiaaleille (HTML, Word, PPT, PDF, video, some). |
| [`zenodo`](skills/zenodo/SKILL.md) | TKI-tuotosten tallennus Zenodoon DOI:lla: julkaisukelpoisuus, metatiedot, lisenssit, rahoittajatiedot ja API-skripti (oletuksena sandbox). |

## Asennus

Pakkaa skillin kansio zipiksi (esim. `cd skills && zip -r seamk-brandi.zip seamk-brandi`) ja lataa se claude.ai:ssa kohdassa *Settings → Capabilities → Skills*, tai kopioi kansio Claude Coden `~/.claude/skills/`-hakemistoon.

## Huomio

Logotiedostot, viralliset PowerPoint-pohjat ja itse brändikäsikirja eivät sisälly tähän repoon. Ne löytyvät SEAMKin Intrasta ja Kuvapankista.
