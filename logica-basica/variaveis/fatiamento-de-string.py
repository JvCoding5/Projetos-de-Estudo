"""
Fatiamento de strings em Python

Formato: [início:fim:passo]
- início: índice onde começa o fatiamento
- fim: índice onde termina o fatiamento (não incluso)
- passo: de quantos em quantos caracteres vai andar

Exemplo de índice:
  012345678   → índices positivos
  Olá mundo
 -987654321   → índices negativos

Obs.:
- A função len() retorna a quantidade de caracteres da string.
- Se algum valor for omitido, Python usa os padrões:
  início = 0, fim = len(string), passo = 1
"""

variavel = 'Olá mundo'  # A variável recebe uma string com 9 caracteres

# Fatiamento invertido:
# [::-1] significa:
# - início: não especificado (vai do fim)
# - fim: não especificado (até o início)
# - passo: -1 (de trás pra frente)
print(variavel[::-1])  # Resultado: 'odnum álO'

# Explicação visual:
# String original:  O  l  á     m  u  n  d  o
# Índices:          0  1  2  3  4  5  6  7  8
# Índices (-):     -9 -8 -7 -6 -5 -4 -3 -2 -1
# Resultado invertido pega os caracteres do último ao primeiro
