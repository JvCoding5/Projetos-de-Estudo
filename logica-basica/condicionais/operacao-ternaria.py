# Exemplo 1: verificar maioridade
idade = 20
status = "maior de idade" if idade >= 18 else "menor de idade"
print(f"Você é {status}.")

# Exemplo 2: encontrar o maior número
a = 10
b = 20
maior = a if a > b else b
print(f"O maior número é {maior}.")

# Exemplo 3: resultado de aluno
nota = 7.5
resultado = "Aprovado" if nota >= 6 else "Reprovado"
print(f"O aluno está {resultado}.")

# Exemplo 4: ternário aninhado (vários níveis)
nota = 8
conceito = "A" if nota >= 9 else "B" if nota >= 7 else "C"
print(f"Conceito: {conceito}")

# Exemplo 5: dentro de uma função
def calcular_desconto(preco, vip):
    return preco * 0.8 if vip else preco * 0.9

print(f"Preço com desconto (VIP): {calcular_desconto(100, True)}")
print(f"Preço com desconto (Normal): {calcular_desconto(100, False)}")
