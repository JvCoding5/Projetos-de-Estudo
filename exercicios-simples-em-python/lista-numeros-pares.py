# Exercício: Criar uma lista com números de 1 a 100 e imprimir apenas os números pares que são divisíveis por 4.
    # Criamos uma lista com os números de 1 até 100 usando a função range(x, y)

"""primeiro criamos uma lista com números de 1 a 100
depois, usamos um loop for para percorrer cad número da lista
e verificamos se ele é par e divisível por 4."""

# A função range(1, 101) gera números de 1 até 100 (o 101 não é incluído)
numeros = list(range(1, 101))  # "=" é o operador de atribuição (atribui o valor à variável 'numeros')


# Iniciamos um loop for para percorrer cada número da lista
for numero in numeros:
    
    # "%" é o operador de módulo (ou resto da divisão)
    # numero % 2 == 0 → verifica se o número é par (divisível por 2, ou seja, sem resto)
    # numero % 4 == 0 → verifica se o número é divisível por 4 (sem resto)
    # "and" é o operador lógico E → ambas as condições devem ser verdadeiras 
    
    if numero % 2 == 0 and numero % 4 == 0:
        # Se as duas condições forem verdadeiras, imprime o número
        print(numero)
        
