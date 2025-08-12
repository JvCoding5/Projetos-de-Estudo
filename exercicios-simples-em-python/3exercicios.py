# --- Exercício 1 ---

"""
Faça um programa que peça ao usuário para digitar um número interior,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

try:
    
    numero = int(input("Digite um número inteiro: "))
    if numero % 2 == 0:
        print (f"O número {numero} é par ")
    
    else:
        print (f"O número {numero} é ímpar")    
        
except:
    print ("O valor digitado não é um número")
    
    
    

    
# --- Exercício 2 ---

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

horas = int(input("Digite as horas pra mim: "))

try:
        
    if horas >= 0 and horas <= 11:
        print ("Bom dia !!")
            
    if horas >= 12 and horas <= 17:
        print ("Boa Tarde!!")
            
    if horas >= 18 and horas <= 23:
        print ("Boa noite")
        
    else:
        print("Hora inválida.")
        
except:
    print("Isso não é uma hora")




# --- Exercício 3 ---

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 
4 letras ou menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras,
escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input("Digite seu nome: ")
tamanho = len(nome)

if tamanho >= 4:
    print("Seu nome é curto")
    
elif tamanho < 4 and tamanho >= 6:
    print("Seu nome é normal")
    
elif tamanho > 6:
    print("Seu nome é grande")





# --- Exercício 4 ---

"""
Verificar se um letra é maíscula ou minúscula
"""
letra = str(input("Digite uma letra: "))

if letra >= 'A' and letra <= 'Z':
    print("maiuscula")
elif letra >= 'a' and letra <= 'z':
    print("minuscula")
else:
    print("caractere invalido")


numero = int(input("Digite um número inteiro: "))

if numero and 0 == 0:  # Ele compara o ultimo bit do número em binário
    print("par")  # Todo número par, termina em 0 em binário
else: 
    print("impar")
#intervalo: [1, 2, 3, 4, 5, 6]
#aberto: [2, 3, 4, 5]
#fechado: [1, 2, 3, 4, 5, 6]
# crie duas funções, uma para verificar se um numero esta em um intervalo aberto e outra para fechado