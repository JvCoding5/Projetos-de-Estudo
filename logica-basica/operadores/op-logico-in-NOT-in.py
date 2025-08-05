
# --- Operadores in e not in ---
# 'in' verifica se um valor está presente em uma lista, string, tupla, dicionário, etc.
# 'not in' faz o oposto: verifica se o valor NÃO está presente na estrutura.

"""
Strings são iteráveis

 0  1  2  3  4  5      -> índice positivo
 O  t  á  v  i  o
-6 -5 -4 -3 -2 -1      -> índice negativo

"""

# Definindo a variável
nome = 'Otávio'
 
#Imprimindo a letra no índice da string
print(nome[2]) # [] serve para acessar o índice na string, dentro da variável.
print(nome[-4]) 

print(10 * "-") 

# Checando se uma LETRA está ENTRE as LETRAS de uma STRING
print('á' in nome) # Ele retorna True
print('á' not in nome) # Ele retorna False 
