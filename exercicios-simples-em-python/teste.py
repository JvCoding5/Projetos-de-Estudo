
"""Dividir um número
1. Solicitar ao usuário um número
2. Armazenar o número em uma variável
3. Dividir o número por 2
4. Exibir o resultado da divisão"""

# Tipos de dados comuns em variáveis Python:
# - int: números inteiros (ex: 10, -5, 0)   
# - float: números com casas decimais (ex: 3.14, -0.5)
# - str: textos (strings) entre aspas (ex: "Fogo", "Água")
# - bool: valores lógicos True ou False
# - list: listas de valores (ex: ["Fogo", "Água", "Planta"])
# - dict: dicionários com pares chave-valor (ex: {"nome": "Pikachu", "tipo": "Elétrico"})
# - None: valor nulo (sem valor definido)


#In´ciio do programa

print ("Olá, vamos dividir um número por 2!")

#Solicitando o número ao usuário
numero = float(input("Digite um número:"))

#Dividindo o número por 2
resultado = numero / 2

#Exibindo o resultado
print(f"O resultado da divisão de {numero} por 2 é: {resultado}")