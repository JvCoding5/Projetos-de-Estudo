# --- Pseudocódigo ---

"""
Primeiro o radar verifica a velocidade do carro no range 99
se velocidade > que limite do radar
exibe "Carro acima da velocidade permitida"
Depois verifica velocidade do carro no range 101
se velocidade > que limite do radar
exibe "carro mutado"

"""

# Constantes = "Variáveis" que não vão mudar
RADAR_1 = 60         # Limite de velocidade do radar
LOCAL_1 = 100        # Posição do radar
RADAR_RANGE = 1      # Alcance do radar (antes e depois)

# Entrada de dados
velocidade = int(input('Digite a velocidade do carro: '))
local_carro = int(input('Digite o local do carro: '))

# Verifica se o carro está no alcance do radar
carro_no_radar = LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE

# Verifica excesso de velocidade
if carro_no_radar and velocidade > RADAR_1:
    print("Carro acima da velocidade permitida!")

# Se passou do radar e estava acima do limite, multar
if local_carro > LOCAL_1 + RADAR_RANGE and velocidade > RADAR_1:
    print("Carro multado!")