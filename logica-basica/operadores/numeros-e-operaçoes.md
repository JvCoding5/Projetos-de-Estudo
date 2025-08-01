# Números e Operações Matemáticas em Python

Python oferece suporte robusto para diferentes tipos de números e uma ampla gama de operações matemáticas. Este guia aborda desde conceitos básicos até funções matemáticas avançadas.

## Tipos de Números

### 1. Inteiros (int)

```python
# Números inteiros
a = 42
b = -15
c = 0

# Números grandes (Python lida automaticamente)
numero_grande = 123456789012345678901234567890
print(type(numero_grande))  # <class 'int'>

# Diferentes bases
binario = 0b1010      # Base 2 (decimal: 10)
octal = 0o12          # Base 8 (decimal: 10)
hexadecimal = 0xA     # Base 16 (decimal: 10)
```

### 2. Números de Ponto Flutuante (float)

```python
# Números decimais
pi = 3.14159
temperatura = -40.5
cientifico = 1.23e-4  # Notação científica (0.000123)

# Precisão limitada
print(0.1 + 0.2)  # 0.30000000000000004 (imprecisão de ponto flutuante)
```

### 3. Números Complexos (complex)

```python
# Números complexos
z1 = 3 + 4j
z2 = complex(2, -1)  # 2 - 1j

# Acessando partes real e imaginária
print(z1.real)  # 3.0
print(z1.imag)  # 4.0

# Operações com números complexos
soma = z1 + z2
print(soma)  # (5+3j)
```

## Operadores Aritméticos Básicos

```python
a = 10
b = 3

# Operações básicas
soma = a + b          # 13
subtracao = a - b     # 7
multiplicacao = a * b # 30
divisao = a / b       # 3.3333333333333335
divisao_inteira = a // b  # 3 (divisão sem resto)
resto = a % b         # 1 (módulo)
potencia = a ** b     # 1000 (10 elevado a 3)

print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao}")
print(f"Divisão inteira: {divisao_inteira}")
print(f"Resto: {resto}")
print(f"Potência: {potencia}")
```

## Operadores de Atribuição

```python
x = 10

x += 5   # x = x + 5  → x = 15
x -= 3   # x = x - 3  → x = 12
x *= 2   # x = x * 2  → x = 24
x /= 4   # x = x / 4  → x = 6.0
x //= 2  # x = x // 2 → x = 3.0
x %= 2   # x = x % 2  → x = 1.0
x **= 3  # x = x ** 3 → x = 1.0

print(f"Valor final de x: {x}")
```

## Funções Matemáticas Básicas

```python
import math

# Funções básicas
print(abs(-5))        # 5 (valor absoluto)
print(round(3.7))     # 4 (arredondamento)
print(round(3.14159, 2))  # 3.14 (2 casas decimais)

# Funções min e max
numeros = [1, 5, 3, 9, 2]
print(min(numeros))   # 1
print(max(numeros))   # 9
print(sum(numeros))   # 20

# Potência e raiz
print(pow(2, 3))      # 8 (2 elevado a 3)
print(math.sqrt(16))  # 4.0 (raiz quadrada)
print(math.pow(2, 3)) # 8.0 (potência usando math)
```

## Módulo Math - Funções Avançadas

```python
import math

# Constantes matemáticas
print(f"Pi: {math.pi}")      # 3.141592653589793
print(f"e: {math.e}")        # 2.718281828459045
print(f"Tau: {math.tau}")    # 6.283185307179586

# Funções trigonométricas (em radianos)
angulo = math.pi / 4  # 45 graus
print(f"sen(45°): {math.sin(angulo)}")  # 0.7071067811865476
print(f"cos(45°): {math.cos(angulo)}")  # 0.7071067811865476
print(f"tan(45°): {math.tan(angulo)}")  # 0.9999999999999999

# Conversão graus ↔ radianos
graus = 90
radianos = math.radians(graus)  # 1.5707963267948966
print(f"90° em radianos: {radianos}")
print(f"π/2 em graus: {math.degrees(math.pi/2)}")  # 90.0

# Funções logarítmicas
print(f"log natural de 10: {math.log(10)}")     # 2.302585092994046
print(f"log base 10 de 100: {math.log10(100)}") # 2.0
print(f"log base 2 de 8: {math.log2(8)}")       # 3.0

# Funções de arredondamento
x = 3.7
print(f"math.floor({x}): {math.floor(x)}")  # 3 (arredonda para baixo)
print(f"math.ceil({x}): {math.ceil(x)}")    # 4 (arredonda para cima)
print(f"math.trunc({x}): {math.trunc(x)}")  # 3 (remove parte decimal)
```

## Módulo Random - Números Aleatórios

```python
import random

# Número aleatório entre 0 e 1
print(random.random())

# Número inteiro aleatório em um intervalo
print(random.randint(1, 10))  # Entre 1 e 10 (inclusive)

# Número float aleatório em um intervalo
print(random.uniform(1.5, 10.5))  # Entre 1.5 e 10.5

# Escolher elemento aleatório de uma lista
cores = ['vermelho', 'azul', 'verde', 'amarelo']
print(random.choice(cores))

# Embaralhar uma lista
numeros = [1, 2, 3, 4, 5]
random.shuffle(numeros)
print(numeros)

# Amostra aleatória sem repetição
print(random.sample(range(1, 51), 6))  # 6 números únicos entre 1 e 50
```

## Conversões entre Tipos

