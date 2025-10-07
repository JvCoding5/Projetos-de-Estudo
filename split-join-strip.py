# string_metodos.py
# Exemplos simples dos métodos strip(), split() e join() no Python

# --- STRIP ---
# strip() remove espaços (ou caracteres específicos) do começo e do fim de uma string

texto = "   Olá, mundo!   "
print("Antes do strip:", repr(texto))
print("Depois do strip:", repr(texto.strip()))

# Você também pode remover caracteres específicos
texto2 = "----Python----"
print("Removendo '-':", texto2.strip('-'))


# --- SPLIT ---
# split() divide uma string em partes (lista), usando um separador

frase = "maçã,banana,laranja"
lista_frutas = frase.split(",")   # divide onde tem vírgula
print("\nResultado do split:", lista_frutas)

# Se não passar nada, o split separa pelos espaços
frase2 = "Python é incrível"
palavras = frase2.split()
print("Split por espaço:", palavras)


# --- JOIN ---
# join() faz o contrário do split: junta os itens de uma lista em uma string

lista = ["maçã", "banana", "laranja"]
texto_junto = ", ".join(lista)   # junta com vírgula e espaço
print("\nUsando join:", texto_junto)

# Outro exemplo — juntar palavras com traço
palavras = ["Python", "é", "divertido"]
print("Com traço:", "-".join(palavras))
