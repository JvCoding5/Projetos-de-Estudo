"""
F string é uma forma de formatar strings em Python,
permitindo incluir expressões dentro de chaves `{}` que serão avaliadas em tempo de execução.

"""

# --- F-strings ---

nome = str(input('Qual é seu nome? '))
peso = int(input('Qual é seu peso?'))  # em kg
altura = float(input('Qual é sua altura?'))  # em metros
imc = (peso / (altura ** 2)) # Fórmula do IMC

linha_1 = f'{nome} tem {altura} de altura, e pesa {peso}, portanto seu IMC é {imc:.2f}'
# O :.2f formata o IMC para duas casas decimais

print(linha_1)  # Imprime a linha formatada com os valores de nome, altura, peso e IMC



