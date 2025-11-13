import math
import random
from personagem import Personagem  # Importa a classe Personagem
from heroi import Heroi
from utils import limpar_terminal, enter_continuar, opcao_invalida

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida_max, ataque, defesa, nivel, experiencia, inventario, maldade=5):
        super().__init__(nome, vida_max, ataque, defesa, nivel, experiencia, inventario)
        self.maldade = maldade

    def balancear_nivel(self, jogador):
        """
        Define as fórmulas de progressão.
        Balancemento dos stats de acordo com o nível do jogador.
        """
        nivel_jogador = jogador.nivel
        
        def escalar(valor_base, aumento, linear, fator_maldade=0):
            valor_escalado = valor_base * (1 + aumento)**(nivel_jogador - self.nivel) + linear*(nivel_jogador - self.nivel)
            valor_final = round(valor_escalado * (1 + self.maldade * fator_maldade))
            return valor_final
        
        vida = max(1, escalar(self.vida_max, 0.12, 5, 0.02)) # Escala a vida: Aumento de 12% + linear 5 + aumento por maldade de 2%
        ataque = max(1, escalar(self.ataque, 0.1, 1, 0.03)) # Escala o ataque: Aumento de 10% + linear 1 + aumento por maldade de 3%
        defesa = max(0, escalar(self.defesa, 0.08, 0.4, 0.015)) # Escala a defesa: Aumento de 8% + linear 0.5 + aumento por maldade de 1.5%
        experiencia = max(1, math.floor(escalar(self.experiencia, 0.04, 1) / 1.25**(nivel_jogador - self.nivel))) # Escala a experiência: Aumento de 4% + linear 1. Reduz quando o nível do jogador é mais alto

        self.vida_max = vida
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.experiencia =experiencia
        
        

    def atacar(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo vilão. Retorna True se o ataque matou o personagem.
        """   
        dano_causado = max(1, self.ataque - math.floor(personagem.defesa / random.randrange(1,4))) # O dano é o valor de ataque menos uma parte do valor de defesa do oponente. Com valor mínimo 1
        print(f'\n{self.nome} atacou {personagem.nome}! Causando {dano_causado} de dano.')
        personagem.retirar_vida(dano_causado)

        if not personagem.esta_vivo:
            return True
        else: return False

    def dar_loot(self, jogador):
        """
        Dá o loot após o jogador ter vencido um inimigo. Sempre dará experiência, e de acordo com a chance dará itens.
        """
        jogador.dar_experiencia(self.experiencia)

        inventario = self.inventario

        for i in range(random.randint(1,2) + 1): # Quantos itens poderão ser dados. Chance de 1/2 para 1 e 2, e adiciona 1 para as moedas
            for item, probabilidade in inventario.items():
                if item == 'moeda': # Checamos se o item é uma moeda, pois sua lógica é diferente
                    if random.randint(0,100) <= random.randint(60,80):
                        del inventario[item]
                        quantidade_moedas = probabilidade + int(probabilidade*random.uniform(-0.3, 0.3)) # Aqui o valor 'probabilidade' se refere a quantidade de moedas padrão do vilão
                        Heroi.adicionar_item_inventario(jogador,item,quantidade_moedas)
                        break
                elif random.randint(0,100) <= probabilidade: # Usa a probabilidade definida no item
                    del inventario[item] # Remove o item dropado, impedindo réplicas
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

        self.balancear_nivel(jogador)

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
                if random.random() <= 0.35: # Chance de 35% do jogador ser atacado quando foge
                    if not self.atacar(jogador):
                        print("\nVocê foi atacado enquanto fugia!")
                    else: 
                        enter_continuar()
                        break
                else: print("\nVocê fugiu!")
                enter_continuar()
                break
            elif opcao == "1":
                jogador.atacar(self)
            elif opcao == "2":
                jogador.menu_inventario()
                continue
            else:
                opcao_invalida()
                continue

            if self.vida > 0: # Se estiver vivo ataca o jogador
                if self.atacar(jogador):
                    enter_continuar()
                    break
            else:
                limpar_terminal()
                print(f"Você derrotou {self.nome}!")
                self.dar_loot(jogador)
                enter_continuar()
                break

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario} Maldade: {self.maldade}'