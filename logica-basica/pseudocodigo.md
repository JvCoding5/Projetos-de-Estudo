# Pseudocódigo

## O que é Pseudocódigo?

O pseudocódigo é uma forma de escrever algoritmos utilizando uma linguagem estruturada, mas que não segue as regras rígidas de sintaxe de uma linguagem de programação específica. É como uma "receita" escrita em linguagem natural, mas organizada de forma lógica e sequencial.

O termo "pseudo" significa "falso" ou "aparente", então pseudocódigo significa "código aparente" - parece código de programação, mas não é executável por um computador. É uma ferramenta intermediária entre o pensamento humano e a programação real.

## Características do Pseudocódigo

### Vantagens
- **Independente de linguagem**: Não está preso a nenhuma sintaxe específica
- **Fácil compreensão**: Usa palavras em português (ou idioma nativo)
- **Foco na lógica**: Permite concentrar-se no algoritmo, não na sintaxe
- **Comunicação**: Facilita a discussão entre programadores e não-programadores
- **Planejamento**: Ajuda a organizar ideias antes de programar

### Desvantagens
- **Não executável**: Precisa ser convertido para uma linguagem real
- **Falta de padronização**: Cada pessoa pode escrever de forma diferente
- **Ambiguidade**: Pode haver interpretações diferentes

## Estrutura Básica do Pseudocódigo

### Formato Geral
```
ALGORITMO <nome_do_algoritmo>
VAR
    // declaração de variáveis
INÍCIO
    // corpo do algoritmo
FIM
```

### Exemplo Simples
```
ALGORITMO SomarDoisNumeros
VAR
    num1, num2, soma: INTEIRO
INÍCIO
    ESCREVA "Digite o primeiro número: "
    LEIA num1
    ESCREVA "Digite o segundo número: "
    LEIA num2
    soma ← num1 + num2
    ESCREVA "A soma é: ", soma
FIM
```

## Elementos Fundamentais

### 1. Declaração de Variáveis
```
VAR
    nome: TEXTO
    idade: INTEIRO
    altura: REAL
    aprovado: LÓGICO
```

**Tipos de dados comuns:**
- `INTEIRO`: números inteiros (1, 42, -10)
- `REAL`: números decimais (3.14, -2.5)
- `TEXTO` ou `CARACTERE`: strings ("João", "Olá")
- `LÓGICO`: verdadeiro ou falso

### 2. Entrada de Dados
```
LEIA variavel
LEIA nome
LEIA "Digite sua idade: ", idade
```

### 3. Saída de Dados
```
ESCREVA "Olá mundo!"
ESCREVA variavel
ESCREVA "Seu nome é: ", nome
ESCREVAL "Texto com quebra de linha"
```

### 4. Atribuição
```
variavel ← valor
nome ← "Maria"
idade ← 25
soma ← a + b
```

## Estruturas de Controle

### 1. Estruturas Condicionais

#### SE/ENTÃO/SENÃO
```
SE (condição) ENTÃO
    // comandos se verdadeiro
SENÃO
    // comandos se falso
FIM SE
```

**Exemplo:**
```
SE (idade >= 18) ENTÃO
    ESCREVA "Maior de idade"
SENÃO
    ESCREVA "Menor de idade"
FIM SE
```

#### SE Aninhado
```
SE (nota >= 9) ENTÃO
    ESCREVA "Excelente"
SENÃO SE (nota >= 7) ENTÃO
    ESCREVA "Bom"
SENÃO SE (nota >= 5) ENTÃO
    ESCREVA "Regular"
SENÃO
    ESCREVA "Insuficiente"
FIM SE
```

#### ESCOLHA/CASO
```
ESCOLHA (variavel)
    CASO valor1:
        // comandos
    CASO valor2:
        // comandos
    CASO CONTRÁRIO:
        // comandos padrão
FIM ESCOLHA
```

**Exemplo:**
```
ESCOLHA (mes)
    CASO 1:
        ESCREVA "Janeiro"
    CASO 2:
        ESCREVA "Fevereiro"
    CASO 3:
        ESCREVA "Março"
    CASO CONTRÁRIO:
        ESCREVA "Mês inválido"
FIM ESCOLHA
```

### 2. Estruturas de Repetição

#### ENQUANTO
```
ENQUANTO (condição) FAÇA
    // comandos a repetir
FIM ENQUANTO
```

**Exemplo:**
```
contador ← 1
ENQUANTO (contador <= 10) FAÇA
    ESCREVA contador
    contador ← contador + 1
FIM ENQUANTO
```

