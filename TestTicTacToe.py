import unittest
from TicTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def testAddPlayer(self):
        game = TicTacToe()
        game.add_player("playerx")
        game.add_player("playery")

        self.assertTrue("playerx" in game.players)
        self.assertTrue("playery" in game.players)

    def testGame(self):
        #setup
        game = TicTacToe()
        game.add_player("playerx")
        game.add_player("playery")
        game.begin()

        self.assertTrue(game.validate("playerx", {"x" : 0, "y" : 0}))
        game.execute("playerx", {"x" : 0, "y" : 0})

        self.assertTrue(game.validate("playery", {"x" : 1, "y" : 0}))
        game.execute("playery", {"x" : 1, "y" : 0})

        self.assertTrue(game.validate("playerx", {"x" : 2, "y" : 0}))
        game.execute("playerx", {"x" : 2, "y" : 0})

        self.assertTrue(game.validate("playery", {"x" : 0, "y" : 1}))
        game.execute("playery", {"x" : 0, "y" : 1})

        self.assertTrue(game.validate("playerx", {"x" : 1, "y" : 1}))
        game.execute("playerx", {"x" : 1, "y" : 1})

        self.assertTrue(game.validate("playery", {"x" : 1, "y" : 2}))
        game.execute("playery", {"x" : 1, "y" : 2})

        self.assertTrue(game.validate("playerx", {"x" : 2, "y" : 1}))
        game.execute("playerx", {"x" : 2, "y" : 1})

        self.assertTrue(game.validate("playery", {"x" : 2, "y" : 2}))
        game.execute("playery", {"x" : 2, "y" : 2})


if __name__ == '__main__':
    unittest.main()
