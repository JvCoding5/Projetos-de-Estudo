#Esse exercicio calcula a área de um paralelogramo
# Área do paralelogramo = base * altura
    
"""Pseudocódigo:
1. Solicitar ao usuário a base do paralelogramo
2. Armazenar o valor da base
3. Solicitar ao usuário a altura do paralelogramo
4. Armazenar o valor da altura
5. Calcular a área usando a fórmula: área = base * altura
6. Armazenar o resultada em uma variável
7. Exibir o resultado
"""

# Tipos de dados comuns em variáveis Python:
# - int: números inteiros (ex: 10, -5, 0)
# - float: números com casas decimais (ex: 3.14, -0.5)
# - str: textos (strings) entre aspas (ex: "Fogo", "Água")
# - bool: valores lógicos True ou False
# - list: listas de valores (ex: ["Fogo", "Água", "Planta"])
# - dict: dicionários com pares chave-valor (ex: {"nome": "Pikachu", "tipo": "Elétrico"})
# - None: valor nulo (sem valor definido)


#Início do programa
print("Olá, vamos calcular a área de um paralelogramo!")

#Pedindo o valor da base
print("Escreva o valor da base do paralelogramo:")
base = float(input("Base: "))

#Pedindo o valor da altura
print("Agora, escreva o valor da altura do paralelogramo:") 
altura = float(input("Altura:  "))

# Calculando a área do paralelogramo    
area = base * altura    

#Exibindo o resultado
print(f"A área do paralelogramo é: {area} unidades quadradas.")