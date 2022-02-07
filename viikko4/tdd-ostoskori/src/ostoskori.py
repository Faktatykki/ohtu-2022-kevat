from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostoslista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if not self.ostoslista:
            return 0

        maara = 0

        for ostos in self.ostoslista:
            maara += ostos.lukumaara

        return maara
       
    def hinta(self):
        if not self.ostoslista:
            return 0

        hinta = 0

        for ostos in self.ostoslista:
            hinta += ostos.hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        pass

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on