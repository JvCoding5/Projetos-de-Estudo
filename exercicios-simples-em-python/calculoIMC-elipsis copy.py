# A fórmula do IMC é: peso / (altura ** 2)
# IMC é a sigla para Índice de Massa Corporal, 
# que é uma medida usada para avaliar se uma pessoa está com peso adequado em relação à sua altura.

# --- Cálculo do IMC ---
peso = int(input('Qual é seu peso?'))  # em kg
altura = float(input('Qual é sua altura?'))  # em metros
imc = peso / (altura ** 2) # Fórmula do IMC

print (int(imc)) # Imprime o IMC como um número inteiro