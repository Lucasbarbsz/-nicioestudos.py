
filmMatrix = ["Matrix", 1999, 8.7, True]
print(filmMatrix)

filmsList = ["Inception", "The Shawshank Redemption",
             "The Dark Kgnith", "Pulp Fiction", "Interstellar"]

# 1 - Buscar os dois primeiros itens da lista
print(filmsList[:2])

# 2 - Buscar o último item da lista
print(filmsList[-1])

# 3 - Buscar filmes até uma determinada posição
print(filmsList[:3])

# 4 - Buscar filmes de uma posição em diante
print(filmsList[1:4])

#testes - (LISTAS)
numeros = [5,7,2]
print(numeros)
print(numeros [1])
print(sum(numeros))

a = 'Deus é bom'
b = list(a) #Converte cada letra: List()
print(b)

# Métodos (Join, Split)
palavra = ['deus', 'é', 'bom']
frase = ' '.join(palavra) # as ' ' serve para Juntar palavras com espaço!
print(frase) #.Join -> Concatena

palavra = 'deus é bom'
frase = palavra.split() # .split -> dividi a string
print(frase)

