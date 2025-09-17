"""
Demonstração de cuidados com dados mutáveis em Python.

- Para tipos imutáveis (int, float, str, tuple, bool):
  A atribuição (=) cria uma nova referência para o valor.
  Como esses valores não podem ser alterados, cada variável mantém sua cópia.

- Para tipos mutáveis (list, dict, set):
  A atribuição (=) faz a nova variável apontar para o mesmo objeto na memória.
  Assim, mudanças em uma variável afetam a outra.

- Para evitar esse efeito em listas, podemos usar .copy() ou list()
  para criar uma cópia independente.

Exemplo:

"""

lista_a = ['Luiz', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)