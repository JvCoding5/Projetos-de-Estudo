"""
Listas em Python
Tipo list - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento


Métodos úteis:
    append - Adiciona um item ao final
    insert - Adiciona um item no índice escolhido
    pop - Remove do final ou do índice escolhido
    del - apaga um índice
    clear - limpa a lista
    extend - estende a lista
    + - concatena listas
    
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD)
"""
#        0   1   2   3   4   5
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2]
# print(lista)
# print(lista[2])
lista.append(50)
lista.pop()
lista.append(60)
lista.append(70)
ultimo_valor = lista.pop(3)
print(lista, 'Removido,', ultimo_valor)




animes_assistidos = ["Boku no Hero", "One piece", "Solo leveling", "VinlandSaga", "Dragon Ball", "Hajime no Hippo" \
            "Baki", "Shuumatsu no Valkyre", "Demon Slayer", "Frieren", "Blue Lock", "Black Clover", "Tower of god", "Kaiju no 8"]

animes_assistidos.pop()
animes_assistidos.append("Viral Hit")
print (animes_assistidos)