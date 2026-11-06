---
name: "zenodo-julkaisu"
description: "Käytä, kun GitHub-repo (koodi, skill, data) tai Horizon Europe -hankkeen julkaisu/aineisto pitää julkaista Zenodossa DOI:lla (OKM:n I2, viitattavuus tai EU-hankkeen avoin saatavuus)."
---

# Zenodo-julkaisu GitHub-reposta

Tavoite: viedä repo Zenodoon, jotta se saa pysyvän DOI:n, oikeat metatiedot ja mahdollisimman vahvan I2-kelpoisuuden. DOI on pysyvä eikä sitä voi perua, joten edetään tarkistuslistan kautta, ja jokainen julkaiseva askel vahvistetaan käyttäjältä.

Jos tallennettava kuuluu Horizon Europe -hankkeeseen (esim. NitroScope, GA 101218902), noudata lisäksi luvun 8 ohjeita. Luku 8 koskee myös artikkeleita ja aineistoja, jotka tallennetaan Zenodoon käsin ilman GitHubia. Yleiset tallennusohjeet ja API-skripti ovat `zenodo`-skillissä.

## 0. Faktat ja rajat

- Zenodo on CERNin ylläpitämä avoin arkisto. Jokainen tallenne saa DOI:n, ja versioilla on lisäksi concept DOI, joka osoittaa aina uusimpaan versioon.
- GitHub-integraatio arkistoi jokaisen GitHub-releasen ja lukee metatiedot `.zenodo.json`-tiedostosta (ensisijainen) tai `CITATION.cff`-tiedostosta.
- Integraation kytkeminen vaatii käyttäjän omat kirjautumiset ja OAuth-hyväksynnän. Claude ei kirjaudu eikä hyväksy käyttöoikeuksia käyttäjän puolesta, vaan ohjaa käyttäjää.
- Testaa ensin hiekkalaatikossa `sandbox.zenodo.org`. Sen DOI:t eivät ole oikeita.

I2-ehdot (tiedonkeruun käsikirja, luku 3.2.2.6). Tarkista ajantasaisuus verkosta ennen käyttöä:
- Sovellus on julkinen ja arvioitavissa. Julkaisusta päättää normaalisti joku muu kuin tekijä, *tai* ulkopuolinen organisaatio on tilannut sovelluksen ja käyttää sitä.
- Sovelluksesta kirjataan vain ensimmäinen versio, ellei muutos ole merkittävä.
- Työ kuuluu tekijän tutkimus- tai asiantuntijatyöhön korkeakoulussa. Pääosin tekoälyn tuottama sisältö ilman omaa panosta ei kelpaa.
- I2:lle ilmoitetaan DOI tai pysyvä osoite.

## 1. Esitarkistus (luku vain, ei muutoksia)

Käy repo läpi ja raportoi puutteet taulukkona:

| Kohta | Tila | Korjaus |

- [ ] `LICENSE` on avoin lisenssi (MIT, Apache-2.0, EUPL-1.2, CC-BY-4.0 datalle).
- [ ] `README.md` sisältää käyttötarkoituksen yhdellä lauseella, asennuksen, esimerkin, viittausohjeen ja maininnan hankkeesta tai TKI-tehtävästä, jossa työ tehtiin.
- [ ] `CITATION.cff` sisältää tekijät, ORCIDit, korkeakouluaffiliaation, version, julkaisupäivän ja lisenssin.
- [ ] `.zenodo.json` sisältää `upload_type`, `creators` (nimi, ORCID, affiliaatio), `license`, `keywords`, `language` ja tarvittaessa `communities` sekä `related_identifiers`.
- [ ] CITATION.cff:n ja .zenodo.json:n tiedot ovat keskenään ristiriidattomia.
- [ ] Tekijän oma panos on kuvattu, jos koodia on tuotettu tekoälyavusteisesti (esim. README:n osio "Tekijän panos").
- [ ] Repossa ei ole salaisuuksia: avaimia, tokeneita, `.env`-tiedostoja eikä henkilötietoja.
- [ ] Repo on julkinen.
- [ ] Horizon Europe -hankkeen tuotoksissa myös luvun 8 metatiedot ja rahoitusmerkinnät.

## 2. I2-kelpoisuuden vahvistaminen

