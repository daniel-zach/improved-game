import json
import os

def limpar_terminal():
    print("\033[H\033[2J", end="")
    print("\033[H\033[3J", end="")
    print("\033c", end="")

def enter_continuar():
    input("\nPressione Enter para continuar...")

def opcao_invalida():
    print("\nOpção inválida!")

def carregar_itens():
    if os.path.exists("data/itens.json"):
        try:
            with open("data/itens.json", encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Não foi possível carregar itens.json")
            return {}
    raise ValueError ("Não foi possível encontrar itens.json")

def carregar_personagens():
    if os.path.exists("data/personagens.json"):
        try:
            with open("data/personagens.json", encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Não foi possível carregar personagens.json")
            return {}
    raise ValueError ("Não foi possível encontrar personagens.json")