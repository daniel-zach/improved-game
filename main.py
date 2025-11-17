from sistema_saves import SistemaSaves
from utils import limpar_terminal, enter_continuar, opcao_invalida, carregar_personagens
from personagem import Personagem
from vilao import Vilao
from heroi import Heroi

class JogoMain:

    def __init__(self):
        self.sistemasaves = SistemaSaves(".save", "saves")
        self.novo_jogador = Heroi("Jogador", 100, 10, 5, 1, 0, {})
        self.jogador = self.novo_jogador
        self.save_atual = None

    def salvar(self):
        self.sistemasaves.salvar_dados_jogo([self.jogador],[self.save_atual])

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
        print(self.jogador.mostrar_vida(tamanho_barra), f"︱{self.jogador.ataque} Atq︱{self.jogador.defesa} Def")
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
                self.salvar()
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
        """ Cenário de caverna """
        
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
                self.salvar()
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
                self.salvar()
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

    def save_menu(self):
        """
        Menu de saves, abre quando o programa é iniciado. Oferece 3 slots e permite redefini-los.
        """
        while True:
            limpar_terminal()
            print(f"{'𓏬'*14} Escolha um save {'𓏬'*14}\n")
            print("1. Save slot 1")
            print("2. Save slot 2")
            print("3. Save slot 3")
            print("R. Resetar um save")

            opcao = input("\nEscolha uma opção: ").strip().lower()

            if opcao == "1":
                self.jogador = self.sistemasaves.carregar_dados_jogo(['save_1'], [self.novo_jogador])
                self.save_atual = 'save_1'
                return
            elif opcao == "2":
                self.jogador = self.sistemasaves.carregar_dados_jogo(['save_2'], [self.novo_jogador])
                self.save_atual = 'save_2'
                return
            elif opcao == "3":
                self.jogador = self.sistemasaves.carregar_dados_jogo(['save_3'], [self.novo_jogador])
                self.save_atual = 'save_3'
                return
            elif opcao == "r":
                while True:
                    limpar_terminal()
                    print("Qual slot deseja resetar:\n")
                    print("1. Save slot 1")
                    print("2. Save slot 2")
                    print("3. Save slot 3")
                    print("Enter para cancelar")

                    opcao_reset = input("\nEscolha uma opção: ").strip()

                    if opcao_reset in ["1","2","3"]:
                        self.sistemasaves.deletar_arquivo(f"save_{opcao_reset}")
                        print(f"Save slot {opcao_reset} redefinido com sucesso!")
                        enter_continuar()
                        break
                    else:
                        break

    def main_encruzilhada(self):
        while True:

            if not self.save_atual:
                self.save_menu()

            if not self.jogador.esta_vivo: # Se o jogador estiver morto chamamos reviver() e salvamos o jogo
                self.jogador.reviver()
                self.salvar()
                enter_continuar()

            limpar_terminal()
            self.hud()
            print(f"\n{'𓏬'*18} Encruzilhada {'𓏬'*18}\n")
            print("E/I. Abrir inventário")
            print("1. Visitar a vila")
            print("2. Ir para a floresta")
            print("3. Ir para as cavernas")
            print("0. Para salvar e sair")
            opcao = input("\nEscolha uma opção: ").strip().lower()

            if opcao == "0":
                print("\nObrigado por jogar!")
                self.salvar()
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