```python
# Conversões básicas
x = 3.8
y = "42"
z = "3.14"

print(int(x))        # 3 (float para int)
print(float(y))      # 42.0 (string para float)
print(int(y))        # 42 (string para int)
print(complex(z))    # (3.14+0j) (string para complex)

# Verificação de tipos
print(isinstance(42, int))      # True
print(isinstance(3.14, float))  # True
print(isinstance(2+3j, complex)) # True
```

## Formatação de Números

```python
numero = 1234567.89

# Formatação básica
print(f"{numero:.2f}")        # 1234567.89 (2 casas decimais)
print(f"{numero:,.2f}")       # 1,234,567.89 (com separador de milhares)
print(f"{numero:e}")          # 1.234568e+06 (notação científica)

# Formatação de porcentagem
taxa = 0.1567
print(f"{taxa:.2%}")          # 15.67%

# Preenchimento com zeros
numero_pequeno = 42
print(f"{numero_pequeno:05d}") # 00042 (5 dígitos com zeros à esquerda)

# Formatação de números binários, octais e hexadecimais
n = 255
print(f"Binário: {n:b}")      # 11111111
print(f"Octal: {n:o}")        # 377
print(f"Hexadecimal: {n:x}")  # ff
print(f"Hexadecimal maiúsculo: {n:X}")  # FF
```

## Operações com Decimal (Precisão Exata)

```python
from decimal import Decimal, getcontext

# Configurar precisão
getcontext().prec = 10

# Usando Decimal para precisão exata
a = Decimal('0.1')
b = Decimal('0.2')
soma = a + b
print(f"Decimal: {soma}")     # 0.3 (precisão exata)

# Comparação com float
print(f"Float: {0.1 + 0.2}")  # 0.30000000000000004

# Operações com Decimal
x = Decimal('10.5')
y = Decimal('3.2')
print(f"Multiplicação: {x * y}")  # 33.60
print(f"Divisão: {x / y}")        # 3.28125
```

## Frações

```python
from fractions import Fraction

# Criando frações
f1 = Fraction(1, 3)      # 1/3
f2 = Fraction(2, 6)      # 2/6 = 1/3 (simplificado automaticamente)
f3 = Fraction('0.25')    # 1/4

print(f"f1: {f1}")       # 1/3
print(f"f2: {f2}")       # 1/3
print(f"f3: {f3}")       # 1/4

# Operações com frações
soma = f1 + f3
print(f"1/3 + 1/4 = {soma}")  # 7/12

# Conversão para decimal
print(f"Decimal: {float(soma)}")  # 0.5833333333333334
```

## Exemplos Práticos

### Calculadora Simples

```python
def calculadora():
    """Calculadora básica com operações fundamentais"""
    print("=== Calculadora Simples ===")
    
    try:
        num1 = float(input("Digite o primeiro número: "))
        operacao = input("Digite a operação (+, -, *, /, **, %): ")
        num2 = float(input("Digite o segundo número: "))
        
        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            if num2 != 0:
                resultado = num1 / num2
            else:
                return "Erro: Divisão por zero!"
        elif operacao == '**':
            resultado = num1 ** num2
        elif operacao == '%':
            if num2 != 0:
                resultado = num1 % num2
            else:
                return "Erro: Divisão por zero!"
        else:
            return "Operação inválida!"
        
        return f"Resultado: {resultado}"
    
    except ValueError:
        return "Erro: Digite apenas números válidos!"

# Exemplo de uso
# print(calculadora())
```

### Conversor de Temperaturas

```python
def converter_temperatura(valor, origem, destino):
    """Converte temperaturas entre Celsius, Fahrenheit e Kelvin"""
    
    # Converter tudo para Celsius primeiro
    if origem.lower() == 'fahrenheit' or origem.lower() == 'f':
        celsius = (valor - 32) * 5/9
    elif origem.lower() == 'kelvin' or origem.lower() == 'k':
        celsius = valor - 273.15
    else:  # origem é Celsius
        celsius = valor
    
    # Converter de Celsius para destino
    if destino.lower() == 'fahrenheit' or destino.lower() == 'f':
        resultado = celsius * 9/5 + 32
    elif destino.lower() == 'kelvin' or destino.lower() == 'k':
        resultado = celsius + 273.15
    else:  # destino é Celsius
        resultado = celsius
    
    return round(resultado, 2)

# Exemplos
print(f"32°F em Celsius: {converter_temperatura(32, 'f', 'c')}°C")  # 0.0°C
print(f"0°C em Kelvin: {converter_temperatura(0, 'c', 'k')}K")      # 273.15K
print(f"100°C em Fahrenheit: {converter_temperatura(100, 'c', 'f')}°F")  # 212.0°F
```

## Dicas e Boas Práticas

1. **Para cálculos financeiros**, use `Decimal` em vez de `float` para evitar erros de precisão
2. **Para operações matemáticas complexas**, importe o módulo `math`
3. **Para números aleatórios criptograficamente seguros**, use o módulo `secrets`
4. **Cuidado com divisão por zero** - sempre verifique antes de dividir
5. **Use f-strings** para formatação de números de forma legível
6. **Para grandes cálculos científicos**, considere usar `numpy` (biblioteca externa)

## Conclusão

Python oferece um sistema numérico robusto e flexível, desde operações básicas até cálculos científicos avançados. O domínio desses conceitos é fundamental para programação eficiente e cálculos precisos.