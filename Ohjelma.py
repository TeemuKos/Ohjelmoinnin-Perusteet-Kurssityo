from luokka import ReseptiKirja

def ValmisteleSivu(valinta):
    print('\n'*40)
    if valinta == 1:
        print("Luodaan uusi resepti")
    elif valinta == 2:
        print("Minkä reseptin haluat poistaa?")
    elif valinta == 3:
        print("Kaikki reseptisi")
    elif valinta == 4:
        print("Mitä reseptiä haluaisit muokata?")
    elif valinta == 5:
        print("Luodaan uusi ruokalista!")
    else:
        None
    print()

def Enter():
    print()
    input("Paina enter jatkaaksesi")

def MoniRivi():                                                                                 
    sana = ""
    print()
    print("Syötä rivi kerrallaan, lopeta painamalla enter tyhjällä rivillä")
    while True:
        arvo = input()
        if arvo == "" and sana != "":                  
            break
        elif arvo == "" and sana == "":
            print("Yksi rivi vaaditaan!")
            continue
        elif arvo != "" and sana == "":
            sana += '\n' + "-" +arvo.capitalize()
        else:
            sana += '\n' + "-" +arvo
    print('\n'*40)
    return sana

def TulostaNimi(lista):
    for x in range(len(lista)):
        print(x+1,"-" + lista[x].nimi)

#PÄÄKOODI
#Määritetään reseptikirja ja ruokalista ReseptiKirja olioiksi, ja ladataan tiedostot
reseptiKirja = ReseptiKirja("reseptikirja")
ruokaLista = ReseptiKirja("ruokalista")

while True:
    print('\n'*40)
    print("Reseptikirjasi")
    print()
    print("Valitse toiminto")
    print()
    print("1- Lisää resepti kirjaan")
    print("2- Poista resepti kirjasta")
    print("3- Katso reseptiä")
    print("4- Muokkaa reseptiä")
    print("5- Luo viikon ruokalista")
    print("6- Katso viimeisintä ruokalistaa")
    print("7- Lopeta")
    print
    a = int(input("Valitse vaihtoehto numerolla: "))
    if a == 1: 
        ValmisteleSivu(a)
        luotunimi = input("Anna ruoannimi, jätä tyhjäksi palataksesi: ")
        if luotunimi == "":
            continue
        else:
            print('\n'*40)
            luotuRaakaAine = MoniRivi()
            luotuOhje = MoniRivi()
            reseptiKirja.LuoUusiRuoka(luotunimi,luotuRaakaAine,luotuOhje)
            reseptiKirja.TalletaLista(reseptiKirja.tiedosto)
        Enter()
    elif a == 2: #Poista resepti
        ValmisteleSivu(a)
        TulostaNimi(reseptiKirja.lista)
        print("-Kaikki")
        etsiPoistettava = input("Valitse reseptin numero tai toiminto, jätä tyhjäksi palataksesi ")
        toiminto = reseptiKirja.PoistaToiminto(etsiPoistettava)
        varmistus = input("Oletko aivan varma (k) tai (e): ")
        reseptiKirja.PoistaVarmistus(toiminto,etsiPoistettava,varmistus)
        reseptiKirja.TalletaLista(reseptiKirja.tiedosto)
        Enter()
    elif a == 3: #Katso reseptiä
        while True:
            ValmisteleSivu(a)
            if reseptiKirja.lista:
                TulostaNimi(reseptiKirja.lista)
                etsi = input("Valitse reseptin numero mitä katsella, jätä tyhjäksi palataksesi: ")
                if etsi.isnumeric():
                    resepti = reseptiKirja.TulostaResepti(etsi)
                    poistu = input("Haluatko katsoa toista reseptiä? [K tai E]: ")
                    if poistu == "k":
                        continue
                    else:
                        break
                else:
                    break           
            else:
                print("Reseptikirjassasi ei ole vielä yhtään reseptiä!")
                Enter()
    elif a == 4: #Muokkaa reseptiä
        ValmisteleSivu(a)
        if reseptiKirja.lista:
            TulostaNimi(reseptiKirja.lista)
            etsiIndeksi = input("Paina enter palataksesi, valitse reseptin numero muokataksesi: ")
            if etsiIndeksi.isnumeric():
                indeksi = int(etsiIndeksi) -1
                print('\n'*40)
                print("Mitä haluat muokata?")
                print("1- Nimi")
                print("2- Raaka-aineita")
                print("3- Valmistusohjetta")
                etsi = (int(input("Valitse muokattavan asian numero: ")))
                print('\n'*40)
                reseptiKirjanOlio = reseptiKirja.lista[indeksi]
                if etsi == 1:
                    print("Ruoan vanha nimi oli: " ,reseptiKirjanOlio.nimi)
                    print()
                    reseptiKirja.MuokkaaListanOlioNimi(indeksi, input("Anna uusi nimi: "))
                elif etsi == 2:
                    print("Ruoan vanhat raaka-aineet olivat: ", reseptiKirjanOlio.raakaAineet)
                    reseptiKirja.MuokkaaListanOlioAine(indeksi, MoniRivi())
                elif etsi == 3:
                    print("Ruoan vanha valmistusohje oli: ", reseptiKirjanOlio.ohje)
                    reseptiKirja.MuokkaaListanOlioOhje(indeksi, MoniRivi())
                reseptiKirja.TalletaLista(reseptiKirja.tiedosto)
                Enter()
        else:
            print("Reseptikirjassasi ei ole vielä yhtään reseptiä!")
            Enter()
    elif a == 5: #Luo ruokalista
        ValmisteleSivu(a)
        print("Reseptikirjassasi on ",len(reseptiKirja.lista), " ruokaa")
        ruokienMaara= input("Montako ruokaa haluaisit listaasi? Jätä tyhjäksi palataksesi: ")
        ruokaLista.LuoRuokaLista(reseptiKirja.lista, ruokienMaara)
        ruokaLista.TalletaLista(ruokaLista.tiedosto)
        TulostaNimi(ruokaLista.lista)
        Enter()
    elif a == 6: #Viimeisin ruokalista 
        while True:                                                             
            ValmisteleSivu(a)                                                                           
            if ruokaLista.lista:
                print("Viimeisin ruokalistasi:")
                TulostaNimi(ruokaLista.lista)
                katsele = input("Halutessasi lukea reseptin, valitse sen numero, muutoin paina enter tyhjällä rivillä jatkaaksesi: ")
                if katsele.isnumeric():
                    ruokaLista.TulostaResepti(katsele)
                else:
                    continue
                poistu = input("Haluatko katsoa toista reseptiä? [K tai E]: ")
                if poistu == "k":
                    continue
                else:
                    break
            else:
                print("Ruokalistaa ei ole tehty!")
                print()
                Enter()
    elif a == 7:
        break
