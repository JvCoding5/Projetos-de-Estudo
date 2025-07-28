#Esse é um exercício simples que implementa o algoritmo Bubble Sort para ordenar uma lista de números.
    # A cada passagem, o maior elemento "flutua" para o final do array, como uma bolha, dando nome ao.

"""Pseudocódigo: 
Inicio

para cada elemento i no array de tamanho n
    para cada elemento j no array de tamanho n - 1
    se elemento i for maior que elemento j
        troque os elementos i e j
Exiba o array ordenado

Fim
"""

# Tipos de dados comuns em variáveis Python:
# - int: números inteiros (ex: 10, -5, 0)   
# - float: números com casas decimais (ex: 3.14, -0.5)
# - str: textos (strings) entre aspas (ex: "Fogo", "Água")
# - bool: valores lógicos True ou False
# - list: listas de valores (ex: ["Fogo", "Água", "Planta"])

#Lista de números a serem ordenados

lista = [64, 34, 25, 12, 22, 11, 90, 30, 45, 78, 56, 89, 23, 67, 88, 99, 100]


# Em Python, def é uma palavra reservada usada para definir funções.
def bubble_sort(arr):   
    n = len(arr)                        # Obtém o tamanho da lista
    for i in range(n):                  # Loop para cada elemento na lista (17 números)
        for j in range(0, n-i-1):       # Loop para comparar elementos adjacentes ()
            
                                        # Troca se o elemento encontrado for maior que o próximo
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Troca os elementos




