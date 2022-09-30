import pickle
from random import randrange
from luokka import ruoka,ReseptiKirja
import os

def ValmisteleSivu(valinta):
    print('\n'*40)
    if valinta == 1:
        print("Luodaan uusi resepti")
    elif valinta == 2:
        print("Minkä reseptin haluat poistaa?")
    elif valinta == 3:
        print("Kaikki reseptisi")
    elif valinta == 4:
        print("Luodaan uusi ruokalista!")
    else:
        None
    print()

def Enter():
    print()
    input("Paina enter jatkaaksesi")

def MoniRivi():                                                                                 #Toimintaehdotus: Varmista, että edes yhdellä rivillä arvo!
    sana = ""
    while True:
        arvo = input()
        if arvo == "":                  
            break
        else:
            sana += '\n' + "-" +arvo
    print('\n'*40)
    return sana

def PoistaToiminto(valinta,lista):
    print('\n'*40)
    if valinta.isnumeric():
        listaIndeksi = int(valinta) - 1
        print()
        print("Olet poistamassa reseptiä: ", lista[listaIndeksi].nimi)

    elif valinta.lower() == "kaikki":
        print()
        print("Olet poistamassa kaikki reseptit")
    return listaIndeksi
                                                                                                    #TÄÄLLÄ VIRHE!!!!
def PoistaVarmistus(lista, indeksi, valinta,poistoVarmistus):                                       #EI POISTA KAIKKIA!!!!
    print('\n'*40)
    if poistoVarmistus == "k" and valinta.isnumeric():
        print("Poistit reseptin: ",lista[indeksi].nimi, " reseptikirjasta")
        del lista[indeksi]
    elif poistoVarmistus == "k" and valinta == "kaikki":
        print("Poistit kaikki reseptit reseptikirjasta")
        lista.clear()
    else:
        print("Et poistanut mitään")
    Enter()

def ViimeisinRuokalista(lista):
    ValmisteleSivu(a)
    if lista:
        print("Viimeisin ruokalistasi")
        TulostaNimi(lista)
        print()
        Enter()
    else:
        print("Ruokalistaa ei ole tehty!")
        print()
        Enter()

def TulostaNimi(lista):
    i = 0
    for obj in lista:
        i+=1
        print(i,"-", obj.nimi)

#PÄÄKOODI

#Määritetään reseptikirja ja ruokalista ReseptiKirja olioiksi, ja ladataan tiedostot
reseptiKirja= ReseptiKirja("reseptikirja")
ruokaLista = ReseptiKirja("ruokalista")

#Käyttöliittymän pohja
while True:
    print('\n'*40)
    print("Reseptikirjasi")
    print()
    print("Valitse toiminto")
    print()
    print("1- Lisää resepti kirjaan")
    print("2- Poista resepti kirjasta")
    print("3- Katso reseptiä")
    print("4- Luo viikon ruokalista")
    print("5- Katso viimeisintä ruokalistaa")
    print("6- Lopeta")
    print
    a = int(input("Valitse vaihtoehto numerolla: "))

    if a == 1: 
        ValmisteleSivu(a)
        luotunimi = input("Anna ruoannimi, jätä tyhjäksi palataksesi: ")
        if luotunimi == "":
            continue
        else:
            print("Syötä raaka-aineet yksi kerrallaan. Lopettaaksesi paina enter tyhjällä rivillä")
            luotuRaakaAine = MoniRivi()
            print("Syötä ohje yksi rivi kerrallaan. Lopettaaksesi paina enter tyhjällä rivillä")
            luotuOhje = MoniRivi()
            reseptiKirja.LuoUusiRuoka(luotunimi,luotuRaakaAine,luotuOhje)
            reseptiKirja.TalletaLista(reseptiKirja.tiedosto)
        Enter()
    elif a == 2: #Poista resepti
        ValmisteleSivu(a)
        TulostaNimi(reseptiKirja.lista)
        print("Kaikki")
        etsiPoisto = input("Valitse reseptin numero tai toiminto, jätä tyhjäksi palataksesi ")
        toiminto = PoistaToiminto(etsiPoisto, reseptiKirja.lista)
        varmistus = input("Oletko aivan varma (k) tai (e): ")
        PoistaVarmistus(reseptiKirja.lista,toiminto,etsiPoisto,varmistus)
        reseptiKirja.TalletaLista(reseptiKirja.tiedosto)

    elif a == 3: #Katso reseptiä
        ValmisteleSivu(a)
        if reseptiKirja.lista:
            TulostaNimi(reseptiKirja.lista)
            etsi = input("Valitse reseptin numero mitä katsella, jätä tyhjäksi palataksesi: ")
            if etsi.isnumeric():
                resepti = reseptiKirja.TulostaResepti(etsi)
                etsi = input("Paina enter palataksesi, halutessasi muokata reseptiä, kirjoita muokkaa: ")
                if etsi.lower() == "muokkaa":
                    print('\n'*40)
                    print("Mitä haluat muokata?")
                    print("1- Nimi")
                    print("2- Raaka-aineita")
                    print("3- Valmistusohjetta")
                    etsi = (int(input("Valitse muokattavan asian numero: ")))
                    print('\n'*40)
                    if etsi == 1:
                        print("Ruoan vanha nimi oli: " ,reseptiKirja.lista[resepti].nimi)
                        print()
                        reseptiKirja.MuokkaaListanOlioNimi(resepti, input("Anna uusi nimi: "))
                    elif etsi == 2:
                        print("Ruoan vanhat raaka-aineet olivat: ", reseptiKirja.lista[resepti].raakaAineet)
                        print()
                        print("Syötä uudet raaka-aineet yksi kerrallaan. Lopettaaksesi paina enter tyhjällä rivillä")
                        reseptiKirja.MuokkaaListanOlioAine(resepti, MoniRivi())
                    elif etsi == 3:
                        print("Ruoan vanha valmistusohje oli: ", reseptiKirja.lista[resepti].ohje)
                        print()
                        print("Syötä uusi ohje yksi rivi kerrallaan. Lopettaaksesi paina enter tyhjällä rivillä")
                        reseptiKirja.MuokkaaListanOlioOhje(resepti, MoniRivi())
                    reseptiKirja.TalletaLista(reseptiKirja.tiedosto)
                    Enter()
        else:
            print("Reseptikirjassasi ei ole vielä yhtään reseptiä!")
            Enter()            
    elif a == 4: #Luo ruokalista
        ValmisteleSivu(a)
        print("Reseptikirjassasi on ",len(reseptiKirja.lista), " ruokaa")
        ruokienMaara= input("Montako ruokaa haluaisit listaasi? Jätä tyhjäksi palataksesi: ")
        ruokaLista.LuoRuokaLista(reseptiKirja.lista, ruokienMaara)
        ruokaLista.TalletaLista(ruokaLista.tiedosto)
        TulostaNimi(ruokaLista.lista)
        Enter()
    elif a == 5: #Viimeisin ruokalista                                                              #LUO OMINAISUUS TULOSTAA RESEPTI
        ValmisteleSivu(a)                                                                           #MINKÄ JÄLKEEN PALATA TAKAISIN LISTAAN
        if ruokaLista.lista:
            print("Viimeisin ruokalistasi:")
            TulostaNimi(ruokaLista.lista)
        else:
            print("Ruokalistaa ei ole tehty!")
            print()
        Enter()
    elif a == 6:
        break
    