#### PARA
```
PARA variavel DE início ATÉ fim [PASSO incremento] FAÇA
    // comandos a repetir
FIM PARA
```

**Exemplo:**
```
PARA i DE 1 ATÉ 10 FAÇA
    ESCREVA "Número: ", i
FIM PARA

PARA i DE 10 ATÉ 1 PASSO -1 FAÇA
    ESCREVA i
FIM PARA
```

#### REPITA/ATÉ
```
REPITA
    // comandos a executar
ATÉ (condição)
```

**Exemplo:**
```
REPITA
    ESCREVA "Digite um número (0 para sair): "
    LEIA numero
    SE (numero != 0) ENTÃO
        ESCREVA "Você digitou: ", numero
    FIM SE
ATÉ (numero = 0)
```

## Operadores

### Operadores Aritméticos
- `+` (adição)
- `-` (subtração)
- `*` (multiplicação)
- `/` (divisão)
- `%` ou `MOD` (resto da divisão)
- `^` ou `**` (exponenciação)

### Operadores Relacionais
- `=` ou `==` (igual)
- `!=` ou `<>` (diferente)
- `>` (maior que)
- `<` (menor que)
- `>=` (maior ou igual)
- `<=` (menor ou igual)

### Operadores Lógicos
- `E` ou `AND` (e lógico)
- `OU` ou `OR` (ou lógico)
- `NÃO` ou `NOT` (negação)

## Estruturas de Dados

### Vetores (Arrays)
```
VAR
    numeros: VETOR[1..10] DE INTEIRO
    nomes: VETOR[1..5] DE TEXTO

INÍCIO
    numeros[1] ← 10
    numeros[2] ← 20
    
    PARA i DE 1 ATÉ 10 FAÇA
        LEIA numeros[i]
    FIM PARA
FIM
```

### Matrizes
```
VAR
    matriz: MATRIZ[1..3, 1..3] DE INTEIRO

INÍCIO
    PARA i DE 1 ATÉ 3 FAÇA
        PARA j DE 1 ATÉ 3 FAÇA
            LEIA matriz[i, j]
        FIM PARA
    FIM PARA
FIM
```

## Funções e Procedimentos

### Função (retorna valor)
```
FUNÇÃO CalcularArea(base, altura: REAL): REAL
INÍCIO
    RETORNE base * altura / 2
FIM FUNÇÃO
```

### Procedimento (não retorna valor)
```
PROCEDIMENTO MostrarMensagem(msg: TEXTO)
INÍCIO
    ESCREVA "*** ", msg, " ***"
FIM PROCEDIMENTO
```

### Uso de Funções e Procedimentos
```
ALGORITMO Principal
VAR
    b, h, area: REAL
INÍCIO
    MostrarMensagem("Cálculo de Área")
    LEIA b, h
    area ← CalcularArea(b, h)
    ESCREVA "Área: ", area
FIM
```

## Exemplos Práticos

### 1. Verificar Número Par ou Ímpar
```
ALGORITMO ParImpar
VAR
    numero: INTEIRO
INÍCIO
    ESCREVA "Digite um número: "
    LEIA numero
    
    SE (numero % 2 = 0) ENTÃO
        ESCREVA numero, " é par"
    SENÃO
        ESCREVA numero, " é ímpar"
    FIM SE
FIM
```

### 2. Calcular Fatorial
```
ALGORITMO Fatorial
VAR
    n, fatorial, i: INTEIRO
INÍCIO
    ESCREVA "Digite um número: "
    LEIA n
    
    fatorial ← 1
    PARA i DE 1 ATÉ n FAÇA
        fatorial ← fatorial * i
    FIM PARA
    
    ESCREVA "Fatorial de ", n, " é ", fatorial
FIM
```

### 3. Sistema de Notas
```
ALGORITMO SistemaNotas
VAR
    notas: VETOR[1..4] DE REAL
    soma, media: REAL
    i: INTEIRO
INÍCIO
    soma ← 0
    
    PARA i DE 1 ATÉ 4 FAÇA
        ESCREVA "Digite a ", i, "ª nota: "
        LEIA notas[i]
        soma ← soma + notas[i]
    FIM PARA
    
    media ← soma / 4
    
    ESCREVA "Média: ", media
    
    SE (media >= 7) ENTÃO
        ESCREVA "Aprovado"
    SENÃO SE (media >= 5) ENTÃO
        ESCREVA "Recuperação"
    SENÃO
        ESCREVA "Reprovado"
    FIM SE
FIM
```

