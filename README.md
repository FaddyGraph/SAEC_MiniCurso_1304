# ⚔️ RPG Battle Simulator - Minicurso Python (SAEC 2026)

Este projeto foi desenvolvido como material prático para o minicurso de introdução à programação utilizando **Python**. O objetivo é apresentar conceitos fundamentais da linguagem de uma forma divertida e interativa: através de um simulador de batalhas de RPG em modo texto (CLI).

Com este código, o usuário pode criar dois personagens personalizados, distribuir pontos de atributos de forma estratégica e colocá-los para duelar em um sistema de turnos dinâmico, completo com rolagens de dados, ataques físicos, mágicos, cura e até um sistema de "salvamento por sorte".

---

## 🎯 O que este projeto ensina? (Conceitos do 1º Período)

Se você está começando agora na programação, este código é um excelente mapa para entender como diferentes peças do Python se encaixam:

* **Orientação a Objetos (POO):** Utilização de `classes` e `métodos` para estruturar a Ficha do Personagem e suas ações.
* **Estruturas de Dados:** Uso prático de `dicionários` para gerenciar atributos e bônus dinamicamente.
* **Controle de Fluxo e Loops:** Laços de repetição (`while`, `for`) e condicionais (`if/elif/else`) para gerenciar os menus e o sistema de turnos da batalha.
* **Tratamento de Erros:** Uso de estruturas `try/except` para garantir que o programa não quebre caso o usuário digite um valor inválido.
* **Módulos Nativos:** Implementação das bibliotecas `random` (para simular a aleatoriedade dos dados de RPG) e `time` (para criar pausas durante o combate).

---

## 🏆 Atividade Prática: Desafios de Engenharia (25 minutos)

Para colocar a mão na massa e fixar os conceitos do minicurso, propomos 4 desafios práticos de modificação do código. Eles simulam a evolução de um software real, onde você precisa entender a arquitetura existente e implementar novas regras de negócio!

### 🛠️ Desafio 1 (Validação): Gasto Obrigatório de Pontos
Altere a função `criar_personagem` para que o jogador seja **obrigado a gastar exatamente todos os 20 pontos** disponíveis. O sistema não deve aceitar a criação se sobrarem pontos ou se o valor for ultrapassado.

### 🛡️ Desafio 2 (Estrutura): Novo Atributo de Defesa
Adicione um novo atributo chamado `"Defesa"` no dicionário de atributos do personagem. Em seguida, atualize a fórmula da Classe de Armadura (CA) na inicialização da classe (`__init__`) para refletir a nova regra:
* `CA = 10 + bônus de Destreza + bônus de Defesa`

### 🩸 Desafio 3 (Lógica Condicional): Mecânica de Fúria
Altere a lógica de aplicação de dano no combate. Caso o HP atual do personagem que está atacando esteja **abaixo de 10**, o seu ataque de Dano Físico (Opção 1) deve se tornar um "Ataque Desesperado" e causar o **dobro do dano** rolado.

### 📊 Desafio 4 (Avançado): Relatório de Danos (Acumuladores)
Crie um sistema de estatísticas para o fim da luta:
* Crie uma variável acumuladora chamada `dano_total_causado` para cada personagem (começando em 0).
* Toda vez que o personagem acertar um ataque (físico ou mágico), some o valor do dano aplicado nessa variável.
* Ao final da batalha, exiba quem foi o maior causador de danos da rodada.

---

## 🕹️ Funcionalidades do Sistema

1.  **Criação de Personagem:** Distribuição de 20 pontos entre 6 atributos clássicos (Força, Destreza, Constituição, Inteligência, Sabedoria e Sorte).
2.  **Cálculo Dinâmico:** O sistema calcula automaticamente os bônus de atributo, a vida máxima (HP) e a defesa (CA) baseado nas escolhas do jogador.
3.  **Menu de Ações no Combate:**
    * `Dano Físico:` Baseado em Força.
    * `Dano Mágico:` Baseado em Inteligência.
    * `Cura:` Baseado em Sabedoria (limite de 3 usos).
4.  **Mecânica de Sorte (Milagre):** Se um personagem for receber um golpe fatal e ainda tiver sua "Sorte" intacta, o sistema faz uma rolagem oculta. Se passar, o personagem sobrevive com 1 de HP!

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o Python 3 instalado em sua máquina.

1. Baixe o arquivo `main.py` (ou clone o repositório).
2. Abra o terminal na pasta do arquivo e execute o comando:
   ```bash
   python main.py
