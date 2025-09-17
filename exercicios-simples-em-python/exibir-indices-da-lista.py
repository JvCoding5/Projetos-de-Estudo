"""
Exercício
Exiba os índices da lista
0 Maria
1 Helena
2 Luiz
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')
indice = range(len(lista))

for i in indice :
    print ("Indíce: ",i,"Objeto:", lista[indice])