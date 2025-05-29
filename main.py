# Este script se usa para jugar al juego de Piedra, Papel o Tijera (RPS)
# contra diferentes jugadores y para realizar pruebas unitarias.
from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

play(player, quincy, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
play(player, mrugesh, 1000)

# Descomentar la línea siguiente para jugar contra un jugador humano:
# play(human, abbey, 20, verbose=True)

# Descomentar la línea siguiente para jugar contra un jugador aleatorio:
# play(human, random_player, 1000)



# Descomentar la línea siguiente para ejecutar las pruebas unitarias.
# main(module='test_module', exit=False)