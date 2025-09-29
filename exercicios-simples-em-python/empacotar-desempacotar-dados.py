
"""
Introdução ao Empacotamento, Desempacotamento e Tuples em Python
================================================================


Empacotamento (Packing)
--------------------------
- Empacotamento ocorre quando vários valores são agrupados em uma única tupla.
- O Python automaticamente "empacota" valores separados por vírgula dentro de uma tupla.
  Exemplo:
      tupla = 10, 20, 30   # empacotamento
      print(tupla)  # (10, 20, 30)

- Também pode ser útil em funções que retornam múltiplos valores:
      def coordenadas():
          return 3, 5
      ponto = coordenadas()  # empacotamento em uma tupla (3, 5)
      
      
Desempacotamento (Unpacking)
-------------------------------
- O desempacotamento permite extrair os valores de uma tupla diretamente em variáveis distintas.
  Exemplo:
      tupla = (10, 20, 30)
      a, b, c = tupla
      print(a, b, c)  # 10 20 30

- Pode-se usar o operador `*` para capturar múltiplos valores:
      tupla = (1, 2, 3, 4, 5)
      a, *b, c = tupla
      print(a)  # 1
      print(b)  # [2, 3, 4]
      print(c)  # 5


"""


# ============== DESEMPACOTAMENTO E EMPACOTAMENTO =================
nome1, nome2, nome3 =['Maria', 'Helena', 'Luiz'] # Uma variável para cada valor da lista
print(nome2)


nome1, *resto =['Maria', 'Helena', 'Luiz']  # Uma variável para o resto dos valores
print(nome1, resto)

nome1, *_ =['Maria', 'Helena', 'Luiz']  # Uma variável que NÃO SERÁ UTILIZADA (_) para o resto dos valores
print(nome1, _ )


# =========================== TUPLE =================================
"""
Tuples
---------
- Uma *tuple* (ou tupla) é uma estrutura de dados imutável em Python, semelhante a uma lista,
  mas que não pode ter seus elementos alterados após a criação.
- São definidas usando parênteses `()` ou simplesmente separando valores por vírgula.
  Exemplo:
      tupla = (1, 2, 3)
      tupla2 = "a", "b", "c"

- Características principais:
  * Imutáveis (não é possível alterar, adicionar ou remover elementos).
  * Podem armazenar diferentes tipos de dados.
  * São frequentemente usadas para representar conjuntos fixos de valores ou para retornos múltiplos de funções.

"""


nomes = "maria", 'Helena', 'Giovana'
# nomes[1] = 'outro'  -> Por ser uma Tupla, o terminal retorna um erro, porque os dados não podem ser alterados.