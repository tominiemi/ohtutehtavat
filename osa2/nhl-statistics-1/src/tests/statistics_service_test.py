import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_palauttaa_oikeat_pelaajat(self):
        """Testaa, että pelaajan haku palauttaa oikean pelaajan tiedot."""
        self.assertEqual(
            str(self.stats.search("Semenko")),
            "Semenko EDM 4 + 12 = 16"
        )
        self.assertEqual(
            str(self.stats.search("Lemieux")),
            "Lemieux PIT 45 + 54 = 99"
        )
        self.assertEqual(
            str(self.stats.search("Kurri")),
            "Kurri EDM 37 + 53 = 90"
        )
        self.assertEqual(
            str(self.stats.search("Yzerman")),
            "Yzerman DET 42 + 56 = 98"
        )
        self.assertEqual(
            str(self.stats.search("Gretzky")),
            "Gretzky EDM 35 + 89 = 124"
        )

    def test_search_palauttaa_none_jos_pelaajaa_ei_loydy(self):
        """Testaa, että pelaajan haku palauttaa None, jos pelaajaa ei löydy."""
        self.assertEqual(
            self.stats.search("Selänne"),
            None
        )

    def test_team_palauttaa_oikeat_pelaajat(self):
        """Testaa, että joukkueen haku palauttaa oikeat pelaajat."""
        self.assertEqual(
            str(self.stats.team("EDM")[0]),
            "Semenko EDM 4 + 12 = 16"
        )
        self.assertEqual(
            str(self.stats.team("EDM")[1]),
            "Kurri EDM 37 + 53 = 90"
        )
        self.assertEqual(
            str(self.stats.team("EDM")[2]),
            "Gretzky EDM 35 + 89 = 124"
        )

    def test_top_palauttaa_oikeat_pelaajat(self):
        """Testaa, että top-pelaajien haku palauttaa oikeat pelaajat."""
        self.assertEqual(
            str(self.stats.top(1)[0]),
            "Gretzky EDM 35 + 89 = 124"
        )
        self.assertEqual(
            str(self.stats.top(2)[0]),
            "Gretzky EDM 35 + 89 = 124"
        )
        self.assertEqual(
            str(self.stats.top(2)[1]),
            "Lemieux PIT 45 + 54 = 99"
        )
