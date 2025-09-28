#lista de dicionários:
listjogadores = [
    {'nome': 'lucas' ,'level': 1},
    {'nome': 'mateus' ,'level': 2},
    {'nome': 'gabriel' ,'level': 3},
    {'nome': 'joão' ,'level': 4},

]

for jogador in listjogadores:
    print(f'nome:{jogador['nome']} // level:{jogador['level']}')

           #PROJECTE_MONSTER
#função responsável por criar um monstro de forma genérica:
from random import randint #randint gera um número aleatório

list_monsters = []

def create_monster():
    level = randint(0,50) #cria um número aleatório de 0 até 50
    novo_monster = {
        'name': f'mosnter #{level}',
        'level': level,
        'dano': 5 * level,
        'hp': 100 * level
    }

    list_monsters.append(novo_monster)

def generate_monsters(n_monsters):

    for x in range(n_monsters):
        create_monster()

generate_monsters(2) #gera dois monstros

for monster in list_monsters:
    print(
        f"nome: {monster['name']} // "
        f"level: {monster['level']} // "
        f"dano: {monster['dano']} // "
        f"hp: {monster['hp']}"
    )
