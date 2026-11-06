---
name: nitroscope-rahoitusmerkinnat
description: Käytä, kun NitroScope-hankkeen tuotos (artikkeli, diat, posteri, raportti) pitää tarkistaa ennen julkaisua: EU- ja SERI-merkinnät, vastuuvapauslauseke, kiitokset, nimeäminen ja OA-kelpoisuus.
---

# NitroScope-rahoitusmerkintöjen tarkistus

Lähde: NitroScope D1.1 Project Management Handbook and Quality Assurance Plan v1.0 (17.12.2025), luvut 1.6.3, 2.2.3, 4.1.1 ja 4.3.2. Logot ja tarkemmat visuaaliset ohjeet ovat projektin SharePointissa (Templates, NitroScope Project Guidelines). Jos käyttäjä antaa uudemman käsikirjan tai viestintäsuunnitelman (D7.1–D7.3), noudata sitä.

Skill tarkistaa valmiin tai lähes valmiin tuotoksen. Se ei muuta käyttäjän tiedostoa ilman pyyntöä; korjaukset tehdään kopioon ja palautetaan samassa muodossa.

## 1. Lue tuotos

Avaa tiedosto sen muodon mukaisella työkalulla (docx, pptx, pdf). Diojen ja postereiden logot tarkistetaan katsomalla renderöityä sivua, ei pelkkää tekstiä.

## 2. Tarkistuslista

Raportoi taulukkona: | Kohta | Löytyi / puuttuu / virheellinen | Sijainti | Korjaus |

**Pakolliset**

1. **EU-lippulogo** ("Funded by the European Union"). Jos samassa näkymässä on muita logoja, EU-logon on oltava riittävän näkyvä (appropriate prominence).
2. **Vastuuvapauslauseke sanatarkasti:**
   > Views and opinions expressed are however those of the author(s) only and do not necessarily reflect those of the European Union or the European Research Executive Agency (REA). Neither the European Union nor the granting authority can be held responsible for them.

   Vertaa merkki merkiltä. Yleisiä virheitä: "European Commission" REA:n paikalla, puuttuva "(REA)", vanha Horizon 2020 -muotoilu.
3. **SERI-logo** ja lause sanatarkasti:
   > This work has received funding from the Swiss State Secretariat for Education, Research and Innovation (SERI).

**Suositellut**

4. **Kiitos (acknowledgement):**
   > The authors acknowledge the funding by the European Union through the NitroScope project (grant agreement No. 101218902) under the Horizon Europe Programme.

   Sopimusnumeron on oltava täsmälleen 101218902. Artikkeleissa tämä kuuluu Acknowledgements- tai Funding-osioon; lehden funding-kenttään syötetään European Union, Horizon Europe, 101218902.
5. **Projektilogo** etusivulla ja EU-logo ensimmäisen sivun alatunnisteen vasemmassa reunassa (dokumentit).

**Tiedostomuoto ja nimeäminen**

6. Ulos lähtevä versio on pdf (sisäisesti doc/docx tai ppt/pptx).
7. Nimeäminen:
   - deliverable: `NitroScope_Dw.n_Title_vX.Y`
   - kokousdokumentti: `NitroScope_YYYYMMDD_Type of Meeting_Location_Type of Doc_vx.y`
   - konferenssiesitys: `NitroScope_YYYYMMDD_Event_Location_Initials/Organisation_vx.y`
   - versiot: luonnokset v0.1, v0.2 …, lopullinen v1.0
8. Esityksissä on käytetty hankkeen PowerPoint-pohjaa, jos kyse on ulkoisesta esityksestä.

**Vertaisarvioidut julkaisut: avoin saatavuus**

9. Kohdelehden malli:
   - Gold OA -lehti: julkaisumaksu (APC) on hyväksyttävä kulu.
   - **Hybridilehti: APC ei ole hyväksyttävä kulu.** Silloin käytetään rinnakkaistallennusta (Green OA), jonka on oltava mahdollista ilman embargoa.
   - Open Research Europe on maksuton vaihtoehto.

   Jos lehden mallia ei tiedetä, tarkista se verkosta (lehden sivu, Sherpa Romeo, DOAJ) ja kerro lähde.
10. Käsikirjoitukseen ei ole jäänyt toisen partnerin julkaisemattomia tuloksia ilman kirjallista lupaa, ja GA-ilmoitus on tehty (skill `nitroscope-julkaisuilmoitus`). Kysy käyttäjältä, jos et voi päätellä tätä.

## 3. Korjaukset

Kun käyttäjä pyytää korjaamaan, lisää puuttuvat tekstit sanatarkasti ja logot SharePointista saaduista tiedostoista. Logoja ei piirretä eikä haeta muualta. Jos logotiedostoja ei ole käytettävissä, merkitse paikka ja pyydä käyttäjää lisäämään ne.

Jos tuotos tehdään samalla SEAMKin nimissä, aja myös `seamk-brandi` ja tarvittaessa `saavutettavuus`. EU-logon näkyvyysvaatimus menee organisaatiobrändin edelle.

## Rajat

- Älä muotoile vastuuvapauslauseketta tai SERI-lausetta uudelleen; ne ovat sanatarkkoja.
- Älä väitä lehden OA-mallia tarkistamatta.

Kirjoita käyttäjälle suomeksi; lisättävät tekstit ovat englanniksi.
