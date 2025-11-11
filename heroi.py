import math
from personagem import Personagem  # Importa a classe Personagem
from utils import carregar_itens

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
        inventario = self.inventario
        if item in carregar_itens():
            propriedades = carregar_itens().get(item)
            tipo_item = propriedades.get('tipo')
            if item in inventario and tipo_item == 'recurso':
                quantidade_atual = inventario[item].get('quantidade',0)
                nova_quantidade = quantidade_atual + quantidade
                inventario[item]['quantidade'] = nova_quantidade
            elif item in inventario and tipo_item == 'consumivel':
                quantidade_atual = inventario[item].get('quantidade',0)
                nova_quantidade = quantidade_atual + quantidade
                inventario[item]['quantidade'] = nova_quantidade
            else:
                inventario[item] = propriedades
            print(f"{propriedades.get('nome')} adicionado ao inventário!")
        else:
            raise ValueError(f"ERRO: Não existe item do tipo '{item}' na tabela.")

    def mostrar_experiencia(self):
        tamanho_barra = 30
        exp_atual = min(math.ceil((self.experiencia/self.exp_prox_nivel)*tamanho_barra),tamanho_barra)
        vazio = tamanho_barra - exp_atual
        return f"Nível atual: {self.nivel} [{'█' * exp_atual}{'░' * vazio}] {self.experiencia}/{self.exp_prox_nivel:.0f} Exp"

    def menu_itens(self):
        pass

    def __str__(self):
        return f'Personagem: {self.nome}, Vida máxima: {self.vida_max}, Vida atual: {self.vida}, Ataque: {self.ataque}, Defesa: {self.defesa}, Nível: {self.nivel}, Inventário: {self.inventario}'