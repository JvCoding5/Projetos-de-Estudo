# 🧪 Exercício com list comprehension:

""" Criar uma lista com os números de 1 a 100 e guardar apenas os que são pares e divisíveis por 4
    A função range(1, 101) gera os números de 1 a 100
    O operador "%" verifica o resto da divisão
    numero % 2 == 0 → número par
    numero % 4 == 0 → divisível por 4
    "and" exige que as duas condições sejam verdadeiras """

numeros_filtrados = [numero for numero in range(1, 101) if numero % 2 == 0 and numero % 4 == 0]

    # Imprimindo os números que passaram na condição
type(numeros_filtrados)  # Verifica o tipo da variável numeros_filtrados
print(numeros_filtrados)
print(type(numeros_filtrados))  # Verifica o tipo da variável numeros_filtrados


