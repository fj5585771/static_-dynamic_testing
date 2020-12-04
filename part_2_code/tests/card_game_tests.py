import unittest

from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.cards= []

# define card1 and card2 objects based on the Card class and respective instance variables

        self.card_4 = Card("Spades", 4)
        self.cards.append(self.card_4)

        self.card_ace = Card("Spades", 1)
        self.cards.append(self.card_ace)

        self.card_9 = Card("Hearts", 9)
        self.cards.append(self.card_9)

        self.card_game = CardGame()

# complete this file first and write a test for each function

    def test_deck_has_ace_true(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card_ace))

    def test_deck_has_ace_false(self):
        self.assertEqual(False, self.card_game.check_for_ace(self.card_9))

    def test_for_highest_card_1(self):
        self.assertEqual(self.card_9, self.card_game.highest_card(self.card_9, self.card_4))

    def test_for_highest_card_2(self):
        self.assertEqual(self.card_9, self.card_game.highest_card(self.card_4, self.card_9))

    def test_total_cards(self):
        self.assertEqual("You have a total of 14", self.card_game.cards_total(self.cards))
