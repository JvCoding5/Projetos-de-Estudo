# --- Operadores Lógicos ---
# Operadores lógicos são usados para combinar expressões booleanas e retornar um valor booleano.

"""
and (e) / or (ou) / not (não)
and - Todas as condições precisam ser verdadeiras.

Se qualquer valor for considerado falso, a expressão inteira 
será avaliada naquele valor.

São considerados falsy os valores 0 e 0.0 '' False

Também existe o tipo None que é usado para representar um não valor
"""

# --- Variáveis ---
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

# --- Operador lógico and ---
if entrada == 'E' and senha_digitada == senha_permitida:
     print('Entrar')
else:
    print('Sair')

# --- Avaliação de curto circuito ---
print(True and False and True) # False porque o segundo valor é False
print(True and 0 and True) # False porque o segundo valor é 0 (falsy)
print(True and ' ' and True) # True porque o espaço em branco é considerado truthy
print(True and True and True) # True porque todos os valores são truthy

""" 
Avaliação de curto circuito é uma característica dos operadores lógicos em Python.
Quando o Python avalia uma expressão lógica, ele para de avaliar assim que encontra um valor que
determina o resultado da expressão.
Por exemplo, em uma expressão com o operador 'and', se um dos valores for falso, o Python não
precisa avaliar os valores restantes, pois o resultado da expressão já será falso.
"""