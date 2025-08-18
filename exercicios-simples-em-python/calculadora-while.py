""" 
--- Calculadora com WHile ---

1 - Pede o primeiro número
2 - Pede o segundo número
3 - Pede um operador (Adição, subtração, multiplicação e divisão)
4 - Realiza a operação, e exibe o resultado

"""



try:
    
    while True:
        
            
        # --- Variáveis ---
        num1_float = float(input("Digite o primeiro número"))
        num2_float = float(input("Digite o segundo número"))
        operacoes = "+-/*"
        operacao = input("Digite a operação (+, -, / ou *)")
        
        # --- Validando Informações
        
        if operacao not in operacoes:
            print ("Operação inválida, tente novamente")
            continue
        
        if len(operacao) > 1:
            print("Escolha apenas um operador")
            continue
        
        # --- Realizando a Operação ---
        
        if operacao == "+":
            print("O resultado é ", num1_float + num2_float)
            
        if operacao == "-":
            print("O resultado é ", num1_float - num2_float)
            
        if operacao == "/":
            print("O resultado é ", num1_float / num2_float)
        
        if operacao == "*":
            print("O resultado é ", num1_float * num2_float)
        
        # --- Pergunta se quer sair ---
        sair = input('Quer sair ? [s]im ou [n]ão ').lower().startswith("s")

        if sair is True:
            print("Saindo")
            break

except:
    print("Você deve digitar apenas números válidas")

