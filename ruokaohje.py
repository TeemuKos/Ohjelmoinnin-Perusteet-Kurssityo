import pickle
from random import randrange
from traceback import print_tb
from luokka import ruoka
import os

def LuoUusi():
    luoNimi = input("Anna ruoannimi: ")
    luoAine=""
    print("Kirjoita raaka-aineet rivi kerrallaan. Kirjoitettuasi rivin paina enter. \nKun haluat lopettaa raaka-aineiden kirjoittamisen, paina enter tyhjällä rivillä")
    while True:
        uusiRiviAine = input("Anna raaka-aine: ")
        if uusiRiviAine == "":
            break
        else:
            luoAine += '\n' + "-" +uusiRiviAine
    luoOhje = ""
    print("Kirjoita ohje rivi kerrallaan. Kirjoitettuasi rivin paina enter. \nKun haluat lopettaa ohjeen kirjoittamisen, paina enter tyhjällä rivillä")
    while True:
        uusiRiviOhje = input("Anna ohjeen rivi: ")
        if uusiRiviOhje == "":
            break
        else:
            luoOhje += ',' + '\n' + uusiRiviOhje
    return ruokaKirja.append(ruoka(luoNimi,luoAine,luoOhje))

tiedosto = "listatiedosto.pkl"
tiedostoSijainti = os.path.join(os.path.dirname(__file__), tiedosto)
ruokaKirja= []
ruokaLista= []
i=0