Pelkkä oma tallennus Zenodoon voi jäädä riippumattoman julkaisijan ehdon alle. Ehdota yhtä tai useampaa näistä ja kerro, että lopullisen tulkinnan tekee korkeakoulun kirjasto:

1. **Kuratoitu Zenodo-yhteisö (community)**, esimerkiksi korkeakoulun oma yhteisö. Kuraattori hyväksyy tallenteen, joten julkaisupäätöksen tekee joku muu kuin tekijä. Tarkista, onko korkeakoululla yhteisö.
2. **Ulkopuolinen tilaaja tai käyttäjä**, esimerkiksi hankekumppani. Dokumentoi se README:hen.
3. **Ohjelmistolehti**, esimerkiksi JOSS. Vertaisarvioitu ohjelmistoartikkeli voi kelvata myös tekstijulkaisuna.
4. **Kirjaston ennakkotulkinta.** Kysy organisaation ennakkotapauksia (esim. aiemmin hyväksyttyjä I2-tallenteita, joiden kustantajana on Zenodo).

## 3. Metatiedot

Luo tai täydennä tiedostot. Pohja tiedostolle `.zenodo.json`:

```json
{
  "title": "<nimi: mitä se tekee>",
  "upload_type": "software",
  "description": "<1–3 lausetta, mihin ongelmaan>",
  "creators": [{"name": "Sukunimi, Etunimi", "orcid": "0000-...", "affiliation": "<korkeakoulu>"}],
  "license": "MIT",
  "keywords": ["..."],
  "language": "fin",
  "communities": [{"identifier": "<yhteisö>"}],
  "related_identifiers": [{"identifier": "<sukulaisjulkaisun DOI>", "relation": "isSupplementTo"}]
}
```

`related_identifiers` sitoo LPU-sukulaiset (raportit, artikkelit, muut moduulit) toisiinsa läpinäkyvästi. Horizon Europe -hankkeessa lisää myös luvun 8 kentät.

## 4. Kytkentä (käyttäjä tekee, Claude ohjaa)

1. Kirjaudu Zenodoon GitHub- tai ORCID-tunnuksilla, ensin osoitteessa sandbox.zenodo.org.
2. Avaa Zenodossa *Account → GitHub* ja kytke repo päälle. Tämä vaatii OAuth-hyväksynnän.
3. Kytke repo ennen ensimmäistä releasea, koska Zenodo arkistoi vain kytkennän jälkeen tehdyt releaset.

## 5. Julkaisu (vahvistus ennen jokaista askelta)

1. Commitoi metatiedot ja tee tagi `v1.0.0`.
2. Ennen GitHub-releasen luomista kerro käyttäjälle, että tämä julkaisee pysyvän DOI:n, jota ei voi poistaa. Odota selvä kyllä.
3. Luo release (`gh release create v1.0.0 --notes ...`) tai ohjaa käyttäjää tekemään se GitHubissa.
4. Tarkista Zenodosta, että tallenne syntyi ja että tekijät, affiliaatio ja lisenssi ovat oikein. Korjaukset tehdään Zenodossa ennen yhteisöhyväksyntää.
5. Kun hiekkalaatikkotesti onnistuu, toista askeleet tuotanto-Zenodossa.

## 6. Jälkityöt

- Lisää concept DOI tiedostoon `CITATION.cff` (`identifiers`) ja README-badgeksi. Commitoi tämä ilman uutta releasea, jotta syntyvä versio ei sotke julkaisuvuotta.
- Kirjaa ilmoitus kirjastolle: nimi, tyyppi I2, tekijät, ORCIDit, DOI, julkaisuvuosi (v1.0.0:n vuosi), tieteenala ja I2-kelpoisuuden peruste (vaihe 2).
- Kerro käyttäjälle, että myöhemmät versiot (v1.1 jne.) saavat oman DOI:n mutta eivät ole uusia julkaisuja, ellei muutos ole merkittävä.
- Horizon Europe -hankkeessa tee myös luvun 8 raportointi.

## 7. Rajat

