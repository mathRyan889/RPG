import random
from random import randint
from time import sleep
import os

# Inicialização das listas
lista_npc = []
lista_de_narrativas = []
lista_personagens = []
lista_nomes = []

# Funções de utilidade
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def criar_monstro():
    Level = randint(5, 50)
    novo_npc = {
        'nome': f'Monstro #{Level}',
        'level': Level,
        'dano': 5 * Level,
        'hp': 100 * Level,
        'xp_drop': Level * 10  # Experiência que o monstro dá ao ser derrotado
    }
    lista_npc.append(novo_npc)

def gerar_monstros(n_npcs):
    for _ in range(n_npcs):
        criar_monstro()

def criar_personagem():
    Level = randint(1, 60)
    novo_personagem = {
        'level': Level,
        'dano': 5 * Level,
        'hp': 100 * Level,
        'xp': 0,
        'inventario': ['Poção de Vida', 'Espada Básica']
    }
    return novo_personagem

def classes_de_personagens(level):
    if level >= 50:
        return {
            'classe': 'Demônio',
            'poderes': f'Chamas Negras, convocação de demônios menores, Caos com capacidade de {level * 100}',
            'vantagem': level * 8,
            'acrescimo_de_vida': (40 * level) + randint(0, 40),
            'ataque_especial': 'Inferno de Fogo'
        }
    elif level > 30:
        return {
            'classe': 'Feiticeiro',
            'poderes': 'Manipulação de eventos naturais por intermédio de magia',
            'vantagem': level * 20,
            'acrescimo_de_vida': (100 * level) + randint(0, 50),
            'ataque_especial': 'Raio Arcano'
        }
    elif level > 20:
        return {
            'classe': 'Cavaleiro',
            'poderes': f'Maestria com armas nível {level - 3}',
            'vantagem': level * 8,
            'acrescimo_de_vida': (40 * level) + randint(0, 40),
            'ataque_especial': 'Investida Poderosa'
        }
    elif level > 10:
        return {
            'classe': 'Arqueiro',
            'poderes': 'Precisão letal, habilidades com arco e flecha',
            'vantagem': level * 10,
            'acrescimo_de_vida': (30 * level) + randint(0, 30),
            'ataque_especial': 'Flecha Explosiva'
        }
    elif level > 5:
        return {
            'classe': 'Mago',
            'poderes': 'Magias elementais, controle das forças da natureza',
            'vantagem': level * 15,
            'acrescimo_de_vida': (25 * level) + randint(0, 25),
            'ataque_especial': 'Tempestade de Gelo'
        }
    else:
        return {
            'classe': 'Bárbaro',
            'poderes': 'Força bruta, resistência elevada',
            'vantagem': level * 12,
            'acrescimo_de_vida': (50 * level) + randint(0, 50),
            'ataque_especial': 'Golpe Devastador'
        }

def usar_item(personagem):
    if personagem['inventario']:
        print("Itens disponíveis no inventário:")
        for i, item in enumerate(personagem['inventario']):
            print(f"{i + 1}. {item}")
        escolha = int(input("Escolha um item para usar (ou 0 para cancelar): "))
        if escolha > 0 and escolha <= len(personagem['inventario']):
            item = personagem['inventario'][escolha - 1]
            if item == 'Poção de Vida':
                personagem['hp'] += 50
                print("Você usou uma Poção de Vida. HP aumentado em 50.")
            elif item == 'Espada Básica':
                personagem['dano'] += 10
                print("Você usou a Espada Básica. Dano aumentado em 10.")
            personagem['inventario'].remove(item)
        else:
            print("Item inválido ou cancelado.")
    else:
        print("Seu inventário está vazio.")

# Jogo começa aqui
print('-+=' * 30)
print('          RPG PYTHON WORLD')
print('-+=' * 30)

iniciar_jogo = input('Deseja iniciar o jogo? [S/N]: ').strip().upper()
if iniciar_jogo == 'N':
    limpar_tela()
    print('Finalizando jogo...')
    sleep(0.5)
    exit()
