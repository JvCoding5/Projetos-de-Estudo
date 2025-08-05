# --- Pseudocódigo ---

"""
1. Solicita ao usuário dois valores
2. Armazena os valores em variáveis
3. Compara os valores usando operadores relacionais
4. Exibe o resultado da comparação
"""


# --- Solicitação de valores ---
primeiro_valor = input ('Digite um valor')  #Armazena o primeiro valor
segundo_valor = input ('Digite outro valor') #Armazena o segundo valor

# --- Comparação dos valores ---
if primeiro_valor > segundo_valor:
    print(f"{primeiro_valor} é maior que {segundo_valor}")
    
elif primeiro_valor < segundo_valor:
    print(f"{primeiro_valor} é menor que {segundo_valor}")
    
elif primeiro_valor == segundo_valor:
    print(f'{primeiro_valor} é igual a {segundo_valor}')
    
else: 
    print(f'{primeiro_valor} é diferente de {segundo_valor}')
    
    