### 4. Busca em Vetor
```
ALGORITMO BuscarElemento
VAR
    numeros: VETOR[1..10] DE INTEIRO
    busca, i: INTEIRO
    encontrou: LÓGICO
INÍCIO
    // Preencher vetor
    PARA i DE 1 ATÉ 10 FAÇA
        ESCREVA "Digite o ", i, "º número: "
        LEIA numeros[i]
    FIM PARA
    
    ESCREVA "Qual número deseja buscar? "
    LEIA busca
    
    encontrou ← FALSO
    PARA i DE 1 ATÉ 10 FAÇA
        SE (numeros[i] = busca) ENTÃO
            ESCREVA "Número encontrado na posição ", i
            encontrou ← VERDADEIRO
        FIM SE
    FIM PARA
    
    SE (NÃO encontrou) ENTÃO
        ESCREVA "Número não encontrado"
    FIM SE
FIM
```

## Variações de Pseudocódigo

### Estilo Português Estruturado
```
ALGORITMO exemplo
VAR
    x: INTEIRO
INÍCIO
    LEIA x
    SE x > 0 ENTÃO
        ESCREVA "Positivo"
    FIM SE
FIM
```

### Estilo Mais Próximo a Linguagens Reais
```
inicio
    int x
    input x
    if (x > 0) then
        print "Positivo"
    endif
fim
```

### Estilo Narrativo
```
1. Solicitar um número ao usuário
2. Ler o número digitado
3. Se o número for maior que zero:
   3.1. Exibir "Positivo"
4. Fim
```

## Boas Práticas

### 1. Clareza e Legibilidade
- Use nomes descritivos para variáveis
- Mantenha a indentação consistente
- Adicione comentários quando necessário

### 2. Estruturação
- Organize o código em blocos lógicos
- Use estruturas de controle adequadas
- Evite repetição desnecessária de código

### 3. Padronização
- Mantenha um estilo consistente
- Use convenções claras para nomeação
- Documente entradas e saídas

### 4. Exemplo de Bom Pseudocódigo
```
ALGORITMO CalculadoraIMC
VAR
    peso, altura, imc: REAL
    nome: TEXTO
INÍCIO
    // Entrada de dados
    ESCREVA "Digite seu nome: "
    LEIA nome
    ESCREVA "Digite seu peso (kg): "
    LEIA peso
    ESCREVA "Digite sua altura (m): "
    LEIA altura
    
    // Cálculo do IMC
    imc ← peso / (altura * altura)
    
    // Saída de dados
    ESCREVA nome, ", seu IMC é: ", imc
    
    // Classificação
    SE (imc < 18.5) ENTÃO
        ESCREVA "Classificação: Abaixo do peso"
    SENÃO SE (imc < 25) ENTÃO
        ESCREVA "Classificação: Peso normal"
    SENÃO SE (imc < 30) ENTÃO
        ESCREVA "Classificação: Sobrepeso"
    SENÃO
        ESCREVA "Classificação: Obesidade"
    FIM SE
FIM
```

## Ferramentas para Pseudocódigo

### Editores Específicos
- **Visualg**: Popular no Brasil, executa pseudocódigo
- **Portugol Studio**: IDE completa para algoritmos
- **PseInt**: Ferramenta educacional gratuita

### Editores Gerais
- **Notepad++**: Com plugins para destacar sintaxe
- **Visual Studio Code**: Com extensões para pseudocódigo
- **Sublime Text**: Leve e personalizável

## Transição para Linguagens Reais

### Do Pseudocódigo para Python
```
// Pseudocódigo
ALGORITMO exemplo
VAR
    nome: TEXTO
INÍCIO
    LEIA nome
    ESCREVA "Olá, ", nome
FIM

# Python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}")
```

### Do Pseudocódigo para Java
```
// Pseudocódigo
SE (idade >= 18) ENTÃO
    ESCREVA "Maior de idade"
FIM SE

// Java
if (idade >= 18) {
    System.out.println("Maior de idade");
}
```

## Conclusão

O pseudocódigo é uma ferramenta fundamental no aprendizado de programação e no planejamento de algoritmos. Ele serve como uma ponte entre o pensamento lógico humano e a implementação em linguagens de programação específicas.

**Benefícios principais:**
- Desenvolve o raciocínio lógico
- Facilita o planejamento de algoritmos
- Permite comunicação clara entre equipes
- Prepara para qualquer linguagem de programação

**Dica importante:** Pratique bastante com pseudocódigo antes de partir para linguagens específicas. Isso criará uma base sólida que facilitará muito seu aprendizado futuro em programação!