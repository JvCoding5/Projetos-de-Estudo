"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permite que o programa quebre com erros de índices inexistenes na lista.
"""


#F========== Funções & Variáveis ==========

lista = []
opcoes= ("A","D", "L")


def adicionar ():
    produto_novo = (input("Digite o nome do produto"))
    lista.append(produto_novo)
    print(f"{produto_novo} foi adicionado com sucesso!")

def deletar ():
    produto_deletado = (input("Digite o produto que você quer deletar"))
    if produto_deletado in lista :
        lista.remove(produto_deletado)
        print(f"{produto_deletado} deletado com sucesso!!")
    else: 
        print(f"{produto_deletado} não está na lista")

    
def listar (): 
    print ("Produtos na lista:" ) ;
    for i, produto in enumerate(lista, start=1):
        print(f"{i}. {produto}")


# ========= Corpo do Código ===========#

while True:
    
    try:     
        escolha = str(input("Escolha entre:\n [A]dicionar\n [D]eletar\n [L]istar\n ")).upper()

        if escolha in opcoes :
        
            if escolha == "A" :
                adicionar()
                
            elif escolha == "D" :
                deletar()
                
            elif escolha == "L" :
                listar()
                
    except:
        print("Está não é uma das opções, tente novameente")
