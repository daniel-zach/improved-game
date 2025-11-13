import json
import os
from utils import limpar_terminal, enter_continuar, opcao_invalida, carregar_personagens
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi

class JogoMain:

    def __init__(self):
        self.jogador = Heroi("Jogador", 10, 10, 5, 1, 0, {})

    def spawn(self, nome):
        """
        Inicializa um personagem, checando se é NPC ou vilão.
        """
        if nome in carregar_personagens().get("viloes", {}):
            dados = carregar_personagens()["viloes"][nome]
            return Vilao(**dados)
        elif nome in carregar_personagens().get("npcs", {}):
            dados = carregar_personagens()["npcs"][nome]
            return Personagem(**dados)
        else:
            raise ValueError(f"Personagem '{nome}' não encontrado.")

    def hud(self, tamanho_barra=25):
        print(self.jogador.mostrar_vida(tamanho_barra))
        print(self.jogador.mostrar_experiencia(tamanho_barra))
        

    def floresta(self):
        """Cenário de floresta"""

        while self.jogador.esta_vivo:
            limpar_terminal()
            self.hud()
            print(f"\n{'𓃑'*19} Floresta {'𓃑'*19}\n")
            print("E/I. Abrir inventário")
            print("1. Atacar aranhas")
            print("2. Atacar goblins")
            print("3. Atacar slimes")
            print("0. Para voltar")

            if not self.jogador.esta_vivo:
                break

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "0":
                print("Você anda até a encruzilhada")
                break
            elif opcao in ["e", "i"]:
                self.jogador.menu_inventario()
            elif opcao == "1":
                self.spawn("aranha").batalhar(self.jogador)
            elif opcao == "2":
                self.spawn("goblin").batalhar(self.jogador)
            elif opcao == "3":
                self.spawn("slime").batalhar(self.jogador)
            else:
                opcao_invalida()
                enter_continuar()

    def caverna(self):
        """Cenário de caverna"""
        
        while self.jogador.esta_vivo:
            limpar_terminal()
            self.hud()
            print(f"\n{'𓃑'*14} Caverna Misteriosa {'𓃑'*14}\n")
            print("E/I. Abrir inventário")
            print("1. Atacar esqueletos")
            print("2. Atacar troll")
            print("0. Para voltar")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "0":
                print("Você anda até a encruzilhada")
                break
            elif opcao in ["e", "i"]:
                self.jogador.menu_inventario()
            elif opcao == "1":
                self.spawn("esqueleto").batalhar(self.jogador)
            elif opcao == "2":
                self.spawn("troll").batalhar(self.jogador)
            else:
                opcao_invalida()
                enter_continuar()

    def vila(self):
        """ Cenário da vila """
        while self.jogador.esta_vivo:
            limpar_terminal()
            self.hud()
            print(f"\n{'𓏬'*18} Vila Pacata {'𓏬'*19}\n")
            print("E/I. Abrir inventário")
            print("1. Entrar na loja")
            print("2. Falar com Gui")
            print("3. Falar com Vini")
            print("0. Para sair da vila")
            opcao = input("\nEscolha uma opção: ").strip().lower()

            if opcao == "0":
                break
            elif opcao in ["e", "i"]:
                self.jogador.menu_inventario()
            elif opcao == "1":
                self.jogador.menu_negociar(self.spawn('guilherme'))
            elif opcao == "2":
                self.spawn('guilherme').dialogar()
            elif opcao == "3":
                self.spawn('vini').dialogar()
            else:
                opcao_invalida()
                enter_continuar()

    def main_encruzilhada(self):
        self.jogador.adicionar_item_inventario('moeda',500)
        self.jogador.adicionar_item_inventario('adaga')
        self.jogador.adicionar_item_inventario('graveto')
        while True:

            if not self.jogador.esta_vivo: # Se o jogador estiver morto chamamos reviver()
                self.jogador.reviver()

            limpar_terminal()
            self.hud()
            print(f"\n{'𓏬'*18} Encruzilhada {'𓏬'*18}\n")
            print("E/I. Abrir inventário")
            print("1. Visitar a vila")
            print("2. Ir para a floresta")
            print("3. Ir para as cavernas")
            print("0. Para sair do jogo")
            opcao = input("\nEscolha uma opção: ").strip().lower()

            if opcao == "0":
                print("Obrigado por jogar!")
                break
            elif opcao in ["e", "i"]:
                self.jogador.menu_inventario()
            elif opcao == "1":
                self.vila()
            elif opcao == "2":
                self.floresta()
            elif opcao == "3":
                self.caverna()
            else:
                opcao_invalida()
                enter_continuar()

if __name__ == "__main__":
    JogoMain().main_encruzilhada()
