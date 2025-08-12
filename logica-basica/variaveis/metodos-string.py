


"""
Imutabilidade em Python significa que alguns tipos de dados 
não podem ser alterados depois de criados.

Por exemplo, strings (str), números (int, float), booleanos (bool) 
e tuplas (tuple) são imutáveis.

Se tentarmos modificar uma string, na verdade o Python cria uma nova 
string na memória e a variável passa a apontar para ela,
enquanto a string original permanece intacta.
"""

nome = "Naruto"

# Mesmo que pareça que mudamos a string, na verdade criamos outra
nome = nome.upper()  # Cria uma nova string "NARUTO" e nome passa a apontar para ela
print (nome.upper())


"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""



# Criando uma string base para testes
texto = "  Python é incrível!  "

# --- Modificação de letras ---
print(texto.upper())       # Maiúsculas
print(texto.lower())       # Minúsculas
print(texto.capitalize())  # Primeira letra maiúscula
print(texto.title())       # Primeira letra de cada palavra maiúscula
print(texto.swapcase())    # Inverte maiúsculas e minúsculas

# --- Remover espaços ---
print(texto.strip())   # Remove espaços do início e do fim
print(texto.lstrip())  # Remove espaços da esquerda
print(texto.rstrip())  # Remove espaços da direita

# --- Busca ---
print(texto.find("Python"))   # Retorna índice da primeira ocorrência (ou -1)
print(texto.index("Python"))  # Igual ao find, mas dá erro se não achar
print(texto.count("i"))       # Conta ocorrências
print(texto.startswith("Py")) # Começa com?
print(texto.endswith("!"))    # Termina com?


# --- Substituição ---
print(texto.replace("Python", "JavaScript"))  # Troca palavras


# --- Quebra e junção ---
print(texto.split())  # Quebra em lista de palavras
print("-".join(["Naruto", "Goku", "Luffy"]))  # Junta com separador


# --- Checagem de conteúdo ---
print("123".isdigit())    # Só dígitos?
print("abc".isalpha())    # Só letras?
print("abc123".isalnum()) # Letras e números?
print("python".islower()) # Está toda minúscula?
print("PYTHON".isupper()) # Está toda maiúscula?
print("   ".isspace())    # Só espaços?
print("Konoha".istitle()) # Cada palavra começa maiúscula?


# --- Fatiamento ---
print(texto[2:8])     # Caracteres do índice 2 ao 7
print(texto[::-1])    # Inverte a string
