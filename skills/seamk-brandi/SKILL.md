---
name: seamk-brandi
description: Käytä aina, kun tehdään SEAMKin (Seinäjoen ammattikorkeakoulu) nimissä viestintää tai materiaalia — esitykset, dokumentit, julisteet, somepostaukset, verkkosivut, hanke- ja TKI-viestintä, tiedotteet — jotta värit, typografia, tunnus, äänensävy ja ydinviestit noudattavat SEAMKin brändikäsikirjaa (2025/03).
---

# SEAMK-brändi

Tiivistys SEAMKin brändikäsikirjasta ja graafisesta ohjeistosta (versio 2025/03). Lue tämä tiedosto aina. Lue lisäksi tarpeen mukaan:

- `references/viestinta.md` — viestinnän tavoitteet, äänensävy, ydinviestit 1–4, "Miten viestimme". Lue, kun kirjoitat tekstiä (somepostaus, uutinen, tiedote, esittely, hakemuksen viestintäosio).
- `references/visuaalinen-ilme.md` — tunnus, suoja-alue, typografia, värit, PPT-pohjat, käyntikortit, somemainokset, tuotteet, Intran ohjeet ja yhteystahot. Lue, kun teet visuaalista materiaalia.
- `assets/seamk-colors.css`, `assets/seamk_colors.py`, `assets/seamk-tokens.json` — valmiit värimuuttujat. Käytä näitä, älä kirjoita värikoodeja käsin.

## Pikasäännöt

**Nimi.** Kirjoita **SEAMK** (isoin kirjaimin). Taivutus: SEAMKin, SEAMKissa, SEAMKiin. Virallinen nimi: Seinäjoen ammattikorkeakoulu / Seinäjoki University of Applied Sciences. Vanhaa muotoa "SeAMK" ei käytetä uudessa materiaalissa.

**Värit** (ainoat viralliset arvot — älä keksi muita):

| Rooli | Nimi | HEX | RGB | CMYK | Pantone |
|---|---|---|---|---|---|
| Pääväri 1 | Lila | `#542583` | 84, 37, 131 | 84, 100, 3, 1 | PMS 267 C |
| Pääväri 2 | Keltainen | `#FFF023` | 255, 240, 35 | 5, 0, 84, 0 | Process Yellow C |
| Lisäväri | Vihreä | `#ACD195` | 172, 209, 149 | 39, 0, 52, 0 | PMS 359 |
| Lisäväri | Pinkki | `#E8A7C6` | 232, 167, 198 | 7, 44, 4, 0 | PMS 210 |
| Lisäväri | Vaaleansininen | `#C7E6F7` | 199, 230, 247 | 26, 1, 2, 0 | PMS P 115 |

- Päävärit (lila + keltainen) ovat verkkosivujen ja markkinointimateriaalien päävärit.
- Lisävärit vain infografiikkaan, taulukoihin, kuvioihin, jakotavaroihin yms. — ei pääpinnoiksi.
- Tunnusvärit (sininen, syaani, vihreä) kuuluvat vain logoon. Ohjeistossa ei ole niille arvoja, joten niitä ei käytetä muuhun.
- Päävärejä saa vaalentaa (sävyt 75/50/25/15 %, ks. assets), jotta teksti erottuu.

**Hyväksytyt väriyhdistelmät tekstille** (WCAG-kontrasti laskettu):
- Valkoinen teksti lilalla 10,7:1 ✔ · Lila teksti valkoisella ✔
- Musta teksti keltaisella 17,7:1 ✔ · Lila teksti keltaisella 9,0:1 ✔
- Lila teksti vaalealla lilasävyllä (25 % / 15 %) 6,7:1 / 8,1:1 ✔
- Musta teksti kaikilla lisäväreillä ✔
- ✘ **Ei koskaan** valkoista tekstiä keltaisella (1,2:1) eikä lisävärien päällä (1,3–2,0:1).
- Älä välitä merkitystä pelkällä värillä (esim. kaavioissa lisää myös nimiöt tai kuviot).

**Typografia:**
- Markkinointi (painettu ja sähköinen): **Acumin Pro** -perhe ensisijaisesti; Adobe Caslon Pro on virallinen serif-täydennys.
- PowerPoint, Word, Excel, sähköiset lomakkeet: otsikot **Alte DIN 1451 Mittelschrift**, leipäteksti **Arial**.
- Visuaalinen tyyli: otsikot usein ISOIN KIRJAIMIN, tiivis groteski, lihava (kuten "HAE MEILLE", "SYKSYN YHTEISHAKU").
- Verkkoartifakteissa, joissa lisensoituja fontteja ei ole: otsikot `"Alte DIN 1451 Mittelschrift", "Barlow Condensed", "Arial Narrow", sans-serif`, leipäteksti `Arial, Helvetica, sans-serif`. Kerro käyttäjälle, että Barlow Condensed on korvike.

