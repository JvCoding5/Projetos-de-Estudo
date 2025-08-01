""" 
Python = "Python é uma linguagem de programação de alto nível, 
interpretada e de tipagem dinâmica. É amplamente utilizada para
desenvolvimento web, automação, análise de dados, inteligência
artificial e muito mais."

Tipo de tipagem = Dinâmica e forte
Isso significa que as variáveis não precisam ser declaradas 
com um tipo específicoe podem ser alteradas durante a execução
do programa. 

E forte significa que o Python não permite operações entre tipos
incompatíveissem uma conversão explícita. Ex: str + int não é permitido.

Str = "String"
Strings = "São sequências de caracteres usadas para representar texto."

Int = "Inteiros"
Inteiros = "Números inteiros, positivos ou negativos, sem casas decimais."
"""

# Aspas simples e duplas são usadas para definir strings
print("Python é uma linguagem de programação.")
print('Python é uma linguagem de programação.')

# Escape de caracteres
print("Python é uma linguagem de programação.\" Ela é muito versátil.\"") #\ é usado para escapar caracteres especiais

#r -> Raw string, onde os caracteres de escape não são processados
print (r"Luiz \"Otávio\"") #r faz com que a string seja interpretada literalmente

"""
Para deixar o código mais legível, podemos utilizar aspas simples e aspas duplas
de forma intercambiável, mas é importante manter a consistência.
# Exemplo:

Print('Python é uma "linguagem" de programação.')

assim não é necessário usar o escape de caracteres, pois as aspas simples
não interferem nas aspas duplas.
"""
#exemplo
print('Python é uma "linguagem" de programação.')