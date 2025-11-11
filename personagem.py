import math

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
        print(f'Vida atual de {self.nome}: {self.vida}')

    def upgrade_vida_max(self, acres=10):
        """
        Aumenta a vida máxima do personagem. O valor padrão de incremento é 10.
        """    
        self.vida_max += acres
        print(f'Vida de {self.nome} após upgrade: {self.vida}')

    def downgrade_vida_max(self, descres=10):
        """
        Reduz a vida máxima do personagem, garantindo que não fique negativa.
        """
        if self.vida_max > descres:
            self.vida_max -= descres
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
            print(f"{i}. {nome} {quantidade}x")
            itens.append(item)
        return True, itens

    def dialogar(self):
        pass

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario}'