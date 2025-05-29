import unittest
from RPS_game import play, mrugesh, abbey, quincy, kris
from RPS import player


class UnitTests(unittest.TestCase):
    print()

    def test_player_vs_quincy(self):
        print("Probando el juego contra Quincy...")
        actual = play(player, quincy, 1000) >= 60
        self.assertTrue(
            actual,
            'Se espera que el jugador derrote a Quincy un 60% del tiempo.')

    def test_player_vs_abbey(self):
        print("Probando el juego contra Abbey...")
        actual = play(player, abbey, 1000) >= 60
        self.assertTrue(
            actual,
            'Se espera que el jugador derrote a abbey un 60% del tiempo.')

    def test_player_vs_kris(self):
        print("Probando el juego contra kris...")
        actual = play(player, kris, 1000) >= 60
        self.assertTrue(
            actual, 'Se espera que el jugador derrote a kris un 60% del tiempo.')

    def test_player_vs_mrugesh(self):
        print("Probando el juego contra mrugesh...")
        actual = play(player, mrugesh, 1000) >= 60
        self.assertTrue(
            actual,
            'Se espera que el jugador derrote a mrugesh un 60% del tiempo.')


if __name__ == "__main__":
    unittest.main()