print("Reseptikirjasi")
while True:
    print('\n'*40)
    print("Valitse toiminto")
    print()
    print("1- Lisää resepti kirjaan")
    print("2- Poista resepti kirjasta")
    print("3- Katso reseptiä")
    print("4- Luo viikon ruokalista")
    print("5- Katso viimeisintä ruokalistaa")
    print("6- Lopeta")
    print("7- Tallenna lista")
    print("8- Lue vanha lista")
    a = int(input("Valitse vaihtoehto numerolla: "))

    if a == 1: #Luo resepti
        print('\n'*40)
        print("Luodaan uusi resepti")
        print()
        LuoUusi()
        print()
        print("Loit uuden reseptin nimellä: ",ruokaKirja[-1].nimi)
        input("Paina enter jatkaaksesi")
    elif a == 2: #Poista resepti
        print('\n'*40)
        print("Minkä reseptin haluat poistaa?")
        for obj in ruokaKirja:
            i+=1
            print(i,"-", obj.nimi)
        etsi = int(input("Valitse reseptin numero minkä haluat poistaa "))
        haettuResepti= etsi - 1
        print()
        print("Olet poistamassa reseptiä: ", ruokaKirja[haettuResepti].nimi)
        print("Oletko aivan varma (k) tai (e)")
        poistoVarmistus = input()
        if poistoVarmistus == "k":
            print("Poistit reseptin: ",ruokaKirja[haettuResepti].nimi)
            del ruokaKirja[haettuResepti]
            input("Paina enter jatkaaksesi")
        else:
            print("Et poistanut mitään")
            input("Paina enter jatkaaksesi")
    elif a == 3: #Katso reseptiä
        print('\n'*40)
        if ruokaKirja:
            print("Kaikki reseptisi")
            for obj in ruokaKirja:
                i+=1
                print(i,"-", obj.nimi)
            etsi = int(input("Valitse reseptin numero mitä katsella "))
            haettuResepti= etsi - 1
            print('\n'*40)
            print("Ruoan nimi: ",ruokaKirja[haettuResepti].nimi)
            print()
            print("Tarvittavat raaka-aineet",ruokaKirja[haettuResepti].raakaAineet)
            print()
            print("Valmistusohje: ",ruokaKirja[haettuResepti].ohje)
            print()
            print("Paina enter palataksesi, halutessasi muokata reseptiä, kirjoita muokkaa")
            katseleToiminto = input()
            if katseleToiminto == "":
                continue
            elif katseleToiminto == "muokkaa" or katseleToiminto == "Muokkaa":
                print('\n'*40)
                print("Mitä haluat muokata?")
                print("1- Nimi")
                print("2- Raaka-aineita")
                print("3- Valmistusohjetta")
                muokkausValinta = (int(input("Valitse muokattavan asian numero: ")))
                if muokkausValinta == 1:
                    print('\n'*40)
                    print("Ruoan vanha nimi oli: ", ruokaKirja[haettuResepti].nimi)
                    print()
                    ruokaKirja[haettuResepti].MuokkaaNimi(input("Mikä on reseptin uusi nimi? "))
                    print("Ruoan uusi nimi on: ", ruokaKirja[haettuResepti].nimi)
                    input("Paina enter jatkaaksesi")
                elif muokkausValinta == 2:
                    print('\n'*40)
                    print("Ruoan vanhat raaka-aineet olivat: ", ruokaKirja[haettuResepti].raakaAineet)
                    print()
                    ruokaKirja[haettuResepti].MuokkaaAine(input("Mikä on reseptin uudet raaka-aineet? "))
                    print("Ruoan uudet raaka-aineet: ", ruokaKirja[haettuResepti].raakaAineet)
                    input("Paina enter jatkaaksesi")
                elif muokkausValinta == 3:
                    print('\n'*40)
                    print("Ruoan vanha valmistusohje oli: ", ruokaKirja[haettuResepti].ohje)
                    ruokaKirja[haettuResepti].MuokkaaOhje(input("Mikä on reseptin uusi ohje? "))
                    print("Ruoan uusi valmistusohje on: ", ruokaKirja[haettuResepti].ohje)
                    input("Paina enter jatkaaksesi")
            i=0
        else:
            print("Reseptikirjassasi ei ole vielä yhtään reseptiä!")
            input("Paina enter jatkaaksesi")
    elif a == 4: #Luo ruokalista
        print('\n'*40)
        print("Luodaan uusi ruokalista!")
        print()
        while True:
            print("Reseptikirjassasi on ",len(ruokaKirja), " ruokaa")
            ruokienMaara= int(input("Montako ruokaa haluaisit listaasi? "))
            ruokaLista.clear()
            if ruokienMaara <= len(ruokaKirja):
                for i in range(ruokienMaara):
                    arvottuRuoka = randrange(0,len(ruokaKirja))             #
                    while arvottuRuoka in ruokaLista:                       # KORJAA TARKASTAMAAN ETTEI RUOKAA OLE JO LISTASSA
                        arvottuRuoka = randrange(0,len(ruokaKirja))         #
                    ruokaLista.append(ruokaKirja[arvottuRuoka])             #
                print("Uusi ruokalistasi: ")
                i=0
                for obj in ruokaLista:
                    i+=1
                    print(i,"-", obj.nimi)
                input("Paina enter jatkaaksesi")
                break
            elif ruokienMaara == 0:
                print("Et lisännyt yhtään ruokaa ruokalistaasi!")
                input("Paina enter jatkaaksesi")
                break
            else:
                print("Reseptikirjassasi ei ole riittävän monta ruokaa!")
                input("Paina enter jatkaaksesi")
                continue
    elif a == 5: #Viimeisin ruokalista
        print('\n'*40)
        if ruokaLista:
            i=0
            print("Viimeisin ruokalistasi")
            for obj in ruokaLista:
                i+=1
                print(i,"-", obj.nimi)
            print()
            input("Paina enter jatkaaksesi")
        else:
            print("Ruokalistaa ei ole tehty!")
            print()
            input("Paina enter jatkaaksesi")
    elif a == 6:
        break
    elif a == 7:
        #PICKLE
        open_file = open(tiedostoSijainti, "wb")
        pickle.dump(ruokaKirja, open_file)
        open_file.close()
    elif a == 8:
        open_file = open(tiedostoSijainti, "rb")
        ruokaKirja = pickle.load(open_file)
        open_file.close()
    
