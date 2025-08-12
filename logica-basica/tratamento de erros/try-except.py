"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""


# --- Exemplo utilizando .isdigit para verificar se a STR possui um int---

# numero_str = input("Vou dobrar o número que você digitar: ")

# if numero_str.isdigit():
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_float} é {numero_float * 2}')
    
# else:
#     print('Isso não é um número')




# --- Exemplo utilizando try/except ---

numero_str = input("Vou dobrar o número que você digitar: ")
    
try:
    print('STR: ', numero_str)
    numero_float = float(numero_str) #Conversão explícita da string
    print('FLOAT:', numero_float) 
    print(f'O dobro de {numero_str} é {numero_str * 2}')

except:   
    print('Isso não é um número') # Caso aconteça algum erro no código, como uma conversão
                                  # explícita inválida, int('a'), ele exibe a mensagem
                                  # através do except.                                  