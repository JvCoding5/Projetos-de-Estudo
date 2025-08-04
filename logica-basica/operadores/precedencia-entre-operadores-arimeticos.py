
"""
Precedência significa a ordem em que os operadores são avaliados em uma expressão.
Os operadores são avaliados na seguinte ordem:

 1. Parênteses
 2. Exponenciação (**)
 3. Multiplicação, Divisão, Divisão Inteira e Módulo
 4. Adição e Subtração
 
A precedência pode ser alterada usando parênteses para agrupar expressões.


"""

# --- Precedência entre operadores aritméticos ---
conta_1 = 1 + 1 ** (5 + 5)
print(conta_1)  # Resultado: 2

conta_1 = 1 + 1 ** 5 + 5
print(conta_1)  # Resultado: 7

conta_1 = (1 + 1) ** 5 + 5
print(conta_1)  # Resultado: 37