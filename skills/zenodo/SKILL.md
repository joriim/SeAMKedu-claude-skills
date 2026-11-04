---
name: zenodo
description: Käytä, kun SEAMKin TKI-työn tuotos (data, raportti, posteri, esitys, ohjelmisto, opetusmateriaali, video) pitää tallentaa Zenodoon pysyvällä DOI:lla — metatiedot, lisenssi, rahoittajatieto, yhteisö, versiointi ja API-lataus.
---

# Zenodo-tallennus SEAMKin TKI-työssä

Tavoite: saada tuotos Zenodoon niin, että se on löydettävä, viitattava ja rahoittajan avoimuusvaatimusten mukainen, ja että se voidaan tarvittaessa ilmoittaa OKM:n julkaisutiedonkeruuseen. **DOI on pysyvä eikä julkaistua tallennetta voi poistaa**, joten jokainen julkaiseva askel vahvistetaan käyttäjältä erikseen.

Lue tarpeen mukaan:
- `references/metatiedot.md` — kenttäkohtainen ohje: tallennetyypit, tekijät, lisenssit, rahoittajat (grants), suhteet (related_identifiers), kielet, avainsanat. Lue aina ennen metatietojen kirjoittamista.
- `scripts/zenodo_api.py` — luonnoksen luonti, tiedostojen lataus, metatiedot ja uusi versio REST-rajapinnan kautta. Oletuksena hiekkalaatikko ja vain luonnos.
- GitHub-repon julkaisu releasen kautta: käytä `zenodo-julkaisu`-skilliä, jos se on asennettu. Muuten kohta 5 alla.

## 0. Faktat ja rajat

- Zenodo on CERNin ylläpitämä yleisarkisto. Jokainen julkaistu tallenne saa DOI:n. Versioiduilla tallenteilla on lisäksi **concept DOI**, joka osoittaa aina uusimpaan versioon. Viittaa concept DOI:hin, kun tarkoitat "tätä työtä yleensä", ja versio-DOI:hin, kun tarkoitat tarkkaa versiota.
- Julkaistun tallenteen **metatietoja voi muokata**, mutta **tiedostoja ei voi vaihtaa** ilman uutta versiota. Väärä tiedosto korjataan uudella versiolla, ja vanha versio jää näkyviin.
- Testaa aina ensin hiekkalaatikossa `sandbox.zenodo.org`. Sen DOI:t eivät ole oikeita, ja tunnus ja token ovat erilliset.
- Claude **ei kirjaudu, luo tunnuksia, hyväksy OAuth-oikeuksia eikä kirjoita tokeneita lomakkeisiin**. Käyttäjä luo tokenin itse (Zenodo → Applications → Personal access tokens, oikeudet `deposit:write` ja tarvittaessa `deposit:actions`) ja asettaa sen ympäristömuuttujaan `ZENODO_TOKEN`. Tokenia ei tulosteta, tallenneta tiedostoon eikä toisteta keskustelussa.
- Zenodo ei korvaa SEAMKin omaa julkaisuarkistoa. **Theseus** on ensisijainen paikka SEAMKin julkaisusarjojen raporteille ja opinnäytteille. Zenodo sopii erityisesti dataan, ohjelmistoihin, posteriin, esityksiin, kansainvälisen hankkeen tuotoksiin ja niiden rinnakkaistallenteisiin. Jos tuotos menee molempiin, linkitä ne toisiinsa (`related_identifiers`), älä luo kahta "alkuperäistä".

## 1. Tunnista tuotos ja tarkista, kuuluuko se Zenodoon

Kysy tai päättele:
1. **Mikä tuotos on?** → valitse `upload_type` (ks. metatiedot.md).
2. **Kenen nimissä ja mistä hankkeesta?** Tekijät, ORCIDit, affiliaatiot, hanke ja rahoittaja (esim. Horizon Europe -sopimusnumero, EAKR-hanketunnus).
3. **Onko jo olemassa toisaalla?** Theseus, kustantajan sivu, GitHub, aiempi Zenodo-tallenne. Jos on, kyseessä on rinnakkaistallenne tai uusi versio, ei uusi tallenne.
4. **Saako sen julkaista?** Ks. kohta 2.
5. **Kenelle ilmoitetaan?** SEAMKin kirjasto (julkaisutiedonkeruu), rahoittaja (esim. Horizon Europe -raportointi Funding & Tenders -portaalissa), hankkeen aineistonhallintasuunnitelma (DMP).

## 2. Julkaisukelpoisuuden tarkistus (luku vain, ei muutoksia)

Raportoi taulukkona: | Kohta | Tila | Korjaus |

