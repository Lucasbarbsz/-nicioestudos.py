
import pprint

filmsDict = {
    "inception":{
        "yearRelease": 2010,
        "imdbRating": 8.8,
        "genre": ["Sci-fi", "Action", "Thriller"]
    },
    "interstellar":{
        "yearRelease": 2014,
        "imdbRating": 8.6,
        "genre": ["Sci-fi", "Drama"]
    },
    "the dark knight":{
        "yearRelease": 2008,
        "imdbRating": 9.0,
        "genre": ["Action", "Drama", "Crime"]
    }
}
pp = pprint.PrettyPrinter(depth=4)
pp.pprint(filmsDict)

# 1 - Buscar uma informação dentro de um dicionário aninhado
print(filmsDict["interstellar"]["genre"])

# 2 - Adicionar novo item
filmsDict["inception"]["director"] = "Christopher Nolan"
print(filmsDict["inception"])

# 3 - Excluir um dicionário
del filmsDict["the dark knight"]
pp.pprint(filmsDict)

#Exercício:
products = {
    "Arroz": 15.50,
    "Feijão": 8.90,
    "Macarrão": 6.75
}
#Resolução:

#Imprimir o dicionário=
print(products)

#O produto mais caro=
produto_mais_caro = max(products, key=products.get) #vai olhar os valores em vez das chaves.
print(produto_mais_caro)

# A média=
media = sum(products.values()) / len(products)  # pega só os valores (preços)
print(round(media,2)) # Round() retorna apenas o numero de casas decimais que eu quiser

