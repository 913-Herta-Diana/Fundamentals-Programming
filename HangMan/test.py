import unittest
from unittest.mock import MagicMock
from service import Player
from repository import Repo

class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.repo = Repo("test_sentences.txt")
        self.player = Player(self.repo)

    def test_sentence_validity(self):
        with self.assertRaises(Exception):
            self.player.sentence_validity("")
        with self.assertRaises(Exception):
            self.player.sentence_validity("a bb ccc")
        with self.assertRaises(Exception):
            self.player.sentence_validity("This is a test sentence.")
        self.repo._used.append("This is a test sentence.")
        with self.assertRaises(Exception):
            self.player.sentence_validity("This is a test sentence.")

    def test_add_sentence(self):
        self.player._add_sentence("This is a test sentence.")
        self.assertEqual(self.player._repository.used[-1], "This is a test sentence.")

    def test_format_hangman(self):
        self.player._repository._read = MagicMock(return_value="test sentence")
        result = self.player._format_hangman()
        self.assertEqual(result, "_est _e____e")

    def test_user_plays(self):
        self.player._repository._read = MagicMock(return_value="test sentence")
        self.player._format_hangman = MagicMock(return_value="_est _e____e")
        self.player._user_plays("t")
        self.assertEqual(self.player._winner, "test _e____e")
        self.assertEqual(self.player._loser, "")
        self.player._user_plays("x")
        self.assertEqual(self.player._winner, "_est _e____e")
        self.assertEqual(self.player._loser, "h")
        self.player._user_plays("e")
        self.assertEqual(self.player._winner, "_est _e__e_e")
        self.assertEqual(self.player._loser, "h")
        self.assertEqual(self.player._user_plays("s"), "_est se__e_e -> h")

    def test_complete_hangman(self):
        self.assertEqual(self.player.complete_hangman(""), "h")
        self.assertEqual(self.player.complete_hangman("h"), "ha")
        self.assertEqual(self.player.complete_hangman("ha"), "han")
        self.assertEqual(self.player.complete_hangman("han"), "hang")
        self.assertEqual(self.player.complete_hangman("hang"), "hangm")
        self.assertEqual(self.player.complete_hangman("hangm"), "hangma")
        self.assertEqual(self.player.complete_hangman("hangma"), "hangman")

    def test_check_winner(self):
        self.player._repository._read = MagicMock(return_value="test sentence")
        self.player._winner = "test sentence"
        self.assertEqual(self.player.check_winner("test sentence", ""), "Winner!")
        self.assertEqual(self.player.check_winner("_est se__e_e", "hangman"), "Loser!")
        self.assertEqual(self.player.check_winner("_est se__e_e", ""), "")

    def test_lost(self):
        self.assertEqual(self.player._lost(), "You lost ma' friend")

    def test_won(self):
        self.assertEqual(self.player._won(), "Good job! You won!")

if __name__ == '__main__':
    unittest.main()