else:
    print('Iniciando jogo...')
    sleep(1)
    limpar_tela()

# Geração de NPCs
gerar_monstros(randint(1, 10))

for npc in lista_npc:
    print('-=' * 30)
    print('                      MONSTRO')
    print(f"Nome: {npc['nome']}\nLevel: {npc['level']}\nDano: {npc['dano']}\nHp: {npc['hp']}\nXP ao derrotar: {npc['xp_drop']}")
    sleep(1)

print('-' * 30)
print('Criaturas geradas...')
sleep(2)

# Criação de personagens
print('-=' * 30)
print('               CRIANDO PERSONAGENS')
print('-=' * 30)

while True:
    nome_perso = input('Digite o nome do seu personagem: ').strip().capitalize()
    lista_nomes.append(nome_perso)
    continuar = input('Deseja adicionar mais um personagem? [S/N]: ').strip().upper()
    if continuar == 'N':
        break
    else:
        print(f'Gerando personagem {len(lista_nomes) + 1}')

# Atribuição de classes e atributos aos personagens
for nome in lista_nomes:
    print(f'{nome}')
    personagem = criar_personagem()
    classe_personagem = classes_de_personagens(personagem['level'])
    personagem.update(classe_personagem)
    print(f"Classe: {classe_personagem['classe']}\nPoderes: {classe_personagem['poderes']}")
    print(f"Level: {personagem['level']}\nDano: {personagem['dano']}\nHp: {personagem['hp'] + classe_personagem['acrescimo_de_vida']}\nVantagem de poder: {classe_personagem['vantagem']}")
    atributos = f"Level: {personagem['level']}\nDano: {personagem['dano']}\nHp: {personagem['hp'] + classe_personagem['acrescimo_de_vida']}\nVantagem de poder: {classe_personagem['vantagem']}"
    lista_personagens.append({
        'nome': nome,
        'classe': classe_personagem['classe'],
        'atributos': atributos,
        'personagem': personagem
    })
    
    if nome != lista_nomes[-1]:
        sleep(0.5)
        print('-=' * 30)

# Dinâmica do jogo
lista_de_monstros = ['Goblin', 'Demogorgon', 'Demônio', 'Deus Antigo']
print('--' * 30)
iniciar_dinamica = input('Deseja iniciar a dinâmica do jogo? [S/N]: ').strip().upper()
sleep(1)

npc_selecionado = random.choice(lista_npc)
selacao_da_classe_criaturas = random.choice(lista_de_monstros)

historia01 = f"Você {nome} está caminhando por uma floresta escura com poucos recursos. Você está voltando de uma batalha perdida, desanimado e com pouca energia. Ao longe, você escuta um barulho e vê uma sombra. No meio das vegetações, surge um {selacao_da_classe_criaturas}."
historia02 = f"Você {nome} está caminhando por uma estrada escura com poucos recursos. Você está voltando de uma batalha perdida, desanimado e com pouca energia. Ao longe, você escuta um barulho e vê uma sombra. No meio das vegetações, surge um {selacao_da_classe_criaturas}."

lista_de_narrativas.append(historia01)
lista_de_narrativas.append(historia02)

print('*' * 30)
print('Mestre...')
narrativa_selecionada = random.choice(lista_de_narrativas)
print(narrativa_selecionada)
print('-+=' * 20)
sleep(1)
print('               Atributos do inimigo')
print('-+=' * 20)
print(f"Classe: {selacao_da_classe_criaturas}\nNome: {npc_selecionado['nome']}\nLevel: {npc_selecionado['level']}\nHp: {npc_selecionado['hp']}\nDano: {npc_selecionado['dano']}\nXP ao derrotar: {npc_selecionado['xp_drop']}")

