# Aprendendo Python

print("Olá Mundo")
print("Aprendendo a Linguagem Python")
"""
    Python é muito
    divertido
"""

#Dentro do input todos os dados são Strings
nome = (input('qual o seu nome:\n')) #\n quebra a linha
altura = input('qual a sua altura:\n')
print(type(nome))
print(type(altura))

#convertendo dados tipo string -> float
nome = (input('qual o seu nome:\n')) #\n quebra a linha
altura = float(input('qual a sua altura:\n'))
print(type(nome))
print(type(altura))

#Exercício para retornar cumprimento:
nome = input('qual o seu nome:\n')
print(f"Olá, {nome}!")