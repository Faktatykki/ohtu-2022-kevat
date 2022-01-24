import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        self.statistics = Statistics(PlayerReaderStub())

    def test_pelaaja_loytyy(self):
        self.assertEqual(self.statistics.search('Semenko').name, 'Semenko')

    def test_pelaaja_ei_loydy(self):
        self.assertEqual(self.statistics.search('Pena'), None)

    def test_kaikki_joukkueesta_loytyy(self):
        self.assertEqual(len(self.statistics.team('EDM')), 3)

    def test_paras_pelaaja_loytyy(self):
        top_player = self.statistics.top_scorers(3)[0]
        self.assertEqual(str(top_player), str(Player("Gretzky", "EDM", 35, 89)))