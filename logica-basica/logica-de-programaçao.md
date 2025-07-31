# Lógica de Programação

## O que é Lógica de Programação?

A lógica de programação é a forma de pensar e organizar ideias de maneira sequencial e estruturada para resolver problemas através de algoritmos. É a base fundamental para o desenvolvimento de software, independente da linguagem de programação utilizada.

Ela envolve a capacidade de **decompor problemas complexos** em partes menores e mais simples, criando uma sequência lógica de passos que, quando executados, levam à solução desejada.

## Por que é Importante?

A lógica de programação é essencial porque:

- **Desenvolve o raciocínio**: Treina o cérebro para pensar de forma analítica e sistemática
- **Base para todas as linguagens**: Os conceitos são universais, aplicáveis em Python, Java, C++, JavaScript, etc.
- **Resolução de problemas**: Ensina a quebrar problemas complexos em etapas menores
- **Eficiência**: Permite criar soluções mais elegantes e otimizadas

## Conceitos Fundamentais

### 1. Algoritmo
Um algoritmo é uma sequência finita de instruções bem definidas para resolver um problema específico.

**Exemplo prático**: Fazer um sanduíche
1. Pegar duas fatias de pão
2. Passar manteiga em uma fatia
3. Colocar o recheio
4. Fechar com a outra fatia
5. Servir

### 2. Variáveis
São espaços na memória do computador onde armazenamos dados que podem ser modificados durante a execução do programa.

**Tipos básicos**:
- **Inteiro**: números sem casa decimal (1, 42, -10)
- **Real/Float**: números com casa decimal (3.14, -2.5)
- **Texto/String**: sequência de caracteres ("João", "Olá mundo")
- **Booleano**: verdadeiro ou falso (true/false)

### 3. Operadores

#### Operadores Aritméticos
- `+` (adição)
- `-` (subtração)  
- `*` (multiplicação)
- `/` (divisão)
- `%` (resto da divisão)

#### Operadores Relacionais
- `==` (igual a)
- `!=` (diferente de)
- `>` (maior que)
- `<` (menor que)
- `>=` (maior ou igual)
- `<=` (menor ou igual)

#### Operadores Lógicos
- `AND` (e): verdadeiro se ambas condições forem verdadeiras
- `OR` (ou): verdadeiro se pelo menos uma condição for verdadeira  
- `NOT` (não): inverte o valor lógico

## Estruturas de Controle

### 1. Estruturas Condicionais

#### SE/ENTÃO/SENÃO (IF/ELSE)
Permite executar diferentes blocos de código baseado em condições.

```
SE (idade >= 18) ENTÃO
    ESCREVA "Maior de idade"
SENÃO
    ESCREVA "Menor de idade"
FIM SE
```

#### ESCOLHA/CASO (SWITCH/CASE)
Útil quando há múltiplas opções baseadas no valor de uma variável.

```
ESCOLHA (dia_semana)
    CASO 1: ESCREVA "Segunda-feira"
    CASO 2: ESCREVA "Terça-feira"
    CASO 3: ESCREVA "Quarta-feira"
    PADRÃO: ESCREVA "Dia inválido"
FIM ESCOLHA
```

### 2. Estruturas de Repetição

#### ENQUANTO (WHILE)
Repete um bloco de código enquanto uma condição for verdadeira.

```
contador = 1
ENQUANTO (contador <= 10) FAÇA
    ESCREVA contador
    contador = contador + 1
FIM ENQUANTO
```

#### PARA (FOR)
Usado quando sabemos quantas vezes queremos repetir algo.

```
PARA i DE 1 ATÉ 10 FAÇA
    ESCREVA i
FIM PARA
```

#### REPITA/ATÉ (DO/WHILE)
Executa o bloco pelo menos uma vez, depois verifica a condição.

```
REPITA
    ESCREVA "Digite um número (0 para sair): "
    LEIA numero
ATÉ (numero == 0)
```

## Estruturas de Dados Básicas

### Arrays/Vetores
Coleção de elementos do mesmo tipo, organizados sequencialmente.

```
numeros = [10, 20, 30, 40, 50]
ESCREVA numeros[0]  // Imprime: 10
```

### Matrizes
Arrays bidimensionais - como uma tabela com linhas e colunas.

```
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
ESCREVA matriz[1][2]  // Imprime: 6
```

## Exemplo Prático: Calculadora de IMC

```
ALGORITMO CalculadoraIMC
INÍCIO
    ESCREVA "=== Calculadora de IMC ==="
    
    ESCREVA "Digite seu peso (kg): "
    LEIA peso
    
    ESCREVA "Digite sua altura (m): "
    LEIA altura
    
    imc = peso / (altura * altura)
    
    ESCREVA "Seu IMC é: ", imc
    
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

## Dicas para Desenvolver a Lógica

### 1. Pratique com Problemas Simples
- Calcule a média de três números
- Verifique se um número é par ou ímpar
- Encontre o maior entre três números

### 2. Use Fluxogramas
Desenhe diagramas que representem visualmente o fluxo do seu algoritmo usando:
- **Oval**: início/fim
- **Retângulo**: processo/ação
- **Losango**: decisão/condição
- **Paralelogramo**: entrada/saída de dados

### 3. Pense Passo a Passo
Antes de programar:
1. Entenda completamente o problema
2. Identifique as entradas necessárias
3. Determine o processamento requerido
4. Defina as saídas esperadas
5. Escreva o algoritmo em linguagem natural
6. Teste mentalmente com diferentes casos

### 4. Pratique Regularmente
A lógica de programação é como um músculo - quanto mais você exercita, mais forte fica. Resolva exercícios diariamente, mesmo que sejam simples.

## Ferramentas para Praticar

- **Visualg**: Ferramenta brasileira para aprender algoritmos
- **Scratch**: Programação visual com blocos
- **Portugol Studio**: IDE para algoritmos em português
- **LeetCode/HackerRank**: Plataformas com desafios de programação
- **URI Online Judge**: Problemas em português

## Próximos Passos

Depois de dominar a lógica de programação, você estará pronto para:

1. **Escolher uma linguagem**: Python, JavaScript, Java, C++, etc.
2. **Aprender paradigmas**: Programação orientada a objetos, funcional
3. **Explorar áreas**: Desenvolvimento web, mobile, inteligência artificial
4. **Praticar projetos**: Construir aplicações reais

## Conclusão

A lógica de programação é a fundação de toda a programação. Dominar esses conceitos fundamentais permitirá que você aprenda qualquer linguagem de programação com mais facilidade e desenvolva soluções eficientes para problemas complexos.

Lembre-se: **programar é uma habilidade que se desenvolve com prática constante**. Seja paciente consigo mesmo e mantenha a consistência nos estudos!