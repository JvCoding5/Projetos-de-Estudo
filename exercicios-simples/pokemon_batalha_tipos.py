# Este programa compara o tipo do seu Pokémon com o tipo do oponente
# e diz se o seu ataque será super eficaz, pouco eficaz ou neutro.

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
