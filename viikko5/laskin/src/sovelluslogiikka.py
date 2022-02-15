class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = None

    def miinus(self, arvo):
        self.edellinen = self.tulos
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.edellinen = self.tulos
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.edellinen = self.tulos
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.edellinen = self.tulos
        self.tulos = arvo

    def edellinen_arvo(self):
        self.tulos = self.edellinen