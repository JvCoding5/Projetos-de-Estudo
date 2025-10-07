# format_exemplos.py
# Demonstração simples do método .format() no Python

# Exemplo 1 — básico
nome = "Ana"
idade = 25
print("Meu nome é {} e eu tenho {} anos.".format(nome, idade))

# Exemplo 2 — usando posições
print("{1} tem {0} anos.".format(25, "Ana"))

# Exemplo 3 — usando nomes
print("Meu nome é {nome} e tenho {idade} anos.".format(nome="Ana", idade=25))

# Exemplo 4 — formatando números
valor = 1234.5678
print("Valor formatado: {:.2f}".format(valor))   # 2 casas decimais
print("Valor formatado: {:.0f}".format(valor))   # sem casas decimais (arredonda)

# Exemplo 5 — alinhamento e espaçamento
# {:>10} → alinha à direita com largura 10
# {:<10} → alinha à esquerda com largura 10
# {:^10} → centraliza com largura 10
palavra = "Python"
print("Direita : {:>10}".format(palavra))
print("Esquerda: {:<10}".format(palavra))
print("Centro  : {:^10}".format(palavra))

# Exemplo 6 — comparação com f-string (forma moderna)
print(f"Meu nome é {nome} e eu tenho {idade} anos (usando f-string).")
