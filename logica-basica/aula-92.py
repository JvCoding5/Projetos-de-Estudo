# ------------------------------------------
# IMPRECISÃO DE PONTO FLUTUANTE EM PYTHON
# ------------------------------------------

# Quando usamos floats, o computador trabalha com base binária.
# Alguns números decimais (como 0.1 e 0.2) não têm representação exata em binário.
# Isso causa pequenas diferenças no resultado.

print("=== PROBLEMA ORIGINAL ===")
a = 0.1 + 0.2
print("0.1 + 0.2 =", a)  # 0.30000000000000004

# ------------------------------------------
# 1️⃣ USANDO decimal.Decimal -> CORRIGE DE VERDADE
# ------------------------------------------

from decimal import Decimal, getcontext

# Define a precisão decimal (quantos dígitos o Decimal guarda)
getcontext().prec = 10

# Passe os valores como STRINGS — isso é importante!
x = Decimal('0.1')
y = Decimal('0.2')
z = x + y

print("\n=== USANDO DECIMAL ===")
print("0.1 + 0.2 =", z)  # 0.3 exato
print("Tipo:", type(z))  # <class 'decimal.Decimal'>

# Decimal é ótimo para cálculos financeiros e científicos
preco1 = Decimal('0.10')
preco2 = Decimal('0.20')
total = preco1 + preco2
print("Total exato com Decimal (dinheiro):", total)

# ------------------------------------------
# 2️⃣ USANDO round() -> NÃO CORRIGE, MAS ARREDONDA
# ------------------------------------------

b = 0.1 + 0.2
print("\n=== USANDO ROUND() ===")
print("Valor original:", b)
print("Arredondado para 2 casas:", round(b, 2))  # 0.3

# round() apenas arredonda visualmente, o valor interno ainda tem imprecisão.

# ------------------------------------------
# 3️⃣ USANDO FORMATAÇÃO :.xf -> SÓ MUDA A EXIBIÇÃO
# ------------------------------------------

c = 0.1 + 0.2
print("\n=== USANDO FORMATAÇÃO ===")
print("Com format():", "{:.2f}".format(c))  # "0.30"
print(f"Com f-string: {c:.2f}")              # "0.30"

# :.2f apenas formata o número como string com 2 casas decimais.
# O valor interno continua impreciso.

# ------------------------------------------
# COMPARAÇÃO FINAL
# ------------------------------------------
print("\n=== COMPARAÇÃO FINAL ===")
print(f"Float original -> {a}")
print(f"Decimal        -> {z}")
print(f"Round()        -> {round(b, 2)}")
print(f"Formatação     -> {c:.2f}")



