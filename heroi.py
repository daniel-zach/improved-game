import math
from personagem import Personagem  # Importa a classe Personagem
from utils import carregar_itens, limpar_terminal, opcao_invalida

class Heroi(Personagem):
    """ 
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida_max, ataque, defesa, nivel, experiencia, inventario):
        super().__init__(nome, vida_max, ataque, defesa, nivel, experiencia, inventario)
        self.exp_prox_nivel = int(75*(self.nivel**1.5)) # Função de progressão

    
    def atacar(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo herói.
        """   
        dano_causado = max(1, self.ataque - math.floor(personagem.defesa / 3)) # O dano é o valor de ataque menos um terço do valor de defesa do oponente. Com valor mínimo 1
        print(f'\n{self.nome} atacou {personagem.nome}! Causando {dano_causado} de dano.')
        personagem.retirar_vida(dano_causado)

    def dar_experiencia(self, acres=10):
        """
        Adiciona pontos de experiência ao herói.
        """   
        self.experiencia += acres
        self.checar_nivel()

    def checar_nivel(self):
        """
        Verifica a experiência do jogador, se for o suficiente aumenta o nível. Com um limite de nível 10.
        """
        while self.experiencia >= self.exp_prox_nivel and self.nivel < 10:
                self.nivel +=1
                self.vida_max +=20
                self.dar_vida(20)
                self.ataque +=2
                self.defesa +=2
                self.experiencia -= self.exp_prox_nivel
                self.exp_prox_nivel = int(75*(self.nivel**1.5))
        if self.experiencia > self.exp_prox_nivel and self.nivel >= 10:
            self.experiencia = self.exp_prox_nivel
            
    def adicionar_item_inventario(self, item, quantidade=1):
        #OBS: Sistema de itens poderia ser melhorado, baseado em uma classe Itens.
        """
        Adiciona itens ao inventário. Apenas uma arma de cada tipo é permitida, se for recurso ou consumível adiciona ao valor 'quantidade' do item.
        """
        inventario = self.inventario
        if item in carregar_itens():
            propriedades = carregar_itens().get(item)
            tipo_item = propriedades.get('tipo')

            if item in inventario:
                if tipo_item == 'recurso' or tipo_item == 'consumivel':
                    quantidade_atual = inventario[item].get('quantidade',0)
                    nova_quantidade = quantidade_atual + quantidade
                    inventario[item]['quantidade'] = nova_quantidade
                else:
                    print("Você já tem este item.")
                    return
            else:
                inventario[item] = propriedades
                inventario[item]['quantidade'] = quantidade
            print(f"{quantidade:02}x {propriedades.get('nome')} adicionado ao inventário!")
        else: raise ValueError(f"ERRO: Não existe item do tipo '{item}' na tabela.")

    def remover_item_inventario(self,item):
        pass

    def equipar_item(self, item):
        """
        Equipa um item que esteja no inventário, passando seus stats para o jogador.
        """
        inventario = self.inventario
        if item in inventario:
            if not inventario[item].get('equipado',False):
                inventario[item]['equipado'] = True
                for key, value in inventario[item].items():
                    if key == 'vida_max':
                        self.vida_max += value
                    if key == 'ataque':
                        self.ataque += value
                    if key == 'defesa':
                        self.defesa += value
            else:
                print(f"O item {inventario[item].get('nome')} já está equipado.")


    def desequipar_item(self, item):
        """
        Desequipa um item que esteja no inventário, removendo seus stats do jogador.
        """
        inventario = self.inventario
        if item in inventario:
            if inventario[item].get('equipado',False):
                inventario[item]['equipado'] = False
                for key, value in inventario[item].items():
                    if key == 'vida_max':
                        self.vida_max -= value
                    if key == 'ataque':
                        self.ataque -= value
                    if key == 'defesa':
                        self.defesa -= value
            else:
                print(f"O item {inventario[item].get('nome')} não está equipado.")

    def usar_item(self, item):
        """
        Usa um item se for do tipo consumível, se for equipável chama equipar_item().
        """
        inventario = self.inventario
        if item in inventario:
            tipo_item = inventario[item].get('tipo')
            quantidade_item = inventario[item].get('quantidade',0)
            item_equipado = inventario[item].get('equipado',False)
            # TODO um for loop para cada value
            if tipo_item == 'consumivel' and quantidade_item > 0:
                if 'vida' in inventario[item]:
                    self.dar_vida(inventario[item].get('vida'))
                else: raise ValueError(f"ERRO: valor a ser alterado não encontrado em {item}.")
                quantidade_final = quantidade_item - 1
                inventario[item]['quantidade'] = quantidade_final
            elif tipo_item == 'arma':
                if not item_equipado:
                    self.equipar_item(item)
                elif item_equipado:
                    self.desequipar_item(item)
            else:
                print(f"Você não pode usar um item deste tipo.")  
            if quantidade_item <= 0:
                self.remover_item_inventario(item)
        else: raise ValueError(f"ERRO: Item do tipo '{item}' não existe no inventário.")

    def menu_inventario(self):
        """
        Exibe o menu de inventário, permitindo o uso de itens.
        """
        limpar_terminal()
        print(f"{'⋮'*21} Inventário {'⋮'*21}\n")
        print("Digite o número correspondente ao item que deseja usar:\n")

        sucesso, itens = self.listar_inventario()
        if not sucesso:
            return

        opcao = input("\nEscolha um item: ").strip()

        if opcao.isdigit() and 1 <= int(opcao) <= len(itens):
            valor = itens[int(opcao) - 1]
            self.usar_item(valor)
        else:
            print("\nNenhuma opção escolhida.")
            return

    def mostrar_experiencia(self,tamanho_barra=30):
        """
        Cria uma barra no terminal para visualizar a quantidade de experiência atual e necessária para o próximo nível.
        """
        exp_atual = min(math.ceil((self.experiencia/self.exp_prox_nivel)*tamanho_barra),tamanho_barra)
        vazio = tamanho_barra - exp_atual
        return f"[{'█' * exp_atual}{'░' * vazio}] {self.experiencia}/{self.exp_prox_nivel:.0f} Exp - Nível: {self.nivel}"

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario}'