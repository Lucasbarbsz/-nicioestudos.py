#Informações sobre o filme
name = input("Digite o nome do filme:\n")
yearRelease = int(input("Digite o ano de lançamento:\n"))
rating = float(input("Digite a nota de avaliação do filme:\n"))

# Verifica se o filme é recomendado
if rating > 8.0 and yearRelease > 2015:
    print(f"O filme {name} é muito bom. Recomendo assisti-lo.")
else:
    print(f"O filme {name} ainda não atingiu uma boa nota.")
    
num1 = float(input("Digite o primeiro número:\n"))
num2 = float(input("Digite o segundo número:\n"))
operation = input("Digite a operação a ser realizada: (+ - * /)\n")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Erro: Divisão por Zero")
        result = 0
else: 
    print("Operação inválida")
    result = 0
    
print(f"Resultado da operação é: {result:.2f}")

# Exercício de casa:
#Crie um programa que pergunte a idade de uma pessoa e classifique-a em categorias:

# Se tiver menos de 12 anos → exibir "Criança"

# Se tiver entre 12 e 17 anos → exibir "Adolescente"

# Se tiver entre 18 e 59 anos → exibir "Adulto"

# Se tiver 60 anos ou mais → exibir "Idoso"

idade = int(input('Qual a sua idade ?\n'))
if idade < 12:
    print('Criança')
elif 12 <= idade <=17:
    print("Adolescente")
elif 18 <= idade <= 59:
    print('Adulto')
else:
    print('Idoso')
