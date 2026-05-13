# ⚔️ Guia de Resolução: Desafios do Simulador RPG em Python

Olá, pessoal! Parabéns por terem chegado até o final do nosso minicurso de Python.

Durante a prática, propusemos alguns desafios para alterar as regras do nosso simulador de batalhas. Na engenharia de software, raramente começamos um código do zero; na maior parte do tempo, precisamos ler um código que já existe, entender sua lógica e adicionar novas funcionalidades.

Abaixo, detalhamos como cada um dos desafios foi resolvido por um dos monitores, mostrando onde o código mudou e o porquê de cada escolha. Usem este material para revisar os conceitos de laços de repetição (`while`, `for`), listas, dicionários e condicionais (`if/else`).

---

# 🛠️ Desafio 1: Gasto Obrigatório de Pontos

## O Problema
No código original, o jogador podia terminar a criação da ficha sem gastar os 20 pontos, o que deixava o personagem mais fraco por engano.

## A Solução
Precisávamos "prender" o usuário na tela de distribuição até que a conta de pontos zerasse.

## Como ficou o código (na função `criar_personagem`)

```python
while pontos_restantes != 0:  # <-- ADICIONAMOS ESSE LOOP PRINCIPAL
    for atr in atributos.keys():
        while True:
            # ... (código de input omitido) ...
            if 0 <= pontos <= pontos_restantes:
                atributos[atr] += pontos  # <-- MUDAMOS DE '=' PARA '+='
                pontos_restantes -= pontos
                break

        if pontos_restantes == 0:
            break  # <-- ADICIONAMOS ESSA QUEBRA
```

## Por que fizemos isso?

### `while pontos_restantes != 0`
Esse laço garante que o programa só vai sair dessa etapa quando não sobrar nenhum ponto.

### Operador `+=`
Antes usávamos `=`, que simplesmente substituía o valor. Mudamos para `+=` porque, se o jogador precisar passar pela lista de atributos uma segunda vez, os novos pontos serão somados aos anteriores.

### `if pontos_restantes == 0: break`
Se o jogador gastar todos os pontos logo no primeiro atributo, o programa não continua perguntando os demais atributos desnecessariamente.

---

# 🛡️ Desafio 2: Novo Atributo "Defesa"

## O Problema
Queríamos adicionar uma camada extra de proteção na esquiva do personagem.

## A Solução
Para um atributo existir, ele precisa ser criado no dicionário inicial e depois ser utilizado nas fórmulas de combate.

## Como ficou o código

```python
# 1. Na função criar_personagem():
atributos = {
    "Força": 0,
    "Destreza": 0,
    "Constituição": 0,
    "Inteligência": 0,
    "Sabedoria": 0,
    "Sorte": 0,
    "defesa": 0
}

# 2. No construtor da classe Personagem (__init__):
self.ca = 10 + self.bonus.get("Destreza", 0) + self.bonus.get("defesa", 0)
```

## Por que fizemos isso?

No Python, um dicionário (`{}`) guarda chaves e valores. Ao adicionarmos `"defesa": 0`, o sistema automaticamente passa a considerar esse atributo durante a distribuição de pontos.

Depois, usamos:

```python
self.bonus.get("defesa", 0)
```

para recuperar o valor de defesa e somá-lo à Classe de Armadura (`CA`).

---

# 🩸 Desafio 3: Mecânica de Fúria (Ataque Desesperado)

## O Problema
Queríamos que ataques físicos causassem o dobro de dano quando o personagem estivesse com pouca vida (`HP < 10`).

## A Solução
Precisávamos verificar a vida do atacante logo após o cálculo do dano.

## Como ficou o código (na função `simular_batalha`)

```python
# Dentro da Ação 1 (Dano Físico):
if dado_acerto + atacante.bonus["Força"] >= defensor.ca:
    dano_causado = random.randint(1, 10) + atacante.bonus["Força"]

    # --- NOVA LÓGICA DE FÚRIA ---
    if atacante.hp_atual < 10:
        dano_causado += dano_causado
        print(f"\n 💢 Em fúria! 💢")
    # ----------------------------
```

## Por que fizemos isso?

Usamos:

```python
if atacante.hp_atual < 10
```

para verificar se o personagem está com pouca vida.

Depois:

```python
dano_causado += dano_causado
```

faz o dano ser somado a ele mesmo, dobrando o valor final.

---

# 📊 Desafio 4: Relatório de Danos (Acumuladores)

## O Problema
Queríamos saber quem causou mais dano durante toda a batalha.

## A Solução
Criamos variáveis acumuladoras para armazenar o dano total causado por cada jogador.

## Como ficou o código (na função `simular_batalha`)

```python
# 1. NO COMEÇO DA FUNÇÃO:
dano_total_causado = [0, 0]

# 2. DURANTE O COMBATE:
if tentou_ataque and dano_causado > 0:
    if atacante == p1:
        dano_total_causado[0] += dano_causado
    else:
        dano_total_causado[1] += dano_causado

# 3. NO FINAL DA PARTIDA:
print(f"| Dano total causado por {p1.nome}: {dano_total_causado[0]}")
print(f"| Dano total causado por {p2.nome}: {dano_total_causado[1]}\n")
```

## Por que fizemos isso?

Criamos uma lista:

```python
[0, 0]
```

- Índice `0` → dano do Jogador 1  
- Índice `1` → dano do Jogador 2  

Sempre que um ataque acerta, usamos `+=` para adicionar o dano ao jogador correto.

No final da batalha, basta imprimir os valores acumulados.

---
# 💻 ! Abra o código do monitor e veja as mudanças na íntegra
---
# 🎯 Conclusão

Ficou com alguma dúvida sobre as lógicas aplicadas?

Experimente alterar os valores do sistema, como:
- Vida mínima para ativar a Fúria
- Quantidade de pontos iniciais
- Valor da Classe de Armadura
- Dano das armas

Esses testes ajudam bastante a entender como pequenas mudanças afetam o comportamento do programa.

Bons estudos! 🚀
