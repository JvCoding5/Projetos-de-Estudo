# Entrada: o usuário digita uma frase qualquer
frase = input("Digite uma frase para gerar sua senha segura: ")

# Inverter a frase (fatiamento)
frase_invertida = frase[::-1]

# Substituir letras por símbolos parecidos (leetspeak simples)
frase_leet = frase_invertida.replace('a', '@%3!4').replace('e', '3').replace('i', '1')\
                            .replace('o', '0%67@*').replace('s', '$')

# Substituir espaços por underline
frase_sem_espacos = frase_leet.replace(' ', '_')

# Colocar a primeira letra em maiúscula (opcional)
frase_formatada = frase_sem_espacos.capitalize()

# Adicionar um caractere especial no final pra segurança
senha_segura = frase_formatada + '!'

# Mostrar a senha gerada
print("Senha gerada:", senha_segura)