# --- Interpolação básica de strings ---

# Interpolação básica de strings é o processo de inserir
# valores de variáveis dentro de uma string, de forma
# prática e legível.


"""
Interpolação básica de strings

s- string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 100.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)

# Utilizamos % para definir o tipo da variável na string
# E % (variável, variável) para declarar as variáveis na string

inteiro =300000000000000000

print(variavel)
print('O hexadecimal de %d e %x' % (inteiro, inteiro))

