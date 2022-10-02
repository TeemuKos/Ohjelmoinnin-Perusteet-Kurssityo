import pickle
import os
from random import randrange
class ruoka:
    def __init__(self,nimi,raakaAineet,ohje):
        self.nimi=nimi.capitalize()
        self.raakaAineet=raakaAineet
        self.ohje=ohje
    def MuokkaaNimi(self, muokattuNimi):
        self.nimi = muokattuNimi
    def MuokkaaAine(self, muokattuaAine):
        self.raakaAineet = muokattuaAine
    def MuokkaaOhje(self, muokattuOhje):
        self.ohje = muokattuOhje
        
    def __str__(self,):
        return f"Ruoan nimi: {self.nimi}, Tarvittavat raaka-aineet: {self.raakaAineet}, Valmistusohje: {self.ohje}"

class ReseptiKirja:
    def __init__(self,nimi):
        self.nimi = nimi
        self.lista = []
        self.tiedostonNimi = self.nimi + ".pkl"
        self.tiedosto = os.path.join(os.path.dirname(__file__), self.tiedostonNimi)
        self.LataaLista(self.tiedosto)

    def TalletaLista(self, talletaTiedosto):
            avattuTiedosto = open(talletaTiedosto, "wb")
            pickle.dump(self.lista, avattuTiedosto)
            avattuTiedosto.close()


    def LataaLista(self, lataaTiedosto):
        try:
            avattuTiedosto = open(lataaTiedosto, "rb")
            self.lista = pickle.load(avattuTiedosto)
            avattuTiedosto.close()
        except IOError:
            pass

    def LuoUusiRuoka(self, nimi, aine, ohje):
        self.lista.append(ruoka(nimi,aine,ohje))
        print("Uusi resepti ",self.lista[-1].nimi, " tallennettu reseptikirjaan")
    
    def LuoRuokaLista(self, listasta, maara):
        if maara.isnumeric():
            maara = int(maara)
            self.lista.clear()
            if maara == 0:
                print("Et lisännyt yhtään ruokaa ruokalistaasi!")
            elif maara <= len(listasta):
                for i in range(maara):
                    arvottuRuoka = randrange(0,len(listasta))
                    arvotunRuuanobj = listasta[arvottuRuoka]
                    while arvotunRuuanobj in self.lista:
                        arvottuRuoka = randrange(0,len(listasta))
                        arvotunRuuanobj = listasta[arvottuRuoka]
                    self.lista.append(listasta[arvottuRuoka])
                print("Uusi ruokalistasi: ")
            else:
                print("Reseptikirjassasi ei ole riittävän monta ruokaa!")
        else:
            return    
    def MuokkaaListanOlioNimi(self, olionIndeksi,uusiNimi):
        print('\n'*40)
        self.lista[olionIndeksi].MuokkaaNimi(uusiNimi)
        print("Ruoan uusi nimi on: ", self.lista[olionIndeksi].nimi)

    def MuokkaaListanOlioAine(self, olionIndeksi,uusiAine):
        print('\n'*40)
        self.lista[olionIndeksi].MuokkaaAine(uusiAine)
        print("Ruoan uudet raaka-aineet: ", self.lista[olionIndeksi].raakaAineet)

    def MuokkaaListanOlioOhje(self, olionIndeksi,uusiOhje):
        print('\n'*40)
        self.lista[olionIndeksi].MuokkaaOhje(uusiOhje)
        print("Ruoan uusi valmistusohje on: ", self.lista[olionIndeksi].ohje)

    def TulostaResepti(self,etsittyResepti):
        haettuResepti= int(etsittyResepti) - 1
        print('\n'*40)
        print("Ruoan nimi: ",self.lista[haettuResepti].nimi)
        print()
        print("Tarvittavat raaka-aineet",self.lista[haettuResepti].raakaAineet)
        print()
        print("Valmistusohje: ",self.lista[haettuResepti].ohje)
        print()
        return haettuResepti        
    def ViimeisinRuokalista(self):
        if self.lista == True:
            print("Viimeisin ruokalistasi")
            print()
            return 1
        else:
            print("Ruokalistaa ei ole tehty!")
            print()
            return 0

    def PoistaToiminto(self,valinta):
        print('\n'*40)
        listaIndeksi = 0
        if valinta.isnumeric():
            listaIndeksi = int(valinta) - 1
            print()
            print("Olet poistamassa reseptiä: ", self.lista[listaIndeksi].nimi)

        elif valinta.lower() == "kaikki":
            print()
            print("Olet poistamassa kaikki reseptit")
        return listaIndeksi
    
    def PoistaVarmistus(self, indeksi, valinta,poistoVarmistus):                                       
        print('\n'*40)
        if poistoVarmistus == "k" and valinta.isnumeric():
            print("Poistit reseptin: ",self.lista[indeksi].nimi, " reseptikirjasta")
            del self.lista[indeksi]
        elif poistoVarmistus == "k" and valinta == "kaikki":
            print("Poistit kaikki reseptit reseptikirjasta")
            self.lista.clear()
        else:
            print("Et poistanut mitään")
