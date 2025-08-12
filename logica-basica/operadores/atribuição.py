
"""
Operadores de Atribuição em Python

Os operadores de atribuição são usados para atribuir valores às variáveis.
Além do operador básico '=', Python oferece operadores combinados que facilitam
a atualização do valor da variável com base no valor atual dela.

Operador básico:
=  : Atribui o valor do lado direito à variável do lado esquerdo.

Operadores combinados:
+= : Adiciona o valor do lado direito ao valor atual da variável e atribui o resultado.
-= : Subtrai o valor do lado direito do valor atual da variável e atribui o resultado.
*= : Multiplica o valor atual da variável pelo valor do lado direito e atribui o resultado.
/= : Divide o valor atual da variável pelo valor do lado direito e atribui o resultado.
//=: Divide o valor atual da variável pelo valor do lado direito usando divisão inteira e atribui o resultado.
**=: Eleva o valor atual da variável à potência do valor do lado direito e atribui o resultado.
%=: Calcula o resto da divisão do valor atual da variável pelo valor do lado direito e atribui o resultado.

Exemplos:
"""

# Atribuição simples
x = 10
print(f"x = {x}")  # Saída: x = 10

# Adição e atribuição
x += 5  # Equivalente a: x = x + 5
print(f"x += 5 -> {x}")  # Saída: x += 5 -> 15

# Subtração e atribuição
x -= 3  # Equivalente a: x = x - 3
print(f"x -= 3 -> {x}")  # Saída: x -= 3 -> 12

# Multiplicação e atribuição
x *= 2  # Equivalente a: x = x * 2
print(f"x *= 2 -> {x}")  # Saída: x *= 2 -> 24

# Divisão e atribuição
x /= 4  # Equivalente a: x = x / 4
print(f"x /= 4 -> {x}")  # Saída: x /= 4 -> 6.0

# Divisão inteira e atribuição
x //= 2  # Equivalente a: x = x // 2
print(f"x //= 2 -> {x}")  # Saída: x //= 2 -> 3.0

# Potência e atribuição
x **= 3  # Equivalente a: x = x ** 3
print(f"x **= 3 -> {x}")  # Saída: x **= 3 -> 27.0

# Módulo e atribuição
x %= 5   # Equivalente a: x = x % 5
print(f"x %= 5 -> {x}")  # Saída: x %= 5 -> 2.0
