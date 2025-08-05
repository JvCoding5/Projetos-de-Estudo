# --- Operadores Lógicos ---
# Operadores lógicos são usados para combinar expressões booleanas e retornar um valor booleano.

"""
and (e) / or (ou) / not (não)
or - Se qualquer opção é verdadeira, toda a expressão é avaliada como True

Também existe o tipo None que é usado para representar um não valor
"""


# --- Avaliação de curto circuito ---
print(0 or False or 0 or True) # Retorna true


""" 
Avaliação de curto circuito é uma característica dos operadores lógicos em Python.
Quando o Python avalia uma expressão lógica, ele para de avaliar assim que encontra um valor que
determina o resultado da expressão.
Por exemplo, em uma expressão com o operador 'and', se um dos valores for falso, o Python não
precisa avaliar os valores restantes, pois o resultado da expressão já será falso.
"""