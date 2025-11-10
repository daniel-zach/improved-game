class Personagem:
    """
    A classe Personagem representa um personagem genérico em um jogo.
    """
    def __init__(self, nome, vida_max=100, ataque=1, defesa=5, nivel=1, inventario=[]):
        self.nome = nome
        self.vida_max = vida_max
        self.vida = vida_max
        self.ataque = ataque
        self.defesa = defesa
        self.nivel = nivel
        self.inventario = inventario

    def upgrade_vida(self, incremento=10):
        """
        Aumenta a vida do personagem. O valor padrão de incremento é 10.
        """
        if self.vida + incremento > self.vida_max:
            self.vida = self.vida_max
        else:
            self.vida += incremento
        print(f'Vida de {self.nome} após upgrade: {self.vida}')


    def downgrade_vida(self, decres=10):
        """
        Reduz a vida do personagem, garantindo que não fique negativa.
        """
        if self.vida > decres:
            self.vida -= decres
        else:
            self.vida = 0
        print(f'Vida de {self.nome} após downgrade: {self.vida}')

    def update_nome(self, nome_editado):
        """
        Atualiza o nome do personagem.
        """
        self.nome = nome_editado

    def listar_inventario(self):
        """ Mostra os itens presentes no inventário do personagem. """

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario}'