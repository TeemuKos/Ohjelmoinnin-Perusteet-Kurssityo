class ruoka:
    def __init__(self,nimi,raakaAineet,ohje):
        self.nimi=nimi
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
