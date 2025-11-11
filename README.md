# DESAFIO 🕹️ Improve This Game 🕹️

### Universidade Federal Rural de Pernambuco  
**Departamento de Estatística e Informática**  
**Bacharelado em Sistemas de Informação**  
**Disciplina: Princípios de Programação**

---

## **Descrição do Projeto**

Este projeto é uma versão aprimorada de um jogo de personagens originalmente proposto como desafio de Programação Orientada a Objetos (POO).  
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
- `heroi.py` – Define a classe `Heroi`, herdando de `Personagem` e incluindo métodos como `usar_item()` e `checar_nivel()`.  
- `utils.py` – Contém funções auxiliares para controle do jogo e formatação de mensagens.  
- `main.py` – Arquivo principal para executar o jogo e controlar as interações entre heróis e vilões.  

## Improved RPG Game v0.4