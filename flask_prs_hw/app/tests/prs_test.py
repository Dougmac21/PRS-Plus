import unittest

from app.models.player import Player
from app.models.prs import Prs


class PrsTest(unittest.TestCase):

    def setUp(self):
        pass


    def test_play_game_to_tie(self):
        self.player_1 = Player("Douglas", "Rock")
        self.player_2 = Player("Marko", "Rock")
        self.assertEqual("It's a tie!", Prs.play_game(self, self.player_1, self.player_2))

    def test_play_game_to_victory_player_1(self):
        self.player_1 = Player("Sally", "Paper")
        self.player_2 = Player("John", "Rock")
        self.assertEqual("Player 1 wins!", Prs.play_game(self, self.player_1, self.player_2))

    def test_play_game_to_victory_player_2(self):
        self.player_1 = Player("Cain", "Scissors")
        self.player_2 = Player("Abel", "Rock")
        self.assertEqual("Player 2 wins!", Prs.play_game(self, self.player_1, self.player_2))

    def test_game_must_have_valid_choice(self):
        self.player_1 = Player("Larry", "Hammer")
        self.player_2 = Player("Paula", "Paper")
        self.assertEqual("Player 1 must pick Paper, Rock or Scissors!", Prs.play_game(self, self.player_1, self.player_2))
    


    