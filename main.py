import json
import os
from utils import limpar_terminal, enter_continuar, opcao_invalida, carregar_personagens
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi

class JogoMain:

    def __init__(self):
        self.jogador = Heroi("Jogador", 100, 10, 5, 1, 0, {})

    def spawn(self, nome):
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
        
        while True:
            limpar_terminal()
            self.hud()
            print(f"\n{'⸬'*19} Floresta {'⸬'*19}\n")
            print("E/I. Abrir inventário")
            print("1. Atacar aranhas")
            print("2. Atacar goblins")
            print("3. Atacar slimes")
            print("0. Para voltar a vila")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "0":
                print("Obrigado por jogar!")
                break
            elif opcao in ["e", "i"]:
                self.jogador.menu_inventario()
                enter_continuar()
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
        
        while True:
            limpar_terminal()
            self.hud()
            print(f"\n{'⸬'*14} Caverna Misteriosa {'⸬'*14}\n")
            print("E/I. Abrir inventário")
            print("1. Atacar esqueletos")
            print("2. Atacar troll")
            print("0. Para voltar a vila")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "0":
                print("Obrigado por jogar!")
                break
            elif opcao in ["e", "i"]:
                self.jogador.menu_inventario()
                enter_continuar()
            elif opcao == "1":
                self.spawn("esqueleto").batalhar(self.jogador)
            elif opcao == "2":
                self.spawn("troll").batalhar(self.jogador)
            else:
                opcao_invalida()
                enter_continuar()

    def main(self):
        while True:
            limpar_terminal()
            self.hud()
            print(f"\n{'⸬'*17} Vila Pacata {'⸬'*18}\n")
            print("E/I. Abrir inventário")
            print("1. Visitar a loja")
            print("2. Ir para a floresta")
            print("3. Ir para as cavernas")
            print("0. Para sair")

            opcao = input("\nEscolha uma opção: ").strip().lower()

            if opcao == "0":
                print("Obrigado por jogar!")
                break
            elif opcao in ["e", "i"]:
                self.jogador.menu_inventario()
                enter_continuar()
            elif opcao == "1":
                pass
            elif opcao == "2":
                self.floresta()
            elif opcao == "3":
                self.caverna()
            else:
                opcao_invalida()
                enter_continuar()

if __name__ == "__main__":
    JogoMain().main()
