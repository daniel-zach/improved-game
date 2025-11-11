import json

def limpar_terminal():
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def enter_continuar():
    input("\nPressione Enter para continuar...")

def opcao_invalida():
    print("\nOpção inválida!")

def carregar_itens():
    try:
        with open("data/itens.json", encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
    return{}

def carregar_personagens():
    try:
        with open("data/personagens.json", encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}
    return{}