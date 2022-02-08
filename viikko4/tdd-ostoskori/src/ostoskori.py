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
            maara += ostos.lukumaara()

        return maara
       
    def hinta(self):
        if not self.ostoslista:
            return 0

        hinta = 0

        for ostos in self.ostoslista:
            hinta += ostos.hinta()

        return hinta

    def lisaa_tuote(self, lisattava: Tuote):
        for i, ostos in enumerate(self.ostoslista):
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                self.ostoslista[i] = ostos
                return


        self.ostoslista.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for i, ostos in enumerate(self.ostoslista):
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)

                self.ostoslista[i] = ostos
            if ostos.lukumaara() <= 0:
                del self.ostoslista[i]
        
    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.ostoslista