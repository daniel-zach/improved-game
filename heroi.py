import math
import random
from personagem import Personagem  # Importa a classe Personagem
from utils import carregar_itens, limpar_terminal, enter_continuar

class Heroi(Personagem):
    """ 
    A classe Heroi representa as características de um herói no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, vida_max, ataque, defesa, nivel, experiencia, inventario):
        super().__init__(nome, vida_max, ataque, defesa, nivel, experiencia, inventario)
        self.exp_prox_nivel = 85

    def reviver(self):
        """
        Revive o herói, resetando os stats de vida.
        """
        self.esta_vivo = True
        self.vida = self.vida_max

    def morrer(self):
        """
        Sobrescrita do método morrer() para o Heroi.
        Esvazia o inventário deixando apenas metade das moedas.
        """
        self.esta_vivo = False
        inventario = self.inventario
        if inventario:
            for item in inventario: # Desequipa todos os itens
                self.desequipar_item(item)
            moedas = 0
            if 'moeda' in inventario:
                moedas = int(inventario['moeda'].get('quantidade')/2) # Calcula a metade das moedas atuais
            self.inventario = {}
            if moedas > 0:
                self.adicionar_item_inventario('moeda',moedas) # Adiciona o novo valor de moedas
        self.experiencia = 0
        limpar_terminal()
        print("Você foi derrotado!")
        print("Parece que seus itens foram levados.")
    
    def atacar(self, personagem):
        """
        Reduz a vida de outro personagem atacado pelo herói.
        """   
        dano_causado = max(1, self.ataque - math.floor(personagem.defesa / random.randrange(2,4))) # O dano é o valor de ataque menos uma parte do valor de defesa do oponente. Com valor mínimo 1
        print(f'\n{self.nome} atacou {personagem.nome}! Causando {dano_causado} de dano.')
        personagem.retirar_vida(dano_causado)

    def dar_experiencia(self, acres=10):
        """
        Adiciona pontos de experiência ao herói.
        """   
        self.experiencia += acres
        self.checar_nivel()
        print(f"Você recebeu {acres} de Exp.")

    def checar_nivel(self):
        """
        Define as fórmulas de progressão
        Verifica a experiência do jogador, se for o suficiente aumenta o nível. Com um limite de nível 10.
        """
        level_up = False
        while self.experiencia >= self.exp_prox_nivel and self.nivel < 10:
                self.nivel +=1
                self.experiencia -= self.exp_prox_nivel
                self.exp_prox_nivel = int(85*(self.nivel**1.5)) # Função de progressão
                level_up = True

        def escalar(valor_base, aumento, linear):
            valor_escalado = valor_base * (1 + aumento)**(self.nivel - 1) + linear*(self.nivel - 1)
            return round(valor_escalado)
        
        vida_max = escalar(self.vida_max, 0.11, 10) # Escala a vida: Aumento de 11% + linear 10
        vida_extra = vida_max - self.vida_max # A vida que será curada ao subir de nível, equivale ao aumento de vida_max
        ataque = escalar(self.ataque, 0.1, 2) # Escala o ataque: Aumento de 10% + linear 2
        defesa = escalar(self.defesa, 0.1, 1) # Escala a defesa: Aumento de 10% + linear 1

        if level_up:
            self.vida_max = vida_max
            self.dar_vida(vida_extra)
            self.ataque = ataque
            self.defesa = defesa

        if self.experiencia > self.exp_prox_nivel and self.nivel >= 10:
            self.experiencia = self.exp_prox_nivel - 1
            
    def adicionar_item_inventario(self, item, quantidade=1):
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
                    print(f"Você já tem {item}.")
                    return
            else:
                inventario[item] = propriedades
                inventario[item]['quantidade'] = quantidade
            print(f"{quantidade:02}x {propriedades.get('nome')} adicionado ao inventário!")
        else: raise ValueError(f"ERRO: Não existe item do tipo '{item}' na tabela.")
        

    def remover_item_inventario(self,item):
        """
        Remove o item do inventário.
        """
        print("Item sendo removido: "+item)
        inventario = self.inventario
        if item in inventario:
            del inventario[item]
        else: return ValueError(f"ERRO: Não existe '{item}' no inventário.")

    def equipar_item(self, item):
        """
        Equipa um item que esteja no inventário, passando seus stats para o jogador.
        """
        # Se o sistema for aumentado para conter um item como 'armadura', o check deverá levar em conta o tipo de item.
        inventario = self.inventario
        if item in inventario:
            if not inventario[item].get('equipado',False):
                for i in inventario: # Procuramos por outros itens que estejam equipados e os desequipamos
                    if inventario[i].get('equipado', False):
                        self.desequipar_item(i)
                inventario[item]['equipado'] = True
                for key, value in inventario[item].items():
                    if key == 'vida_max':
                        self.upgrade_vida_max(value)
                    if key == 'ataque':
                        self.ataque += value
                    if key == 'defesa':
                        self.defesa += value
            else: return f"O item {inventario[item].get('nome')} já está equipado."


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
                        self.downgrade_vida_max(value)
                    if key == 'ataque':
                        self.ataque -= value
                    if key == 'defesa':
                        self.defesa -= value
            else: return f"O item {inventario[item].get('nome')} não está equipado."

    def usar_item(self, item):
        """
        Usa um item se for do tipo consumível, se for equipável chama equipar_item().
        """
        inventario = self.inventario
        if item in inventario:
            tipo_item = inventario[item].get('tipo')
            quantidade_item = inventario[item].get('quantidade',0) # Este valor é definido aqui e não atualiza mesmo usando 'quantidade_item' depois
            item_equipado = inventario[item].get('equipado',False)
            if tipo_item == 'consumivel' and quantidade_item > 0: # Checamos se é consumível
                for key, value in inventario[item].items(): # Adicionamos cada stat ao player se houver
                    if key == 'vida':
                        self.dar_vida(value)
                    elif key == 'experiencia':
                        self.dar_experiencia(value)
                inventario[item]['quantidade'] = quantidade_item - 1
                enter_continuar()
            elif 'equipado' in inventario[item]: # Se for do tipo "equipável" chamamos equipar_item ou desequipar_item
                if not item_equipado:
                    self.equipar_item(item)
                elif item_equipado:
                    self.desequipar_item(item)
            else:
                print(f"Você não pode usar um item deste tipo.")  
            if inventario[item].get('quantidade',0) < 1: # Se no fim do uso a quantidade for 0, removemos o item do inventário
                self.remover_item_inventario(item)
        else: raise ValueError(f"ERRO: Item do tipo '{item}' não existe no inventário.")

    def menu_inventario(self):
        """
        Exibe o menu de inventário, permitindo o uso de itens.
        """
        while True:
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

    def menu_negociar(self, personagem):
        """
        Menu de negociação com NPCs. Recebe do NPC os itens disponíveis e os custos.
        Permite ao jogador comprar estes itens em troca de moedas.
        """
        while True:
            limpar_terminal()
            print(f"{'⋮'*17} Loja do {personagem.nome} {'⋮'*17}\n")
            print("Digite o número correspondente ao item que deseja comprar:\n")

            sucesso, itens, custos = personagem.itens_a_venda()
            if not sucesso:
                return
            
            inventario = self.inventario
            quantidade_moedas = 0
            if 'moeda' in inventario: # Checamos se há moedas no inventário e mostramos a quantia
                quantidade_moedas = inventario['moeda'].get('quantidade',0)
            print(f"\nVocê tem: ${quantidade_moedas}")

            opcao = input("\nEscolha um item: ").strip()

            if opcao.isdigit() and 1 <= int(opcao) <= len(itens):
                item = itens[int(opcao) - 1]
                custo = custos[int(opcao) - 1]
                if custo <= quantidade_moedas:
                    if custo < quantidade_moedas:
                        inventario['moeda']['quantidade'] = quantidade_moedas - custo
                    else:
                        self.remover_item_inventario('moeda')
                    self.adicionar_item_inventario(item)
                else: print(f"Você não tem dinheiro suficiente para comprar este item!")
                enter_continuar()
            else:
                print("\nNenhuma opção escolhida.")
                return

    def mostrar_experiencia(self,tamanho_barra=30):
        """
        Cria uma barra no terminal para visualizar a quantidade de experiência atual e necessária para o próximo nível.
        """
        exp_atual = min(math.ceil((self.experiencia/self.exp_prox_nivel)*tamanho_barra),tamanho_barra)
        vazio = tamanho_barra - exp_atual
        return f"⟨{'█' * exp_atual}{'░' * vazio}⟩ {self.experiencia}/{self.exp_prox_nivel:.0f} Exp - Nível: {self.nivel}"

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario}'