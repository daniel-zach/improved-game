# Improved RPG Game v0.7

### Universidade Federal Rural de Pernambuco  
**Departamento de Estatística e Informática**  
**Bacharelado em Sistemas de Informação**  
**Disciplina: Princípios de Programação**

---

## **Descrição do Projeto**

Este projeto é uma versão aprimorada de um jogo de personagens originalmente proposto como **desafio** de Programação Orientada a Objetos (POO).  
Foram aplicados conceitos de **herança**, **polimorfismo**, **listas**, **dicionários** e **estruturas de controle** para criar uma experiência mais interativa e dinâmica.

## **Principais Melhorias Implementadas**

- Inclusão da classe `Heroi`, herdando de `Personagem`, com atributos e métodos exclusivos.  
- Expansão das classes existentes para permitir **ataques, defesas, uso de habilidades** e **interações entre personagens**.  
- Implementação de um **sistema de batalha** entre heróis e vilões com decisões e repetições.  
- Criação de um **sistema de diálogo** e eventos durante o jogo para enriquecer a narrativa.  
- Utilização de **listas e dicionários** para gerenciamento de personagens, itens e atributos.
- Melhoria da **interface textual**, com mensagens mais envolventes e dinâmicas.  
- Modularização do código, permitindo fácil expansão e manutenção.  

## **Estrutura do Projeto**

O projeto contém os seguintes arquivos:

- `personagem.py` – Define a classe base `Personagem`.  
- `vilao.py` – Define a classe `Vilao`, herdando de `Personagem` com métodos únicos, como `batalhar()` e `dar_loot()`.  
- `heroi.py` – Define a classe `Heroi`, herdando de `Personagem` e incluindo métodos como `usar_item()` e `checar_nivel()`. Faz também a sobrescrita do método `morrer()` para gerar uma interação única.
- `utils.py` – Contém funções auxiliares para controle do jogo e formatação de mensagens.  
- `main.py` – Arquivo principal para executar o jogo e controlar as interações entre heróis e vilões.  

## **Improved RPG Game - Release Notes**

### v0.7
- Sistema de saves.
- Sistemas de diálogos.
- Correção de bugs no inventário.

### v0.6
- Balanceamento do sistema de níveis. Stats de inimigos baseados no nível do jogador.
- Sistema de morte, com melhoria da fuga de batalhas.
- Sistema de loja. Com itens sendo vendidos por npcs.
- Inventario mostra itens equipados e seus stats.
- Correção de bugs no inventário/itens. Agora só é possível equipar um item.

### v0.5
- Sistema completo de itens. Com uso de consumíveis e equipáveis.
- Sistema de loot. Monstros agora dropam loot de acordo com as probabilidades definidas em seu inventário.
- Melhorias na interface e de qualidade de vida.
- Correção de bugs.

## Improved RPG Game

**Feito por:** [Daniel Zacheu](https://github.com/daniel-zach)

**Projeto original:** [improve-this-game](https://github.com/profcvanut/improve-this-game)