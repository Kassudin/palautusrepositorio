from contextlib import AbstractContextManager
from typing import Any
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
    def test_search_player(self):
        player = self.stats.search("Semenko")

        self.assertAlmostEqual(player.name, "Semenko")

    def test_search_player_not_found(self):
        player = self.stats.search("UnknownPlayer")
        self.assertIsNone(player)

    def test_team_players(self):
        team_players = self.stats.team("PIT")

        self.assertAlmostEqual(team_players[0].name, "Lemieux")

    def test_top_scorers(self):
        top_players = self.stats.top(2)
        self.assertAlmostEqual(top_players[0].name, "Gretzky")
        self.assertAlmostEqual(top_players[1].name, "Lemieux")
        self.assertAlmostEqual(top_players[2].name, "Yzerman")

#coverage run --branch -m pytest; coverage html