"""
DEFINIR CONSTANTES (MAGO/GUERREIRO/ARQUEIRO)
Primeiro pede ao usuário para escolher uma classe
cria a variável (Escolha)
escolha = UMA DAS CONSTANTE
Exibir ("Você escolheu {escolha})
criar variavel personagem = escolha
se não exibir "escolha inválida


"""

# --- Classes e Herança ---
class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = self.ataque - alvo.defesa
        if dano < 0:
            dano = 0
        alvo.vida -= dano
        print(f"{self.nome} causou {dano} de dano em {alvo.nome}.")
        print(f"Vida de {alvo.nome}: {alvo.vida}\n")

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=80, ataque=20, defesa=5)

    def atacar(self, alvo):
        dano = int(self.ataque * 1.5) - alvo.defesa
        if dano < 0:
            dano = 0
        alvo.vida -= dano
        print(f"{self.nome} lançou magia causando {dano} de dano em {alvo.nome}.")
        print(f"Vida de {alvo.nome}: {alvo.vida}\n")

class Guerreiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=15, defesa=8)

    def atacar(self, alvo):
        dano = (self.ataque + 5) - alvo.defesa
        if dano < 0:
            dano = 0
        alvo.vida -= dano
        print(f"{self.nome} golpeou causando {dano} de dano em {alvo.nome}.")
        print(f"Vida de {alvo.nome}: {alvo.vida}\n")

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=90, ataque=18, defesa=6)

    def atacar(self, alvo):
        dano = (self.ataque + 3) - alvo.defesa
        if dano < 0:
            dano = 0
        alvo.vida -= dano
        print(f"{self.nome} atirou flecha causando {dano} de dano em {alvo.nome}.")
        print(f"Vida de {alvo.nome}: {alvo.vida}\n")


# --- Função ---
def escolher_classe():
    while True:
        print("Escolha sua classe:")
        print("1 - Mago")
        print("2 - Guerreiro")
        print("3 - Arqueiro")
        escolha = input("Digite o número da classe: ")

        if escolha == '1':
            return Mago("Jogador Mago")
        elif escolha == '2':
            return Guerreiro("Jogador Guerreiro")
        elif escolha == '3':
            return Arqueiro("Jogador Arqueiro")
        else:
            print("Escolha inválida. Tente novamente.\n")

def main():
    jogador = escolher_classe()
    inimigo = Guerreiro("Inimigo Orc")  # Pode criar inimigo fixo ou variar

    print(f"\nVocê escolheu: {jogador.nome}!\n")
    print("Iniciando batalha...\n")

    while jogador.vida > 0 and inimigo.vida > 0:
        jogador.atacar(inimigo)
        if inimigo.vida <= 0:
            print("Inimigo derrotado! Você venceu!")
            break

        inimigo.atacar(jogador)
        if jogador.vida <= 0:
            print("Você foi derrotado! Fim de jogo.")
            break

if __name__ == "__main__":
    main()
