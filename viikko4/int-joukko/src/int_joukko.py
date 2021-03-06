KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None or not self.tarkista_parametri(kapasiteetti):
            self.kapasiteetti = KAPASITEETTI
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None or not self.tarkista_parametri(kasvatuskoko):
            self.kasvatuskoko = OLETUSKASVATUS
        else:
            self.kasvatuskoko = kasvatuskoko

        self.ljono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0


    def kuuluu(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                return True

        return False


    def lisaa(self, n):
        if not self.kuuluu(n):
            self.ljono[self.alkioiden_lkm] = n
            self.alkioiden_lkm = self.alkioiden_lkm + 1

            if self.alkioiden_lkm % len(self.ljono) == 0:
                self.kasvata_taulukkoa()

            return True

        return False


    def poista(self, n):
        for i in range(0, self.alkioiden_lkm):
            if n == self.ljono[i]:
                self.pienenna_taulukkoa(i)
                return True

        return False


    def kasvata_taulukkoa(self):
        uusi_taulukko = [0] * (self.alkioiden_lkm + self.kasvatuskoko)
        self.kopioi_taulukko(self.ljono, uusi_taulukko)
        self.ljono = uusi_taulukko


    def pienenna_taulukkoa(self, poistettavan_indeksi):
        for j in range(poistettavan_indeksi, self.alkioiden_lkm - 1):
            temp = self.ljono[j]
            self.ljono[j] = self.ljono[j + 1]
            self.ljono[j + 1] = temp

        self.alkioiden_lkm = self.alkioiden_lkm - 1


    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]


    def mahtavuus(self):
        return self.alkioiden_lkm


    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.ljono[i]

        return taulu


    @staticmethod
    def tarkista_parametri(parametri):
        if not isinstance(parametri, int) or parametri < 0:
            return False
        
        return True

    @staticmethod
    def yhdiste(a, b):
        x = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            x.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            x.lisaa(b_taulu[i])

        return x


    @staticmethod
    def leikkaus(a, b):
        y = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    y.lisaa(b_taulu[j])

        return y


    @staticmethod
    def erotus(a, b):
        z = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            z.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            z.poista(b_taulu[i])

        return z


    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.ljono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.ljono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.ljono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
