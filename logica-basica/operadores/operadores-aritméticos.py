"""
Aritmético significa que está relacionado a operações matemáticas básicas,
como adição, subtração, multiplicação, divisão, etc. Em programação, 
os operadores aritméticos são usados para realizar cálculos numéricos.
"""

# --- Operadores Aritméticos ---

adicao = 10 + 10 # + faz com que o resultado seja um inteiro
print('Adição:', adicao)

subtracao = 10 -5 # - faz com que o resultado seja um inteiro
print('Subtração:', subtracao)

multiplicacao = 10 * 10 # * faz com que o resultado seja um inteiro
print('Multiplicação:', multiplicacao)

divisao = 10 / 2 # / faz com que o resultado seja um float
print('Divisão:', divisao)

divisao_inteira = 10 // 3 # // faz com que o resultado seja um inteiro
print('Divisao', divisao_inteira)

exponenciacao = 2 ** 3 # ** eleva o primeiro número ao segundo
print('Exponenciação:', exponenciacao)

modulo = 10 % 3 # % retorna o resto da divisão

print('Módulo:', modulo)
if modulo > 0:
    print("O número não é divisível por 3")
else: print("O número é divisível por 3 ")