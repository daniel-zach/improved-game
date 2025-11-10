from personagem import Personagem
from vilao import Vilao
from heroi import Heroi

def main():
    # Criando personagens e vilões
    heroi = Heroi('Link', 100, 15, 10, 1, [])
    npc = Personagem('José', 80)
    vilao = Vilao('Ganon', 100, 50, 20, 1, [], 'Baixa')

    # Mostrando personagens
    print(heroi)
    print(npc)
    print(vilao)

    # Vilão ataca o herói
    vilao.atacar(heroi)

    # Melhorando a vida do herói
    heroi.upgrade_vida(20)
    print(f'{heroi.nome} após upgrade de vida: {heroi.vida}')

    # Mudando nome do NPC
    npc.update_nome('Princesa Zelda')
    print(f'Nome atualizado: {npc.nome}')

if __name__ == "__main__":
    main()
