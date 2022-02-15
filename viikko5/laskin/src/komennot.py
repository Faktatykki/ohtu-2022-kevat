class Summa:
    def __init__(self, sovellus, lukija):
        self.sovellus = sovellus
        self.lukija = lukija
    
    def suorita(self):
        arvo = int(self.lukija())
        self.sovellus.plus(arvo)


class Erotus:
    def __init__(self, sovellus, lukija):
        self.sovellus = sovellus
        self.lukija = lukija

    def suorita(self):
        arvo = int(self.lukija())
        self.sovellus.miinus(arvo)


class Nollaus:
    def __init__(self, sovellus, lukija):
        self.sovellus = sovellus
        self.lukija = lukija

    def suorita(self):
        self.sovellus.nollaa()


class Kumoa:
    def __init__(self, sovellus, lukija):
        self.sovellus = sovellus
        self.lukija = lukija

    def suorita(self):
        self.sovellus.edellinen_arvo()
    
    