- [ ] **Oikeudet**: kaikilla tekijöillä on lupa julkaista. Konsortiotuotoksissa konsortiosopimus ja rahoittajan ehdot sallivat avaamisen. Kolmannen osapuolen kuville, kartoille ja datalle on lupa tai yhteensopiva lisenssi.
- [ ] **Henkilötiedot ja tietosuoja**: ei tunnistettavia henkilöitä ilman suostumusta, ei viljelijöiden tai tilojen tunnistetietoja (nimet, tilatunnukset, tarkat lohkosijainnit) ilman lupaa. Tarvittaessa karkeista koordinaatit tai pseudonymisoi. Epäselvässä tapauksessa ohjaa SEAMKin tietosuojavastaavalle.
- [ ] **Liikesalaisuudet ja kumppanidata**: yritysten luovuttama data vain sopimuksen salliessa.
- [ ] **Patentoitavuus**: jos tuotoksessa voi olla keksintö, julkaisu vie uutuuden. Kysy käyttäjältä ennen jatkamista.
- [ ] **Tiedostomuodot**: avoimet ja pitkäikäiset (CSV, GeoPackage, GeoTIFF/COG, NetCDF, PDF/A, PNG, TXT/MD). Suljetuille muodoille rinnalle avoin versio.
- [ ] **README / kuvaus**: datalle README, jossa sarakkeet, yksiköt, menetelmä, koordinaattijärjestelmä, puuttuvien arvojen merkintä ja aikaväli.
- [ ] **Saavutettavuus**: PDF:t ja esitykset tagattuja ja saavutettavia (ks. `saavutettavuus`-skill). Zenodoon viety SEAMKin julkaisema sisältö kuuluu digipalvelulain piiriin.
- [ ] **Koko**: enintään 50 Gt ja 100 tiedostoa tallennetta kohden. Suuremmat aineistot pilkotaan tai pakataan, ja kysytään Zenodolta tarvittaessa lisätilaa.
- [ ] **Salaisuudet**: ei API-avaimia, salasanoja, `.env`-tiedostoja tai sisäisiä polkuja.

Jos jokin kohta on punaisella, älä jatka kohtaan 4 ennen kuin käyttäjä on ratkaissut sen. Vaihtoehtona on rajoitettu pääsy (`access_right: restricted`) tai embargo (`embargoed` + `embargo_date`), jolloin metatiedot ja DOI ovat avoimia mutta tiedostot eivät.

## 3. Metatiedot

Kirjoita metatiedot JSON-tiedostoon `zenodo-metadata.json` (pohja ja kenttäohjeet: `references/metatiedot.md`). Vähimmäistaso SEAMKissa:

- **title**: kuvaava, mitä ja missä. Hankkeen nimi alaotsikkona, ei ainoana otsikkona.
- **creators**: `"Sukunimi, Etunimi"`, ORCID ja affiliaatio. SEAMKin affiliaatio muodossa `Seinäjoki University of Applied Sciences` (sama kuin ROR-rekisterissä; tarkista ROR-tunnus verkosta, älä keksi sitä).
- **description**: mitä, miksi, miten ja missä tuotettiin, 1–3 kappaletta. Mainitse hanke ja rahoittaja tekstissä.
- **license**: avoin lisenssi, ks. metatiedot.md. Oletus: CC-BY-4.0 julkaisuille ja datalle, MIT tai Apache-2.0 koodille, EUPL-1.2 julkishallinnon ohjelmistolle tarvittaessa.
- **keywords**: 5–10, suomeksi ja englanniksi.
- **language**: ISO 639-3 (`fin`, `eng`, `swe`).
- **grants**: rahoitussopimus, jos rahoittaja on Zenodon/OpenAIREn tuntema (esim. EU:n Horizon Europe). Muotoa `{"id": "10.13039/501100000780::<sopimusnumero>"}`. **Älä arvaa sopimusnumeroa** — kysy käyttäjältä tai tarkista hankkeen sivuilta.
- **communities**: hankkeen tai SEAMKin Zenodo-yhteisö, jos sellainen on. Tarkista olemassaolo haulla `zenodo.org/communities` ennen lisäämistä; älä keksi yhteisön tunnistetta.
- **related_identifiers**: linkit sukulaistuotoksiin (artikkeli, Theseus-raportti, GitHub-repo, aiempi data).

Näytä valmiit metatiedot käyttäjälle taulukkona ennen latausta ja pyydä hyväksyntä.

## 4. Lataus

**Selainkäyttö (suositus kertaluonteisiin tallenteisiin):** ohjaa käyttäjää: Zenodo → *New upload* → lataa tiedostot → täytä kentät hyväksytyistä metatiedoista → *Save* → tarkista esikatselu → *Publish*. Claude voi täyttää kenttiä selaimessa vain käyttäjän pyynnöstä, ei koskaan paina *Publish*-painiketta ilman nimenomaista vahvistusta, eikä kirjoita tunnuksia.

