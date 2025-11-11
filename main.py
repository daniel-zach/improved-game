import json
import os
from utils import limpar_terminal, enter_continuar, carregar_personagens
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

    def floresta(self):
        """Cenário de floresta"""
        
        while True:
            limpar_terminal()
            print(self.jogador.mostrar_experiencia())
            print("\n1. Atacar aranhas")
            print("0. Para voltar a vila")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "0":
                print("Obrigado por jogar!")
                break
            elif opcao == "1":
                self.spawn("aranha").batalhar(self.jogador)
            elif opcao == "2":
                self.spawn("goblin").batalhar(self.jogador)
            else:
                print("Opção inválida!")
                enter_continuar()

    def main(self):

        while True:
            limpar_terminal()
            print(self.jogador.mostrar_experiencia())
            print("\n1. Teste")
            print("2. Ir para a floresta")
            print("3 Para xp")
            print("0. Para sair")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "0":
                print("Obrigado por jogar!")
                break
            elif opcao == "1":
                self.jogador.adicionar_item_inventario('moeda')
            elif opcao == "2":
                self.floresta()
            elif opcao == "3":
                self.jogador.dar_experiencia()
            elif opcao == "e":
                self.jogador.listar_inventario()
                enter_continuar()
            else:
                print("Opção inválida!")
                enter_continuar()

if __name__ == "__main__":
    JogoMain().main()
