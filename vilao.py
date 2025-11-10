from personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida_max, ataque, defesa, nivel, inventario, maldade='Média'):
        super().__init__(nome, vida_max, ataque, defesa, nivel, inventario)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade

    def atacar(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """   
        
        print(f'{self.nome} atacou {personagem.nome}!')
        personagem.downgrade_vida(self.ataque)

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario} Maldade: {self.maldade}'
