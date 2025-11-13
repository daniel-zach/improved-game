import math
from utils import carregar_itens

class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, vida_max=100, ataque=1, defesa=5, nivel=1, experiencia=0, inventario={}, dialogos={}):
        self.nome = nome
        self.vida_max = vida_max
        self.vida = vida_max
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = nivel
        self.experiencia = experiencia
        self.inventario = inventario
        self.dialogos = dialogos

    def dar_vida(self, acres=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        if self.vida + acres > self.vida_max:
            self.vida = self.vida_max
        else:
            self.vida += acres
        print(f'Vida atual de {self.nome}: {self.vida}')

    def retirar_vida(self, decres=10):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > decres:
            self.vida -= decres
        else:
            self.vida = 0
            #TODO Chamar morte
        print(f'Vida atual de {self.nome}: {self.vida}')

    def upgrade_vida_max(self, acres=10):
        """
        Aumenta a vida máxima do personagem. O valor padrão de incremento é 10.
        """    
        self.vida_max += acres
        if self.vida >= self.vida_max - acres:
            self.vida = self.vida_max
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def downgrade_vida_max(self, descres=10):
        """
        Reduz a vida máxima do personagem, garantindo que não fique negativa.
        """
        if self.vida_max > descres:
            self.vida_max -= descres
            if self.vida > self.vida_max:
                self.vida = self.vida_max
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def mostrar_vida(self, tamanho_barra=20):
        """
        Cria uma barra no terminal para visualizar a quantidade de vida restante e total.
        """
        vida_atual = min(math.ceil((self.vida/self.vida_max)*tamanho_barra),tamanho_barra)
        vazio = tamanho_barra - vida_atual
        return f"[{'█' * vida_atual}{'░' * vazio}] {self.vida}/{self.vida_max} PV"

    def listar_inventario(self):
        """ 
        Mostra os itens presentes no inventário do personagem. Utilizando os valores 'nome' e 'quantidade'.
        """
        itens = []
        if not self.inventario:
            print("\nO inventário está vázio!")
            return False, itens

        for i, (item, dados) in enumerate(sorted(self.inventario.items()), start=1):
            nome = dados.get('nome', item)
            quantidade = dados.get('quantidade',0)
            equipado = dados.get('equipado',False)

            lista_verificar = ['vida_max','vida','ataque','defesa']
            lista_formatada = ""
            for valor in sorted(dados):
                if valor in lista_verificar:
                    lista_formatada = f"{lista_formatada}{valor.capitalize()} - {dados.get(valor)} "

            if equipado:
                print(f"{i}. {nome} ★︱{lista_formatada} ")
            elif dados.get('tipo') == 'arma':
                print(f"{i}. {nome} ☆︱{lista_formatada} ")
            else:
                print(f"{i}. {nome} {quantidade}x︱{lista_formatada}")
            itens.append(item)
        return True, itens

    def dialogar(self):
        pass

    def itens_a_venda(self):
        """
        Lista de itens disponíveis para venda.
        """
        itens = []
        valores = []
        if self.inventario:
            for i, (item, valor) in enumerate(sorted(self.inventario.items()), start=1):
                if item in carregar_itens():
                    propriedades = carregar_itens().get(item)
                    item_nome = propriedades.get('nome')
                    print(f"{i}. {item_nome} - ${valor}")
                    itens.append(item)
                    valores.append(valor)
                else: return ValueError (f"O item '{item}' não está na lista de itens.")
            return True, itens, valores
        else: 
            print(f"Não tenho nada para vender.")
            return False, itens, valores

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario}'