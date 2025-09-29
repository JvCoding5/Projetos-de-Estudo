"""
enumerate - enumera iteráveis (índices)
Uma função e iterador (percorre um iterável, e lembra a posição[i])
"""

lista= ["Maria", "Helena", "Luiz"]
lista.append("João")

lista_enumerada = enumerate(lista)
print(next(lista_enumerada))
print(next(lista_enumerada))

print (list(enumerate(lista)))