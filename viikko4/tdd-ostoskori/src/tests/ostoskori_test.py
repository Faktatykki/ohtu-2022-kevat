import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)


    def test_yhden_tuotteen_lisaamisen_jalkeen_ostoskorin_hinta_sama_kuin_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)


    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_2_tavaraa(self):
        maito = Tuote("Maito", 3)
        koiranruoka = Tuote("Koiranruoka", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(koiranruoka)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_kahden_eri_tuotetta_ostoskorin_hinta_sama_kuin_tuotteiden_hintojen_summa(self):
        maito = Tuote("Maito", 3)
        koiranruoka = Tuote("Koiranruoka", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(koiranruoka)

        tuotteiden_yhteissumma = maito.hinta() + koiranruoka.hinta()

        self.assertEqual(self.kori.hinta(), tuotteiden_yhteissumma)


    def test_kahden_saman_tuotteen_jalkeen_ostoskorissa_2_tavaraa(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_jalkeen_hinta_sama_kuin_2_kertaa_hinta(self):
        hinta = 3
        
        maito = Tuote("Maito", hinta)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), hinta * 2)

    def test_yhden_tuotteen_lisaamisen_jalkeen_yksi_ostos(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()
        
        self.assertEqual(len(ostokset), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")
        self.assertEqual(ostos.lukumaara(), 1)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_ostoskorissa_kaksi_ostosta(self):
        maito = Tuote("Maito", 3)
        koiranruoka = Tuote("Koiranruoka", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(koiranruoka)

        self.assertEqual(len(self.kori.ostokset()), 2)

    def test_kahden_saman_tuotteen_lisaaminen_ostoskorissa_yksi_ostos(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(len(self.kori.ostokset()), 1)
