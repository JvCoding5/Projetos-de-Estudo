"""
Esse é um exemplo de código que demonstra o uso de variáveis e tipos de dados em Python.
Variáveis são usadas para armazenar valores na memória do computador.
PEP8 recomenda iniciar variáveis com letras minúsculas, podendo usar números e underline (_).
O sinal de = é o operador de atribuição, usado para atribuir um valor a uma variável.
"""

# --- Declarando variáveis ---
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
idade = int(input('Digite sua idade: '))
ano_nascimento = int(input('Digite seu ano de nascimento: '))
maior_de_idade = idade >= 18
altura = float(input('Digite sua altura em metros: '))


# --- Exibindo informações ---
print('nome:', nome)
print('Sobrenome:', sobrenome)
print('Idade:', idade)
print('Ano de nascimento:', ano_nascimento)
print('É maior?', maior_de_idade)
print('Altura em metros:', altura)
