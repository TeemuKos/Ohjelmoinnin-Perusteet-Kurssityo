import pickle
from random import randrange
from luokka import ruoka
import os

def LuoUusi(lista ,listanTiedosto):
    print('\n'*40)
    print("Luodaan uusi resepti")
    print()
    luoNimi = input("Anna ruoannimi, jätä tyhjäksi palataksesi: ")
    if luoNimi == "":
        return
    print('\n'*40)
    luoAine=""
    print("Kirjoita raaka-aineet rivi kerrallaan. Kirjoitettuasi rivin paina enter. \nKun haluat lopettaa raaka-aineiden kirjoittamisen, paina enter tyhjällä rivillä")
    while True:
        uusiRiviAine = input("Anna raaka-aine: ")
        if uusiRiviAine == "":
            break
        else:
            luoAine += '\n' + "-" +uusiRiviAine
    print('\n'*40)
    luoOhje = ""
    print("Kirjoita ohje rivi kerrallaan. Kirjoitettuasi rivin paina enter. \nKun haluat lopettaa ohjeen kirjoittamisen, paina enter tyhjällä rivillä")
    while True:
        uusiRiviOhje = input("Anna ohjeen rivi: ")
        if uusiRiviOhje == "":
            break
        else:
            luoOhje += '\n' + uusiRiviOhje +','
    print('\n'*40)
    lista.append(ruoka(luoNimi,luoAine,luoOhje))
    print("Uusi resepti ",lista[-1].nimi, " tallennettu reseptikirjaan")
    TalletaLista(listanTiedosto, lista)
    input("Paina enter jatkaaksesi")


def PoistaRuokalistasta(lista, listanTiedosto):
    print('\n'*40)
    print("Minkä reseptin haluat poistaa?")
    TulostaNimi(lista)
    print("Kaikki")
    print("Poistu")
    etsi = input("Valitse reseptin numero tai toiminto, jätä tyhjäksi palataksesi ")
    if etsi.isnumeric() == True:
        haettuResepti= int(etsi) - 1
        print()
        print("Olet poistamassa reseptiä: ", lista[haettuResepti].nimi)
        print("Oletko aivan varma (k) tai (e)")
        poistoVarmistus = input()
        if poistoVarmistus == "k":
            print("Poistit reseptin: ",lista[haettuResepti].nimi, " reseptikirjasta")
            del lista[haettuResepti]
            TalletaLista(listanTiedosto, lista)
            input("Paina enter jatkaaksesi")
        else:
            print("Et poistanut mitään")
            input("Paina enter jatkaaksesi")
    elif etsi.lower() == "kaikki":
        print()
        print("Olet poistamassa kaikki reseptit")
        print("Oletko aivan varma (k) tai (e)")
        poistoVarmistus = input()
        if poistoVarmistus == "k":
            print("Poistit kaikki reseptit reseptikirjasta")
            ruokaKirja.clear()
            TalletaLista(listanTiedosto, lista)
            input("Paina enter jatkaaksesi")
        else:
            print("Et poistanut mitään")
            input("Paina enter jatkaaksesi")
    else:
        return


def KatsoReseptiä(lista):
    print('\n'*40)
    if lista:
        print("Kaikki reseptisi")
        TulostaNimi(lista)
        etsi = input("Valitse reseptin numero mitä katsella, jätä tyhjäksi palataksesi: ")
        if etsi.isnumeric():
            haettuResepti= int(etsi) - 1
            print('\n'*40)
            print("Ruoan nimi: ",lista[haettuResepti].nimi)
            print()
            print("Tarvittavat raaka-aineet",lista[haettuResepti].raakaAineet)
            print()
            print("Valmistusohje: ",lista[haettuResepti].ohje)
            print()
            print("Paina enter palataksesi, halutessasi muokata reseptiä, kirjoita muokkaa: ")
            katseleToiminto = input()
            if katseleToiminto == "":
                return
            elif katseleToiminto.lower() == "muokkaa":
                print('\n'*40)
                print("Mitä haluat muokata?")
                print("1- Nimi")
                print("2- Raaka-aineita")
                print("3- Valmistusohjetta")
                muokkausValinta = (int(input("Valitse muokattavan asian numero: ")))
                if muokkausValinta == 1:
                    print('\n'*40)
                    print("Ruoan vanha nimi oli: ", lista[haettuResepti].nimi)
                    print()
                    lista[haettuResepti].MuokkaaNimi(input("Mikä on reseptin uusi nimi? "))
                    print("Ruoan uusi nimi on: ", lista[haettuResepti].nimi)
                    input("Paina enter jatkaaksesi")
                elif muokkausValinta == 2:
                    print('\n'*40)
                    print("Ruoan vanhat raaka-aineet olivat: ", lista[haettuResepti].raakaAineet)
                    print()
                    lista[haettuResepti].MuokkaaAine(input("Mikä on reseptin uudet raaka-aineet? "))
                    print("Ruoan uudet raaka-aineet: ", lista[haettuResepti].raakaAineet)
                    input("Paina enter jatkaaksesi")
                elif muokkausValinta == 3:
                    print('\n'*40)
                    print("Ruoan vanha valmistusohje oli: ", lista[haettuResepti].ohje)
                    lista[haettuResepti].MuokkaaOhje(input("Mikä on reseptin uusi ohje? "))
                    print("Ruoan uusi valmistusohje on: ", lista[haettuResepti].ohje)
                    input("Paina enter jatkaaksesi")
        else:
            return
    else:
        print("Reseptikirjassasi ei ole vielä yhtään reseptiä!")
        input("Paina enter jatkaaksesi")


