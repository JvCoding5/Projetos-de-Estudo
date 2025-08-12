
"""
Formatação básica de strings
s - string
d - int
f - float
.<número de dígitos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a 
"""

variavel = 'Olá Mundo'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}.')
print(f'{1000.4873648123746:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')
print(f'{variavel!r}') # Mostra a representação oficial do objeto (útil para debug, mostra aspas, \n, etc.)
print(f'{variavel!s}') # Mostra a representação amigável (a padrão quando você imprime algo)
print(f'{variavel!a}') # Igual ao repr(), mas escapa caracteres não-ASCII usando códigos \x, \u, \U