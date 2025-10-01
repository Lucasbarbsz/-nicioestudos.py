
           #PROJECTE_MONSTER
#função responsável por criar um monstro de forma genérica:
from random import randint  # randint gera um número aleatório

list_monsters = []

player = {
    'nome': 'Lucas',
    'level': 1,
    'exp': 0,
    'exp_max': 50,
    'hp': 100,
    'hp_max': 100,
    'dano': 25,
}

def create_monster():
    # evita level 0 para não criar monstros com 0 HP
    level = randint(1, 50)  # cria um número aleatório de 1 até 50
    novo_monster = {
        'nome': f'monster #{level}',   # use 'nome' para bater com o resto do código
        'level': level,
        'dano': 5 * level,
        'hp_max': 100 * level,         # hp_max definido
        'hp': 100 * level,             # hp inicial igual ao hp_max
        'exp': 7 * level,
    }
    return novo_monster

def generate_monsters(n_monsters):
    for _ in range(n_monsters):
        novo = create_monster()
        list_monsters.append(novo)

# Gere monstros UMA vez
generate_monsters(5)

# Função para exibir todos os monstros
def exibir_monsters():
    for monster in list_monsters:
        exibir_monster(monster)

# Função para exibir um único monstro
def exibir_monster(monster):
    print(
        f"Nome: {monster['nome']} // Level: {monster['level']} // "
        f"Dano: {monster['dano']} // HP: {monster['hp']}/{monster['hp_max']} // "
        f"EXP: {monster['exp']}"
    )

def exibir_player():
    print(
        f"Nome: {player['nome']} // Level: {player['level']} // "
        f"Dano: {player['dano']} // HP: {player['hp']}/{player['hp_max']} // "
        f"EXP: {player['exp']}/{player['exp_max']}"
    )

def reset_player():
    player["hp"] = player["hp_max"]

def reset_monster(monster):
    monster["hp"] = monster["hp_max"]

def level_up():
    if player["exp"] >= player["exp_max"]:
        player["level"] += 1
        player["exp"] = 0
        player["exp_max"] = player["exp_max"] * 2
        player["hp_max"] += 20
        reset_player()

def iniciar_batalha(monster):
    # garante que monster tem hp atualizado (caso tenha sido usado antes)
    if 'hp' not in monster or 'hp_max' not in monster:
        monster['hp_max'] = monster.get('hp_max', 100 * monster['level'])
        monster['hp'] = monster['hp_max']

    while player["hp"] > 0 and monster["hp"] > 0:
        atacar_monster(monster)
        if monster["hp"] <= 0:
            break
        atacar_player(monster)
        exibir_info_batalha(monster)

    if player["hp"] > 0:
        print(f"O {player['nome']} venceu e ganhou {monster['exp']} de EXP!")
        player["exp"] += monster['exp']
    else:
        print(f"O {monster['nome']} venceu!")
        exibir_monster(monster)

    level_up()
    reset_player()
    reset_monster(monster)

def atacar_monster(monster):
    monster["hp"] -= player["dano"]

def atacar_player(monster):
    player["hp"] -= monster["dano"]

def exibir_info_batalha(monster):
    print(f"Player: {player['hp']}/{player['hp_max']}")
    print(f"Monster: {monster['nome']}: {monster['hp']}/{monster['hp_max']}")
    print("-----------------\n")

# Exemplo de uso
exibir_monsters()
npc_selecionado = list_monsters[0]
iniciar_batalha(npc_selecionado)
exibir_player()
