import random
import time

class Personagem:
    def __init__(self, nome, atributos):
        self.nome = nome
        self.atributos = atributos
        # Calcula o bônus: a cada 2 pontos, +1 de bônus
        self.bonus = {k: v // 2 for k, v in atributos.items()}
        
        # Status de Combate baseados nos atributos
        self.hp_maximo = 30 + (self.bonus.get("Constituição", 0) * 5)
        self.hp_atual = self.hp_maximo
        self.ca = 10 + self.bonus.get("Destreza", 0) + self.bonus.get("defesa", 0) # add do bonus de defesa
        
        
        self.curas_restantes = 3
        self.sorte_utilizada = False

    def exibir_planilha(self):
        print(f"\n{'='*35}")
        print(f"{'FICHA DE PERSONAGEM':^35}")
        print(f"{'='*35}")
        print(f"Nome: {self.nome}")
        print(f"HP: {self.hp_atual}/{self.hp_maximo}  |  CA (Esquiva): {self.ca}")
        print(f"Curas Restantes: {self.curas_restantes}/3")
        print(f"{'-'*35}")
        print(f"{'Atributo':<15} | {'Pontos':<6} | {'Bônus'}")
        print(f"{'-'*35}")
        for atr, val in self.atributos.items():
            print(f"{atr:<15} | {val:<6} | +{self.bonus[atr]}")
        print(f"{'='*35}\n")

def criar_personagem(num_personagem):
    print(f"\n--- Criação do Personagem {num_personagem} ---")
    nome = input("Digite o nome do personagem: ")
    
    
    atributos = {"Força": 0, "Destreza": 0, "Constituição": 0, "Inteligência": 0, "Sabedoria": 0, "Sorte": 0, "defesa":0} # add de defesa
    pontos_restantes = 20

    print(f"\n-- Você tem {pontos_restantes} pontos para distribuir. --")
    while pontos_restantes!=0: # add de um loop para gastar todos os pontos 
        for atr in atributos.keys():
            while True:
                try:
                    pontos = int(input(f"Pontos em {atr} (Restam {pontos_restantes}): "))
                    if 0 <= pontos <= pontos_restantes:
                        atributos[atr] += pontos # add '+=' para o caso de não ter gastado todos os pontos
                        pontos_restantes -= pontos
                        break
                    else:
                        print(f"Erro: Digite um valor entre 0 e {pontos_restantes}.")
                except ValueError:
                    print("Erro: Digite apenas números inteiros.")
                
            if pontos_restantes==0: break #se já gastou todos os pontos a função acaba (os outros valores já foram inicializados com 0)
        if pontos_restantes!=0: # add de aviso quando ainda restão pontos 
            print(f"\n-- Você ainda tem {pontos_restantes} pontos para distribuir. --")
    return Personagem(nome, atributos)


def simular_batalha(p1, p2):
    dano_total_causado = [0 , 0]
    print("\n" + "#"*40)
    print(f"{' INÍCIO DA BATALHA ':^40}")
    print("#"*40)
    
    # Restaura os status dos personagens caso já tenham lutado antes
    for p in [p1, p2]:
        p.hp_atual = p.hp_maximo
        p.curas_restantes = 3
        p.sorte_utilizada = False
        
    print(f"\n{p1.nome} (HP: {p1.hp_atual}) VS {p2.nome} (HP: {p2.hp_atual})\n")
    
    # Define a ordem baseada na Destreza
    if p2.atributos["Destreza"] > p1.atributos["Destreza"]:
        atacante, defensor = p2, p1
    elif p1.atributos["Destreza"] > p2.atributos["Destreza"]:
        atacante, defensor = p1, p2
    else:
        # Em caso de empate na destreza, sorteia aleatoriamente quem começa
        atacante, defensor = random.sample([p1, p2], 2)
        
    print(f"Iniciativa: {atacante.nome} ataca primeiro!\n")
    time.sleep(1)
    
    turno = 1
    
    while p1.hp_atual > 0 and p2.hp_atual > 0:
        print(f"--- Turno {turno}: {atacante.nome} ---")
        print(f"HP Atual: {atacante.hp_atual}/{atacante.hp_maximo}")
        
        # MENU DE COMBATE
        while True:
            print("\n[ MENU DE AÇÃO ]")
            print("1 - Dano físico (Usa Força)")
            print("2 - Dano mágico (Usa Inteligência)")
            print(f"3 - Curar (Usa Sabedoria) [{atacante.curas_restantes} usos restantes]")
            escolha = input("Escolha sua ação: ")
            
            if escolha in ['1', '2', '3']:
                break
            print("\nErro: Opção inválida! Digite 1, 2 ou 3.")
        
        dano_causado = 0
        tentou_ataque = False
        
        # AÇÃO 1: FÍSICO
        if escolha == '1':
            dado_acerto = random.randint(1, 20)
            if dado_acerto + atacante.bonus["Força"] >= defensor.ca:
                dano_causado = random.randint(1, 10) + atacante.bonus["Força"]
                if atacante.hp_atual <10: # add condição de furia com a vida a baixo de 10 (dobra o dano)
                    dano_causado +=dano_causado
                    print(f"\n 💢 Em fúria! 💢")
                print(f"\n> ⚔️ ACERTO FÍSICO! Você causou {dano_causado} de dano.")
            else:
                print(f"\n> 🛡️ ERROU! A defesa de {defensor.nome} bloqueou o ataque.")
            tentou_ataque = True
            
        # AÇÃO 2: MÁGICO
        elif escolha == '2':
            dado_acerto = random.randint(1, 20)
            if dado_acerto + atacante.bonus["Inteligência"] >= defensor.ca:
                # Magia usa d12 + bonus
                dano_causado = random.randint(1, 12) + atacante.bonus["Inteligência"]
                print(f"\n> ✨ ACERTO MÁGICO! A magia atingiu em cheio, causando {dano_causado} de dano.")
            else:
                print(f"\n> 💨 FALHOU! {defensor.nome} resistiu à magia.")
            tentou_ataque = True
            
        # AÇÃO 3: CURA
        elif escolha == '3':
            if atacante.curas_restantes > 0:
                cura_rolagem = random.randint(1, 6) + atacante.bonus["Sabedoria"]
                hp_antes = atacante.hp_atual
                # min() garante que a vida não passe do hp_maximo
                atacante.hp_atual = min(atacante.hp_maximo, atacante.hp_atual + cura_rolagem)
                curado = atacante.hp_atual - hp_antes
                atacante.curas_restantes -= 1
                
                print(f"\n> 💚 CURA! {atacante.nome} curou {curado} de HP. (HP Atual: {atacante.hp_atual}/{atacante.hp_maximo})")
                print(f"> Restam {atacante.curas_restantes} usos de cura.")
            else:
                print(f"\n> ❌ AÇÃO PERDIDA! {atacante.nome} tentou se curar, mas não tem mais usos de cura!")
        
        time.sleep(1)
        
        # LÓGICA DE APLICAÇÃO DE DANO E TESTE DE SORTE
        if tentou_ataque and dano_causado > 0:
            if atacante == p1: # add soma do dano total
                dano_total_causado[0]+=dano_causado
            else:
                dano_total_causado[1]+=dano_causado

            # Verifica se o dano seria fatal e se a sorte ainda NÃO foi usada
            if defensor.hp_atual - dano_causado <= 0 and not defensor.sorte_utilizada:
                print(f"\n!!! GOLPE FATAL RECEBIDO POR {defensor.nome.upper()} !!!")
                time.sleep(1)
                print(f"Rolando teste de SORTE (Precisa tirar {defensor.atributos['Sorte']}(seu bônus de sorte) ou menos no d20)...")
                
                teste_sorte = random.randint(1, 20)
                time.sleep(1)
                print(f"Dado rolado: {teste_sorte}")
                
                if teste_sorte <= defensor.atributos["Sorte"]:
                    defensor.hp_atual = 1
                    defensor.sorte_utilizada = True
                    print(f"🍀 UM MILAGRE! A Sorte sorriu para {defensor.nome}, que sobreviveu com apenas 1 de HP!")
                else:
                    print("💀 A sorte não foi suficiente...")
                    defensor.hp_atual = 0
            else:
                # Aplica o dano normalmente
                defensor.hp_atual -= dano_causado
                if defensor.hp_atual < 0:
                    defensor.hp_atual = 0
                if defensor.hp_atual > 0:
                    print(f"Status: {defensor.nome} agora tem {defensor.hp_atual} HP restante.")
                    
        time.sleep(1.5)
        print("\n" + "-"*40 + "\n")
        
        # Verifica se alguém morreu antes de passar o turno
        if defensor.hp_atual <= 0:
            break
            
        # Alterna os turnos
        atacante, defensor = defensor, atacante
        turno += 1

    # Fim de Jogo
    vencedor = p1 if p1.hp_atual > 0 else p2
    print("#"*40)
    print(f" {vencedor.nome.upper()} VENCEU A BATALHA! ".center(40, '#'))
    print("#"*40 + "\n")
    print(f"| Dano total causado por {p1.nome}: {dano_total_causado[0]}") # add visualização dos danos totais
    print(f"| Dano total causado por {p2.nome}: {dano_total_causado[1]}\n")
    print("#"*40 + "\n")
    time.sleep(2)



def main():
    p1 = None
    p2 = None
    
    while True:
        print("\n" + "="*30)
        print(" MENU PRINCIPAL ")
        print("="*30)
        print("1 - Criar personagem 1")
        print("2 - Criar personagem 2")
        print("3 - Imprimir personagens criados")
        print("4 - Simular batalha")
        print("5 - Sair do programa")
        
        opcao = input("\nEscolha uma opção: ")
        
        if opcao == '1':
            p1 = criar_personagem(1)
            print(f"\nPersonagem {p1.nome} criado com sucesso!")
            
        elif opcao == '2':
            p2 = criar_personagem(2)
            print(f"\nPersonagem {p2.nome} criado com sucesso!")
            
        elif opcao == '3':
            if p1 is None and p2 is None:
                print("\nNenhum personagem foi criado ainda. Direcionando para a criação do Personagem 1...")
                p1 = criar_personagem(1)
                print(f"\nPersonagem {p1.nome} criado com sucesso!")
            else:
                if p1 is not None:
                    p1.exibir_planilha()
                if p2 is not None:
                    p2.exibir_planilha()
                    
        elif opcao == '4':
            if p1 is not None and p2 is not None:
                simular_batalha(p1, p2)
            else:
                print("\nErro: Você precisa criar os dois personagens para simular uma batalha!")
                
        elif opcao == '5':
            print("\nEncerrando o sistema...")
            break
            
        else:
            print("\nOpção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
