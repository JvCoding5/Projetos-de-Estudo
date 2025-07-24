#Esse exercício cria uma calculadora simples que realiza operações básicas de adição, subtração, multiplicação e divisão.


"""Pseudocódigo:
pergunta ao usuário qual operação deseja realizar
1. Solicitar ao usuário a operação desejada (adição, subtração, multiplicação ou divisão)
2. Armazenar a operação em uma variável
3. Solicitar ao usuário o primeiro número
4. Armazenar o primeiro número em uma variável
5. Solicitar ao usuário o segundo número
6. Armazenar o segundo número em uma variável
7. Verificar a operação escolhida
   - Se for adição, calcular a soma dos dois números
   - Se for subtração, calcular a diferença dos dois números
   - Se for multiplicação, calcular o produto dos dois números
   - Se for divisão, verificar se o segundo número é diferente de zero e calcular o quociente
"""

# Tipos de dados comuns em variáveis Python:
# - int: números inteiros (ex: 10, -5, 0)
# - float: números com casas decimais (ex: 3.14, -0.5)
# - str: textos (strings) entre aspas (ex: "Fogo", "Água")
# - bool: valores lógicos True ou False
# - list: listas de valores (ex: ["Fogo", "Água", "Planta"])
# - dict: dicionários com pares chave-valor (ex: {"nome": "Pikachu", "tipo": "Elétrico"})
# - None: valor nulo (sem valor definido)

print("Bem-vindo à calculadora simples!")

# Solicita ao usuário a operação desejada
operacao = input("Escolha a operação (adição, subtração, multiplicação ou divisão):").strip().lower()

#.strip() remove espaços extras no início e no final da string
#.lower() converte a string para minúsculas para facilitar a comparação


# Solicita ao usuário o primeiro número
numero1 = float(input("Digite o primeiro número: "))

# Solicita ao usuário o segundo número
numero2 = float(input("Digite o segundo número: "))

# Verifica a operação escolhida e realiza o cálculo
if operacao == "adição":
    resultado = numero1 + numero2
    print(f"O resultado da adição é: {resultado}")
    
elif operacao == "subtração":
    resultado = numero1 - numero2
    print(f"O resultado da subtração é: {resultado}")
    
elif operacao == "multiplicacão":
    resultado = numero1 * numero2
    print(f"O resultado da multiplicação é: {resultado}")
    
elif operacao == "divisão":
    if numero2 != 0:
        resultado = numero1 / numero2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
        
#O operador "!=" verifica se os valores são diferentes, evitando divisão por zero.