from conexao_final import *

op = "S"
while op == "S":
    print("Escolha uma opção: \n 1 - Inserir dados \n 2 - Alterar dados \n 3 - Apagar dados \n 4 - Consultar dados \n 5 - Consultar Médias \n 6 - Sair")
    op = input("Opção: ")
    if op == "1":
        inserir_dados(None, None, None, None, None, None)
    elif op == "2":
        alterar_dados(None, None, None, None, None, None)
    elif op == "3":
        apagar_dados(None)
    elif op == "4":
        consultar_dados(None)
    elif op == "5":
        consultar_medias(None)
    elif op == "6":
        print("Saindo...")
        op = "N"
    else:
        print("Opção inválida. Tente novamente.")