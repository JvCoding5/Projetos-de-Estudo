# Funções em Python - Guia Completo

As funções em Python são blocos de código reutilizáveis que executam uma tarefa específica. Elas são fundamentais para organizar e estruturar seu código de forma eficiente.

## Definindo uma Função

Para criar uma função, use a palavra-chave `def`:

```python
def nome_da_funcao(parametros):
    """Documentação opcional"""
    # código da função
    return valor  # opcional
```

## Exemplo Básico

```python
def saudacao(nome):
    """Função que retorna uma saudação personalizada"""
    return f"Olá, {nome}!"

# Chamando a função
mensagem = saudacao("Maria")
print(mensagem)  # Saída: Olá, Maria!
```

## Tipos de Parâmetros

### Parâmetros obrigatórios

```python
def somar(a, b):
    return a + b

resultado = somar(5, 3)  # 8
```

### Parâmetros com valores padrão

```python
def apresentar(nome, idade=25):
    return f"Eu sou {nome} e tenho {idade} anos"

print(apresentar("João"))        # idade usa valor padrão
print(apresentar("Ana", 30))     # idade especificada
```

### Argumentos posicionais variáveis (*args)

```python
def somar_varios(*numeros):
    return sum(numeros)

print(somar_varios(1, 2, 3, 4, 5))  # 15
```

### Argumentos nomeados variáveis (**kwargs)

```python
def criar_perfil(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

criar_perfil(nome="Pedro", idade=28, cidade="São Paulo")
```

## Escopo de Variáveis

```python
x = 10  # variável global

def minha_funcao():
    x = 20  # variável local
    print(f"Dentro da função: {x}")

minha_funcao()    # Saída: Dentro da função: 20
print(f"Fora da função: {x}")  # Saída: Fora da função: 10
```

## Funções Lambda

Para funções simples de uma linha:

```python
# Função normal
def quadrado(x):
    return x ** 2

# Função lambda equivalente
quadrado_lambda = lambda x: x ** 2

print(quadrado_lambda(5))  # 25

# Uso comum com map, filter, etc.
numeros = [1, 2, 3, 4, 5]
quadrados = list(map(lambda x: x ** 2, numeros))
print(quadrados)  # [1, 4, 9, 16, 25]
```

## Exemplo Prático

```python
def calcular_media(notas):
    """Calcula a média de uma lista de notas"""
    if not notas:  # verifica se a lista não está vazia
        return 0
    return sum(notas) / len(notas)

def classificar_aluno(media):
    """Classifica o aluno baseado na média"""
    if media >= 9:
        return "Excelente"
    elif media >= 7:
        return "Bom"
    elif media >= 5:
        return "Regular"
    else:
        return "Insuficiente"

# Usando as funções
notas_aluno = [8.5, 7.0, 9.2, 6.8]
media = calcular_media(notas_aluno)
classificacao = classificar_aluno(media)

print(f"Média: {media:.1f}")
print(f"Classificação: {classificacao}")
```

## Boas Práticas

- Use nomes descritivos para suas funções
- Mantenha funções focadas em uma única responsabilidade
- Documente suas funções com docstrings
- Evite funções muito longas (idealmente menos de 20 linhas)
- Use type hints quando apropriado:

```python
def multiplicar(a: float, b: float) -> float:
    """Multiplica dois números"""
    return a * b
```

## Conclusão

As funções tornam seu código mais modular, legível e reutilizável, sendo uma das ferramentas mais importantes na programação Python. Elas permitem quebrar problemas complexos em partes menores e mais gerenciáveis, facilitando a manutenção e o teste do código.