def LuoRuokalista(listasta, luotavaLista, luotavaListaTiedosto):
    print('\n'*40)
    print("Luodaan uusi ruokalista!")
    print()
    while True:
        print("Reseptikirjassasi on ",len(listasta), " ruokaa")
        ruokienMaara= input("Montako ruokaa haluaisit listaasi? Jätä tyhjäksi palataksesi: ")
        if ruokienMaara.isnumeric():
            ruokienMaara = int(ruokienMaara)
            luotavaLista.clear()
            if ruokienMaara == 0:
                print("Et lisännyt yhtään ruokaa ruokalistaasi!")
                input("Paina enter jatkaaksesi")
                break
            elif ruokienMaara <= len(listasta):
                for i in range(ruokienMaara):
                    arvottuRuoka = randrange(0,len(listasta))
                    arvotunRuuanobj = listasta[arvottuRuoka]
                    while arvotunRuuanobj in ruokaLista:
                        arvottuRuoka = randrange(0,len(listasta))
                        arvotunRuuanobj = listasta[arvottuRuoka]
                    luotavaLista.append(listasta[arvottuRuoka])
                TalletaLista(luotavaListaTiedosto,luotavaLista)
                print("Uusi ruokalistasi: ")
                TulostaNimi(luotavaLista)
                input("Paina enter jatkaaksesi")
                break
            else:
                print("Reseptikirjassasi ei ole riittävän monta ruokaa!")
                input("Paina enter jatkaaksesi")
                continue
        else:
            return


def ViimeisinRuokalista(lista):
    print('\n'*40)
    if lista:
        print("Viimeisin ruokalistasi")
        TulostaNimi(lista)
        print()
        input("Paina enter jatkaaksesi")
    else:
        print("Ruokalistaa ei ole tehty!")
        print()
        input("Paina enter jatkaaksesi")

def TulostaNimi(lista):
    i = 0
    for obj in lista:
        i+=1
        print(i,"-", obj.nimi)

def TalletaLista(talletaTiedosto,lista):
    avattuTiedosto = open(talletaTiedosto, "wb")
    pickle.dump(lista, avattuTiedosto)
    avattuTiedosto.close()


def LataaLista(lataaTiedosto):
    avattuTiedosto = open(lataaTiedosto, "rb")
    ladattuRuokaKirja = pickle.load(avattuTiedosto)
    avattuTiedosto.close()
    return ladattuRuokaKirja

#PÄÄKOODI

#Haetaan reseptikirjan ja ruokalistan tiedostot muistiin
ruokaKirjaTiedosto = os.path.join(os.path.dirname(__file__), "kirjatiedosto.pkl")
ruokaListaTiedosto = os.path.join(os.path.dirname(__file__), "listatiedosto.pkl")

ruokaKirja= []
ruokaLista= []

#Määritetään reseptikirja ja ruokalista listat tiedostojensa arvoihin
ruokaKirja = LataaLista(ruokaKirjaTiedosto)
ruokaLista = LataaLista(ruokaListaTiedosto)

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
    a = int(input("Valitse vaihtoehto numerolla: "))

    if a == 1: 
        LuoUusi(ruokaKirja,ruokaKirjaTiedosto)
    elif a == 2: #Poista resepti
        PoistaRuokalistasta(ruokaKirja, ruokaKirjaTiedosto)
    elif a == 3: #Katso reseptiä
        KatsoReseptiä(ruokaKirja)
    elif a == 4: #Luo ruokalista
        LuoRuokalista(ruokaKirja,ruokaLista,ruokaListaTiedosto)
    elif a == 5: #Viimeisin ruokalista
        ViimeisinRuokalista(ruokaLista)
    elif a == 6:
        break
    
