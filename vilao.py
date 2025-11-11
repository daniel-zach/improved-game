import math
import random
from personagem import Personagem  # Importa a classe Personagem
from heroi import Heroi
from utils import limpar_terminal, enter_continuar

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida_max, ataque, defesa, nivel, experiencia, inventario, maldade=5):
        super().__init__(nome, vida_max, ataque, defesa, nivel, experiencia, inventario)
        self.maldade = maldade

    def atacar(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo vilão.
        """   
        dano_causado = max(1, self.ataque - math.floor(personagem.defesa / 2)) # O dano é o valor de ataque menos metade do valor de defesa do oponente. Com valor mínimo 1
        print(f'\n{self.nome} atacou {personagem.nome}! Causando {dano_causado} de dano.')
        personagem.retirar_vida(dano_causado)

    def dar_loot(self, jogador):
        """
        Dá o loot após o jogador ter vencido um inimigo. Sempre dará experiência, e de acordo com a chance dará itens.
        """
        jogador.dar_experiencia(self.experiencia)

        inventario = self.inventario

        for i in range(random.randint(1,3)): # Quantos itens poderão ser dados. Chance de 1/3 para 1, 2 e 3
            for item, probabilidade in inventario.items():
                if random.random() <= (probabilidade/100): # Usa a probabilidade definida no item
                    del inventario[item] # Remove o item dropado, impedindo réplicas.
                    Heroi.adicionar_item_inventario(jogador, item)
                    break
        

    def batalhar(self, jogador):
        """
        Checa se o nível do jogador é suficiente para batalhar com o vilão.
        Inicia o menu de batalha.
        """
        if jogador.nivel < self.nivel:
            limpar_terminal()
            print("Este inimigo é poderoso demais para você!")
            enter_continuar()
            return

        while True:
            limpar_terminal()
            print(f"Batalha com {self.nome}\n")
            print(f"Vida do inimigo: {self.mostrar_vida()}")
            print(f"Sua vida:{' '*8}{jogador.mostrar_vida()}\n") # Uso ' '*8 para alinhar os mostradores de vida
            print("1. Para atacar")
            print("2. Para usar um item")
            print("0. Para fugir da batalha")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "0":
                print("Você fugiu!")
                break
            elif opcao == "1":
                jogador.atacar(self)
            elif opcao == "2":
                jogador.menu_itens()
            else:
                print("Opção inválida!")

            if self.vida > 0:
                self.atacar(jogador)
            else:
                limpar_terminal()
                print(f"Você derrotou {self.nome}!")
                self.dar_loot(jogador)
                enter_continuar()
                break

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario} Maldade: {self.maldade}'