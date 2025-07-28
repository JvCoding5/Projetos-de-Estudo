# Este programa compara o tipo do seu Pokémon com o tipo do oponente
# e diz se o seu ataque será super eficaz, pouco eficaz ou neutro.




"""Pseudocódigo:
1. Solicitar ao jogador o tipo do Pokémon adversário (Fogo, Água ou Planta)
2. Armazenar o tipo digitado, removendo espaços e padronizando com a primeira letra maiúscula
3. Verificar se o tipo do adversário é válido (Fogo, Água ou Planta)
    → Se for inválido, exibir mensagem de erro e encerrar o programa

4. Solicitar ao jogador o tipo do seu próprio Pokémon (Fogo, Água ou Planta)
5. Armazenar o tipo digitado, também formatado corretamente

6. Verificar o tipo do Pokémon do jogador:
    - Se for Fogo:
        → Contra Planta: ataque é super eficaz
        → Contra Fogo ou Água: ataque é pouco eficaz
    - Se for Planta:
       → Contra Água: ataque é super eficaz
        → Contra Fogo ou Planta: ataque é pouco eficaz
    - Se for Água:
        → Contra Fogo: ataque é super eficaz
       → Contra Água ou Planta: ataque é pouco eficaz

7. Se o tipo do Pokémon do jogador for inválido, exibir mensagem de erro"""

# Solicita ao jogador o tipo do Pokémon adversário
tipo_adversario = input("Jogador, informe o tipo do Pokémon adversário (Fogo, Água ou Planta): ").strip().capitalize()

if tipo_adversario not in ["Fogo", "Água", "Planta"]:   
    print("Tipo do Pokémon adversário inválido.")
    exit()



# Solicita ao jogador o tipo do seu próprio Pokémon
tipo_aliado = input("Jogador, informe o tipo do seu Pokémon (Fogo, Água ou Planta): ").strip().capitalize()




# Verifica o tipo do Pokémon aliado
if tipo_aliado == "Fogo":
    # Se o tipo do adversário for Planta, o ataque é super eficaz
    if tipo_adversario == "Planta":
        print("Seu ataque foi super eficaz!")
    # Se for Fogo ou Água, o ataque é pouco eficaz
    elif tipo_adversario == "Fogo" or tipo_adversario == "Água":
        print("Seu ataque foi pouco eficaz.")
    else:
        print("Ataque neutro.")

elif tipo_aliado == "Planta":
    if tipo_adversario == "Água":
        print("Seu ataque foi super eficaz!")
    elif tipo_adversario == "Fogo" or tipo_adversario == "Planta":
        print("Seu ataque foi pouco eficaz.")
    else:
        print("Ataque neutro.")

elif tipo_aliado == "Água":
    if tipo_adversario == "Fogo":
        print("Seu ataque foi super eficaz!")
    elif tipo_adversario == "Água" or tipo_adversario == "Planta":
        print("Seu ataque foi pouco eficaz.")
    else:
        print("Ataque neutro.")

else:
    # Caso o tipo do Pokémon aliado não seja reconhecido
    if tipo_aliado not in ["Fogo", "Água", "Planta"]:
        print("Tipo do seu Pokémon inválido.")
