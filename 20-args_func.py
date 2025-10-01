# # 1 - Função para imprime um nome completo
# def full_name(first_name, last_name):
#     print(f"Nome é: {first_name} {last_name}")
    
# full_name("Fulano", "Sicrano")
# full_name("João", "Costa")

# # 2 - Função para somar dois números
# def sum_numbers(a, b):
#     return a + b

# print(f"Soma é: {sum_numbers(10, 50)}")

# # 3 - Função com parâmetro default
# def address(country="Brasil"):
#     print(f"Eu moro em: {country}")
    
# address()
# address("Portugal")

# # 4 - Função para avaliar filme
# def rate_movie(num_ratings, movie_name):
#     total = 0
#     for i in range(num_ratings):
#         note = float(input("Digite a nota para o filme:\n"))
#         total += note
    
#     if num_ratings > 0:
#         average = total / num_ratings
#     else:
#         average = 0
        
#     print(f"Média de avaliação do filme: {movie_name} é: {average:.2f}")
    
# rate_movie(2, "Sonic")

def rate_movies():
    # Pergunta quantos filmes serão avaliados
    num_movies = int(input("Quantos filmes deseja avaliar?\n"))
    
    # Lista para guardar os resultados
    resultados = []

    # Loop para cada filme
    for i in range(num_movies):
        movie_name = input("\nDigite o nome do filme:\n")
        num_ratings = int(input(f"Quantas notas para {movie_name}?\n"))

        total = 0
        for j in range(num_ratings):
            note = float(input("Digite a nota para o filme:\n"))
            total += note #soma a nota digitada ao total!

        # Calcula média
        if num_ratings > 0:
            average = total / num_ratings
        else:
            average = 0

        # Salva o resultado
        resultados.append((movie_name, average))

    # Exibe resumo
    print("\n--- Resumo das avaliações ---")
    for movie, avg in resultados:
        print(f"Filme: {movie} | Média: {avg:.2f}")


# Chama a função
rate_movies()



        