# Função para desfechos baseados nas decisões
def desfecho_combate(acao, resultado, personagem, npc_selecionado):
    if acao == 'A':
        if resultado:
            print(f"Você ataca com força total e consegue derrotar o {npc_selecionado['nome']}.")
            personagem['xp'] += npc_selecionado['xp_drop']
            
        else:
            print(f"Seu ataque não foi forte o suficiente. O {npc_selecionado['nome']} contra-ataca!")
            personagem['hp'] -= npc_selecionado['dano']
            if acao == 'A':
                sorte = randint(0,20)
                print(f'Você ataca {selacao_da_classe_criaturas['nome']} deixando-o com {npc_selecionado['hp']- personagem['dano'*sorte]}')
                if personagem['dano']*sorte > npc_selecionado['hp']:
                    print(f'Seu ataque foi tão brutal e poderoso que o {selacao_da_classe_criaturas['nome']} cai morto no chão.')
    elif acao == 'E':
        if resultado:
            print(f"Você usa sua habilidade especial {personagem['ataque_especial']} e aniquila o {npc_selecionado['nome']}!")
            personagem['xp'] += npc_selecionado['xp_drop']
        else:
            print(f"Sua habilidade especial falhou. O {npc_selecionado['nome']} se aproveita e te ataca!")
            personagem['hp'] -= npc_selecionado['dano']
    elif acao == 'D':
        print(f"Você se defende, reduzindo o dano do ataque do {npc_selecionado['nome']}.")
        personagem['hp'] -= npc_selecionado['dano'] // 2
    elif acao == 'F':
        if resultado:
            print(f"Você conseguiu fugir com sucesso!")
        else:
            print(f"Você tenta fugir, mas o {npc_selecionado['nome']} te alcança e ataca!")
            personagem['hp'] -= npc_selecionado['dano']
    elif acao == 'I':
        print(f"Você usou um item, recuperando {personagem['hp']} pontos de vida.")

def combate(personagem, npc_selecionado):
    while personagem['hp'] > 0 and npc_selecionado['hp'] > 0:
        d20 = randint(1, 20)
        print('Escolha uma ação:')
        print('(A) Atacar')
        print('(E) Usar Habilidade Especial')
        print('(D) Defender')
        print('(F) Fugir')
        print('(I) Usar Item')
        acao = input("Escolha uma ação: ").strip().upper()

        if acao == 'A':
            sucesso = personagem['dano'] * d20 > npc_selecionado['hp']
            desfecho_combate(acao, sucesso, personagem, npc_selecionado)
        elif acao == 'E':
            sucesso = personagem['dano'] * 2 * d20 > npc_selecionado['hp']
            desfecho_combate(acao, sucesso, personagem, npc_selecionado)
        elif acao == 'D':
            desfecho_combate(acao, True, personagem, npc_selecionado)
        elif acao == 'F':
            sucesso = randint(1, 20) > 10
            desfecho_combate(acao, sucesso, personagem, npc_selecionado)
            if sucesso:
                break
        elif acao == 'I':
            usar_item(personagem)
            desfecho_combate(acao, True, personagem, npc_selecionado)
        
        if personagem['hp'] <= 0:
            print(f"Você foi derrotado pelo {npc_selecionado['nome']}.")
            break
        elif npc_selecionado['hp'] <= 0:
            print(f"Você derrotou o {npc_selecionado['nome']} e ganhou {npc_selecionado['xp_drop']} XP!")
            break

# Atributos do personagem antes da luta
print('-+=' * 20)
print('               Seus atributos')
print('-+=' * 20)
sleep(1)

for p in lista_personagens:
    nome = p['nome']
    personagem = p['personagem']
    classe_personagem = classes_de_personagens(personagem['level'])
    print(f"Nome: {nome}\nClasse: {classe_personagem['classe']}\nLevel: {personagem['level']}\nHp: {personagem['hp']}\nDano: {personagem['dano']}")
    sleep(1)

# Combate
combate(personagem, npc_selecionado)

# Finalização do combate
print("Fim da batalha. Verifique os seus atributos.")
for p in lista_personagens:
    print(f"{p['nome']} - Level: {p['personagem']['level']}, XP: {p['personagem']['xp']}, HP: {p['personagem']['hp']}, Inventário: {p['personagem']['inventario']}")
