import random

class Player:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mano = []
        self.total = 0
        self.estado = "jugando"

    def __str__(self):
        return f"{self.nombre}: {self.mano} (Total: {self.total}) - {self.estado}"


class Blackjack:
    def __init__(self):
        self.cartas = list(range(1, 12))  # Cartas simples 1-11
        self.jugadores = {}

    def add_player(self, nombre):
        jugador = Player(nombre)
        self.jugadores[nombre] = jugador
        return jugador

    def repartir(self, jugador):
        carta = random.choice(self.cartas)
        jugador.mano.append(carta)
        jugador.total += carta
        return carta

    def process_command(self, jugador, comando):
        if comando in ["hit", "h"]:
            carta = self.repartir(jugador)
            return f"Has pedido carta: {carta}. Total: {jugador.total}"
        elif comando in ["stand", "s"]:
            return f"{jugador.nombre} se plantó con {jugador.total}"
        elif comando in ["help"]:
            return "Comandos: hit[h], stand[s], split[l], help"
        else:
            return "Comando no reconocido."
