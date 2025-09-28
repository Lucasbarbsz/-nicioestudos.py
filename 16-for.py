
# Lista de Filmes
moviesList = ["Titanic", "The Godfather", "Inception", "Jurassic Park"]

# 1 - Iterando valores de uma lista
for movie in moviesList:
    print(movie)

# 2 - Quando a condição for atendida, o loop será encerrado
for movie in moviesList:
    if movie == "Inception":
        break
    print(movie)
    
# 3 - Quando a condição for atendida, o loop vai para próxima iteração
for movie in moviesList:
    if movie == "Inception":
        continue
    print(movie)
    
# 4 - Avaliação do filme:
movieName = input("Digite o nome do filme:\n")
movieRating = int(input("Digite quantas avaliações deseja fazer:\n"))

total = 0
for i in range(movieRating):
    note = float(input("Digite a nota para o filme:\n"))
    total += note # "+="Acrescenta um número a cada loop 
    
if movieRating > 0:
    average = total / movieRating
else: 
    average = 0
    
print(f"Média de avaliação do filme {movieName} é: {average:.2f}")

#Exercícios:
Movieslist = ["Batman", "Spider-man", "Jurassicpark"] #Lista
#retirando os itens da lista usando o laço "for":
for movie in Movieslist: #For == Para; In == Em;
    print(movie)

#Repetindo sequência:
for n in range(1,100): #O for vai atribuir cada número dessa sequência à variável "N" a cada volta do laço.
    print(n)










