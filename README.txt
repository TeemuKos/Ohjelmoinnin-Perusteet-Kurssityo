Ohjelman tarkoituksena on toimia sähköisenä reseptikirjana, jolla on seuraavat toiminnallisuudet

-Lisätä resepti
-Poistaa resepti tai kaikki reseptit kerralla
-Lukea reseptejä
-Muokata reseptejä
-Tehdä ruokalista käyttäjän määrittämän ruokien määrän mukaan
-Katsella viimeistä ruokalistaa
-Tallentaa listat tiedostoihin .pkl
-Lataa listat tiedostoista .pkl

- Kaikki reseptikirjan ja ruokalistojen objektit ovat olioita
- olioilla on metodeja, joita kutsutaan käyttäjän määrittämän toiminnallisuuden myötä
- Koodissa funktioita, jotka lyhentävät koodia toistojen osalta

Käyttäjä valitsee aloituksessa haluamansa toiminnallisuuden numerolla, jotka printataan nähtäväksi. Lisää resepti kysyy ensimmäisenä reseptin nimen, jos tässä kohtaa käyttäjä jättää rivin tyhjäksi, palataan alkunäyttöön. Nimen jälkeen ohjelma kysyy raaka-aineita, minkä jälkeen kysytään valmistusohjetta. Kummassakin kohtaa ohjelma vaatii käyttäjää syöttämään vähintään yhden rivin tietoja.

Poista resepti antaa käyttäjälle mahdollisuuden poistaa reseptikirjasta reseptin numerolla tai vastaamalla "kaikki" poistetaan kaikki. Ohjelma varmistaa "k" tai "e" kysymyksellä poiston.

Muokkaa reseptiä antaa käyttäjälle ensiksi koko reseptikirjan nimet tulostettuna, jonka jälkeen käyttäjä voi valita näistä reseptin mitä muokata. Tämän jälkeen ohjelma kysyy mitä käyttäjä haluaa muokata (nimi,raaka-aineet vai ohje)

Tee ruokalista, kertoo käyttäjälle kuinka monta reseptiä reseptikirjassa on. Tämän jälkeen ohjelma kysyy, kuinka monta reseptiä halutaan viiikon ruokalistalle. Käyttäjän määrittämän syötteen mukaan ohjelma arpoo niin monta reseptiä, kuin käyttäjä on määrittänyt. Ohjelma myös varmistaa, ettei samaa reseptiä tule kahteen kertaan

Viimeisin ruokalista tulostaa aiemmin tehdyn ruokalistan, minkä reseptejä käyttäjä pystyy tarkastelemaan syöttämällä reseptin tulostetun numeron.

Ohjelma automaattisesti käynnistettäessä yrittää avata tiedostoja reseptikirja.pkl ja ruokalista.pkl. Jos nämä eivät onnistu, ohjelma jatkaa toimintaansa. Syötettäessä ruokalistaan uusi resepti, ohjelma luo tiedoston reseptikirja.pkl ja tulostaa käyttäjän määrittämän reseptin tiedostoon.


!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!Huom!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
 
Ohjelma ei löydä .pkl tiedostoja muualta, kuin samasta kansiosta, missä ohjelma sijaitsee. Halutessasi tutkia ohjelman toimintaa ilman valmiita .pkl tiedostoja, aja ohjelma, kuten se on kansiorakenteessa. Halutessasi käyttää valmiita "testi" .pkl tiedostoja, kopioi ne kansiosta testitiedostot ohjelman omaan kansioon.

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!



https://github.com/Teemu-Kostamo/Ohjelmoinnin-Perusteet-Kurssityo
