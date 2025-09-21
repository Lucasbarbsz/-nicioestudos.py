
filmsSet = {"Inception", "The Shawshank Redemption",
             "The Dark Kgnith", "Pulp Fiction", "Interstellar"}

print(type(filmsSet))

# 1 - Buscar o tamanho do set
print(len(filmsSet))

# 2 - True e 1 são considerados o mesmo valor
exampleSet = {"Inception", True, 1, 8.7}
print(exampleSet)

# 3 - Adicionar item de outro set
filmsSet.update(exampleSet)
print(filmsSet)

# 4 - Remover um item no set
filmsSet.remove(True)
filmsSet.remove(8.7)
print(filmsSet)

# adicionando item ao final da lista (Append)
lista = [1,2,3,4]
lista.append(5)
print(lista)

meuset = {1,2,3,4} # O set em Python é uma estrutura de dados que representa um conjunto.
meuset.add(5) #.add tmb adiciona ao final.
print(type(meuset))