- Älä tee releasea, julkaise tai hyväksy OAuth-oikeuksia ilman käyttäjän nimenomaista vahvistusta kyseiselle askeleelle.
- Älä ehdota saman sovelluksen uusien versioiden ilmoittamista uusina I2-julkaisuina.
- Älä lisää tekijöitä ilman todellista panosta.
- Jos skill ajetaan yhdessä amk-lpu-suunnittelu-skillin kanssa, tämä skill hoitaa vaiheen 6 (metatiedot) ohjelmistoyksiköille.
- Älä tallenna kustantajan julkaistua versiota (publisher PDF), jos kustantajan ehdot eivät salli sitä; tallenna silloin hyväksytty käsikirjoitus (AAM).

## 8. Horizon Europe -hankkeen tuotokset (esim. NitroScope)

Lähde: NitroScope D1.1 Project Management Handbook v1.0, luku 4.3.2, sekä GA:n artikla 17 ja liite 5. NitroScopen sopimusnumero on **101218902**.

**Mitä ja milloin**
- Kaikki hankkeen tuloksiin liittyvät vertaisarvioidut julkaisut on oltava avoimesti saatavilla. Tallenna koneluettava kopio julkaistusta versiosta tai hyväksytystä käsikirjoituksesta repositorioon **mahdollisimman pian ja viimeistään julkaisupäivänä**, ja avoimen saatavuuden on alettava heti. Zenodo on OpenAIRE-yhteensopiva ja kelpaa repositorioksi; myös oman organisaation repositorio käy.
- Pyri tallentamaan samaan aikaan tulosten varmentamiseen tarvittava aineisto. Noudata hankkeen datanhallintasuunnitelmaa (D1.2), ja pseudonymisoi tai anonymisoi henkilötiedot.
- Lisenssiksi CC BY 4.0, ellei GA:n liite 5 salli muuta kyseiselle tuotokselle; tarkista tarvittaessa.

**Käsin tallennus (artikkeli tai aineisto ilman GitHubia)**
Ohjaa käyttäjää Zenodon *New upload* -lomakkeella: resurssityyppi (Publication → Journal article, tai Dataset), tiedosto, tekijät ORCIDeineen, lisenssi, julkaisupäivä, lehden DOI kohtaan related identifiers ("is version of" / "is supplement to"), ja funding-kenttä (alla). Julkaiseminen tehdään vain käyttäjän vahvistuksella, kuten luvussa 5. API-lataukseen käytä `zenodo`-skillin skriptiä.

**Pakolliset metatiedot**
- termit "European Union (EU)" ja "Horizon Europe"
- hankkeen nimi, akronyymi (NitroScope) ja sopimusnumero (101218902)
- julkaisupäivä
- pysyvä tunniste (DOI)

Zenodossa rahoitus syötetään Funding-kenttään hakemalla rahoittaja European Commission ja sopimus 101218902. Silloin OpenAIRE yhdistää tallenteen hankkeeseen. `.zenodo.json`-tiedostossa vastaava kenttä on muotoa

```json
"grants": [{"id": "10.13039/501100000780::101218902"}]
```

Tarkista kentän muoto ajantasaisesta Zenodon dokumentaatiosta ennen käyttöä ja varmista julkaisun jälkeen, että tallenteen sivulla näkyy oikea hanke. Kirjoita lisäksi kuvaukseen tai muistiinpanoihin lause "Funded by the European Union under the Horizon Europe Programme, NitroScope project, grant agreement No. 101218902."

**Rahoitusmerkinnät tallennettavassa tiedostossa**
Jos tiedosto on hankkeen oma (raportti, juliste, esitys, aineiston README), tarkista EU- ja SERI-merkinnät skillillä `nitroscope-rahoitusmerkinnat`.

**Raportointi**
- Lisää julkaisu ja aineisto hankkeen SharePointin Reporting-Excel-tiedostoon. WP7:n vetäjä ena siirtää ne F&T-portaalin Continuous reporting -osioon.
- Kun tallenne on kytketty hankkeeseen oikein, se näkyy portaalissa ehdotuksena "suggested by OpenAIRE". Kerro käyttäjälle, että tämä kannattaa tarkistaa muutaman viikon kuluttua.
- Ilmoita Steering Committeelle, kun julkaisu on hyväksytty (jos ei ole jo tehty).

Kirjoita käyttäjän kielellä, oletuksena suomeksi.
