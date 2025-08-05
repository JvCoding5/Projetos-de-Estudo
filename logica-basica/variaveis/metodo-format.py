#--- Método format ---

"""
O método `format` é uma forma de formatar strings em Python,
permitindo incluir placeholders `{}` que serão substituídos 
por valores especificados.  
"""


# Definindo variáveis
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

# --- Definindo a string com placeholders ---


# Os placeholders são definidos com chaves `{}` e podem ser preenchidos com valores
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'


# O método format substitui os placeholders pelos valores correspondentes
formato = string.format(nome1=a, nome2=b, nome3=c)
print(formato)


#---- Utilizando índices nos placeholders ---
# É possível usar índices para referenciar os valores na ordem em que foram passados
a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

string = 'b={1} a={0} a={0} c={2:.2f}'
formato = string.format(a, b, c)

print(formato) # Saída: b=BBBBBB a=AAAAA a=AAAAA c=1.10

