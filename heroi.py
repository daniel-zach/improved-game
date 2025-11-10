from personagem import Personagem

class Heroi(Personagem):
    """ 
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida_max, ataque, defesa, nivel, inventario):
        super().__init__(nome, vida_max, ataque, defesa, nivel, inventario)