**API (toistuvat tai monitiedostoiset tallenteet):**

```bash
export ZENODO_TOKEN=...   # käyttäjä asettaa itse
python scripts/zenodo_api.py create --metadata zenodo-metadata.json --files data/*.csv README.md
# → tulostaa luonnoksen id:n, varatun DOI:n ja esikatselulinkin (sandbox oletuksena)
python scripts/zenodo_api.py publish --id <id> --confirm
python scripts/zenodo_api.py newversion --id <id> --metadata zenodo-metadata.json --files ...
```

- Tarkista metatiedot ensin: `python scripts/zenodo_api.py check --metadata zenodo-metadata.json`.
- Oletuksena `sandbox.zenodo.org`. Tuotantoon vain `--production`-lipulla ennen alikomentoa (`zenodo_api.py --production create ...`), ja tuotannolla on oma token.
- `create` luo **luonnoksen** ja varaa DOI:n (`prereserve_doi`). Varattu DOI ei ole vielä voimassa, mutta sen voi kirjoittaa README:hen tai raporttiin ennen julkaisua.
- `publish` vaatii `--confirm`-lipun. **Ennen kuin ajat publishin, kerro käyttäjälle, että julkaisu on pysyvä, ja odota selvä kyllä tälle nimenomaiselle tallenteelle.** Edellinen hyväksyntä ei kata seuraavaa tallennetta.

## 5. GitHub-repo

Jos `zenodo-julkaisu`-skill on käytettävissä, käytä sitä. Muuten lyhyesti:
1. Lisää repoon `LICENSE`, `CITATION.cff` ja `.zenodo.json` (`.zenodo.json` ohittaa CITATION.cff:n Zenodossa; pidä ne ristiriidattomina).
2. Käyttäjä kytkee repon Zenodossa (*Account → GitHub*). Vain kytkennän jälkeen tehdyt releaset arkistoituvat.
3. Release (`v1.0.0`) luo tallenteen. Vahvista käyttäjältä ennen releasea.
4. Lisää concept DOI README-badgeksi ja `CITATION.cff`:n kenttään `identifiers`.

## 6. Julkaisun jälkeen

- Tarkista tallenteesta: DOI ratkeaa, tekijät, ORCIDit, affiliaatio, lisenssi ja rahoittaja näkyvät oikein, tiedostot aukeavat.
- Lisää DOI ja viittausohje hankkeen sivuille, DMP:hen ja liittyviin julkaisuihin.
- **Julkaisutiedonkeruu**: kerro käyttäjälle, mitkä tiedot kirjastolle ilmoitetaan (nimi, tekijät, ORCIDit, DOI, vuosi, tyyppi, hanke). Tyyppiluokituksen (esim. I2 ohjelmisto, D-/E-luokan julkaisu, posteri, avoin data) ja kelpoisuuden ratkaisee SEAMKin kirjasto ajantasaisen OKM:n tiedonkeruun käsikirjan mukaan. Jos tuotoksen pilkkominen julkaisuiksi on auki, käytä `amk-lpu-suunnittelu`-skilliä.
- **Rahoittajaraportointi**: Horizon Europe -hankkeissa vertaisarvioidut julkaisut ja tutkimusdata kuuluu ilmoittaa hankkeen jaksoraportissa. Zenodo-tallenne, jossa on oikea `grants`-kenttä, näkyy myös OpenAIREssa.
- Myöhemmät korjaukset: metatiedot → *Edit* olemassa olevaan tallenteeseen. Tiedostot → uusi versio (`newversion`).

## 7. Rajat

- Älä julkaise, tee releasea tai hyväksy OAuth-oikeuksia ilman käyttäjän vahvistusta kyseiselle askeleelle.
- Älä keksi ORCIDeja, sopimusnumeroita, ROR-tunnuksia, yhteisöjen tunnisteita tai DOI:ta. Puuttuva tieto merkitään `TODO` ja kysytään.
- Älä lisää tekijöitä ilman todellista panosta, äläkä jätä pois henkilöitä, joilla panos on.
- Älä tallenna samaa tuotosta useaan kertaan eri DOI:lla. Muutokset ovat versioita.
- Jos aineisto sisältää henkilötietoja tai luottamuksellista kumppanidataa eikä lupaa ole varmistettu, pysähdy ja kerro syy.

Kirjoita käyttäjän kielellä, oletuksena suomeksi. Zenodon metatiedot englanniksi, ellei käyttäjä toisin pyydä; tiivistelmä voi olla myös kaksikielinen.
