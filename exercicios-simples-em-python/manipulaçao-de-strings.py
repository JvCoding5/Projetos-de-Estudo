import sys

"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
    
"""

#Variaveis
nome = None
idade = None

nome = (input("Digite o seu nome "))
idade = (input("Agora digite sua idade "))

# nome && idade != None
if nome and idade is not None:
    print("Leitura passou")
else:
    print("Desculpe, você deixou campos vazios")
    sys.exit(0)

# Exibe nome && nome invertido
print(f"Seu nome é {nome}")
print(f"Seu nome invertido é {nome[::-1]}")

# Exibe se nome tem espaços
quantidade_espaços = nome.count(" ")

if " " in nome:
    print("seu nome contém espaço")
else:
    print("Seu nome não contém espaço")


# Exibe qtd. letras em nome && 1° letra em nome && ùltima letra em nome
quantidade_de_letras = len(nome) 

print(f"Seu nome tem {quantidade_de_letras} letras")
print(f"A primeira letra do seu nome é {nome[0]}")
print(f"A última letra do seu nome é {nome[-1]}")