**Tunnus (logo):**
- **Älä piirrä, rekonstruoi tai kirjoita logoa tekstinä logon tilalle.** Käytä aina originaalitiedostoja SEAMKin Kuvapankista (SharePoint: SeAMK-Staff → Kuvapankki). Jos tiedostoa ei ole saatavilla, jätä selkeästi merkitty paikka ("[SEAMK-tunnus]") ja kerro käyttäjälle.
- Kolme versiota: värillinen (ensisijainen, valkoisella pohjalla), valkoinen (kuvan tai tumman väripinnan päällä), musta (vaaleilla väripohjilla).
- Suoja-alue = logon E-kirjaimen koko joka suuntaan; sen sisälle ei tekstiä, kuvia eikä grafiikkaa.
- Ei venytystä, suhteiden muuttamista, värien vaihtamista, efektejä eikä sijoittamista kirjavan kuvan päälle ilman riittävää kontrastia.

**Esitykset:** SEAMKin omissa esityksissä käytetään aina virallista PowerPoint-pohjaa (Intra). Pohjan tyylejä ei muuteta, ja pohjan kolmea väriversiota ei sekoiteta samassa esityksessä. Jos teet esitystä ilman pohjaa, noudata yllä olevia värejä ja fontteja ja kerro käyttäjälle, että lopullinen versio kannattaa siirtää viralliseen pohjaan.

**Äänensävy lyhyesti:** helposti lähestyttävä, aito, me-henkinen ja tekemisen meininkiä välittävä. Käytä "Meillä SEAMKissa" -ilmausta, kun se luontuu. Kerro esimerkein ja ihmisten kautta, ilman muodollisuuksia. Kriittisistäkin asioista saa viestiä, kunhan linja on yhtenäinen. Viesti tarvittaessa kahdella kielellä (suomi + englanti). Tarkemmin: `references/viestinta.md`.

**Ydinviestit** (huomioi soveltuvin osin):
1. SEAMK on helposti lähestyttävä yhteisö, jossa on tekemisen meininki.
2. SEAMK on paras korkeakoulu opiskelijalle.
3. SEAMKilla on vahvat vahvuusalat — asiantuntemuksemme on Suomen huippua; SEAMKista löytää kansainväliset osaajat.
4. Meillä työskentelet huippuporukan kanssa laadukkaassa ympäristössä.

## Työnkulku

1. Tunnista tuotos (teksti / esitys / dokumentti / some / verkko / painotuote) ja kohderyhmä (hakijat, opiskelijat, henkilöstö, yritykset, media, kansainväliset).
2. Lue tarvittava viitetiedosto.
3. Tee tuotos. Ota värit assets-tiedostoista. Käytä logoa vain originaalitiedostona.
4. Tarkista ennen luovutusta:
   - [ ] vain viralliset värit; lisävärit vain tukielementeissä
   - [ ] tekstin ja taustan kontrasti hyväksyttyjen yhdistelmien mukainen
   - [ ] fontit oikein (tai korvike mainittu)
   - [ ] logo originaalina, suoja-alue kunnossa, ei muokattu
   - [ ] nimi kirjoitettu "SEAMK", taivutus oikein
   - [ ] äänensävy ja vähintään yksi ydinviesti läsnä, kun kyse on ulkoisesta viestinnästä
   - [ ] saavutettavuus: alt-tekstit, otsikkotasot, ei pelkkää väriä merkityksen kantajana
5. Kerro käyttäjälle lyhyesti, missä poikettiin ohjeistosta (esim. fonttikorvike) ja miksi.

## Rajaukset

- Tämä skill ei korvaa virallisia pohjia eikä logotiedostoja — ne haetaan SEAMKin Intrasta / Kuvapankista.
- Hankeviestinnässä rahoittajan (esim. EU, Horizon Europe, Interreg) logo- ja näkyvyysvaatimukset ovat SEAMKin ilmeen lisäksi pakollisia; noudata rahoittajan ohjetta niiden osalta.
- Epäselvissä tapauksissa ohjaa käyttäjä SEAMKin markkinointiin ja viestintään: markkinointi@seamk.fi.
