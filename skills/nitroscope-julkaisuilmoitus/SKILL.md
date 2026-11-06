---
name: nitroscope-julkaisuilmoitus
description: Käytä, kun NitroScope-hankkeen tuloksia ollaan julkaisemassa (artikkeli, esitelmä, posteri, abstrakti): GA-ilmoitus 45 pv ennen, aikataulu ja partnerilupien tarkistus.
---

# NitroScope-julkaisuilmoitus

Lähde: NitroScope D1.1 Project Management Handbook and Quality Assurance Plan v1.0 (17.12.2025), luku 4.3.1. Täydelliset säännöt ovat Consortium Agreementin luvussa 8.3 sekä Grant Agreementin artiklassa 17 ja liitteessä 5 (GA 101218902). Jos käyttäjä antaa uudemman käsikirjan version, noudata sitä.

Skill koskee kaikkea, millä hankkeen tuloksia tai tietoa esitetään konsortion ulkopuolelle: lehtiartikkeleita, konferenssiabstrakteja ja -esitelmiä, postereita, käsikirjoituksia ja preprinttejä.

## 1. Kerää tiedot

Kysy vain se, mikä puuttuu:
- julkaisun tyyppi ja työnimi
- kohdelehti tai -tapahtuma ja **suunniteltu lähetyspäivä** (submission) tai abstraktin takaraja
- kirjoittajat ja heidän organisaationsa
- abstrakti (luonnos riittää)
- työpaketti tai -paketit (WP)
- sisältääkö julkaisu **toisen partnerin julkaisemattomia tuloksia tai taustatietoa (background)**
- onko julkaisu samalla hankkeen deliverable (esim. D3.6 tai D3.7, peer-reviewed publication)

## 2. Laske aikataulu

Säännöt:
- Ilmoitus General Assemblylle **vähintään 45 kalenteripäivää ennen** lähetystä.
- Partnereilla on **30 kalenteripäivää** aikaa vastustaa. Jos vastalausetta ei tule, saa julkaista.
- Perusteltu vastalause voi lykätä julkaisua **enintään 45 kalenteripäivää** vastalauseen esittämisestä. Sen jälkeen saa julkaista, kunhan vastustajan osoittamat luottamukselliset tiedot on poistettu.

Laske päivämäärät koodilla, älä päässä:

```python
from datetime import date, timedelta
submit = date(2027, 3, 1)          # suunniteltu lähetys
notify_by = submit - timedelta(45)  # viimeinen ilmoituspäivä
# jos ilmoitus lähetetään päivänä n:
n = notify_by
objection_end = n + timedelta(30)
worst_case = objection_end + timedelta(45)  # vastalause viimeisenä päivänä + max lykkäys
```

Esitä taulukkona: viimeinen ilmoituspäivä, vastustusajan loppu ja pahimman tapauksen julkaisupäivä. Jos viimeinen ilmoituspäivä on jo mennyt, sano se suoraan ja ehdota, että ilmoitus lähetetään heti ja lähetystä siirretään tai asiasta kysytään koordinaattorilta (UGent). Älä väitä aikataulua sääntöjen mukaiseksi, jos se ei ole.

## 3. Partnerien tulokset

Toisen partnerin tuloksia tai taustatietoa ei saa käyttää missään julkaisussa ilman **kirjallista lupaa**, ellei niitä ole jo julkaistu. Jos käyttäjä vastasi kyllä kohdassa 1, listaa partnerit ja luonnostele lyhyt lupapyyntö jokaiselle. Lupa on hankittava erikseen; GA-ilmoitus ei korvaa sitä.

## 4. Luonnostele ilmoitus

Vastaanottaja: **nitroscope.ga@lists.ugent.be**

Aiherivi hankkeen käytännön mukaan: `NitroScope: WPx – Publication notice – <lyhyt otsikko>`

Runko englanniksi:

```
Dear NitroScope General Assembly,

In line with Section 4.3.1 of the Project Handbook (D1.1) and Section 8.3 of the Consortium Agreement, I hereby notify the consortium of a planned publication.

Type: <journal article / conference abstract / poster / ...>
Working title: <...>
Authors and affiliations: <...>
Target journal / event: <...>
Planned submission date: <YYYY-MM-DD>
Related WP(s): <...>
Use of other beneficiaries' results or background: <none / yes, written approval obtained from ...>

Abstract:
<...>

Objections can be raised within 30 calendar days of this notice (by <YYYY-MM-DD>).

Best regards,
<nimi, organisaatio>
```

Näytä luonnos käyttäjälle. Lähetä se vain, jos käyttäjä erikseen pyytää lähettämään ja sähköpostiyhteys on käytettävissä.

## 5. Jälkitoimet (muistilista käyttäjälle)

- Merkitse kalenteriin vastustusajan loppu.
- Kun julkaisu hyväksytään julkaistavaksi, ilmoita Steering Committeelle (seurantaa varten).
- Ennen lähetystä tarkista rahoitusmerkinnät skillillä `nitroscope-rahoitusmerkinnat`.
- Julkaisun jälkeen hoida avoin saatavuus ja raportointi (skill `zenodo-julkaisu`, Horizon Europe -osio, tai `zenodo`).
- Jos julkaisu on deliverable, työpaketin vetäjä raportoi sen F&T-portaalin Continuous reporting -moduulissa ja deliverable kulkee käsikirjan mukaisen sisäisen arvioinnin kautta.

## Rajat

- Skill ei tulkitse vastalauseiden oikeutusta juridisesti. Perusteltu vastalause on vain sellainen, joka vahingoittaisi merkittävästi vastustajan akateemisia tai kaupallisia etuja tai heikentäisi sen tulosten tai taustatiedon suojaa, ja siinä on pyydettävä täsmällisiä muutoksia. Riitatilanteet ohjataan koordinaattorille.
- Älä lähetä sähköpostia ilman käyttäjän nimenomaista pyyntöä.

Kirjoita käyttäjälle suomeksi, ilmoitukset konsortiolle englanniksi.
