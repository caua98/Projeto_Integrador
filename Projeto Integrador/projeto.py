from conexao import *
from cifra_de_palavra import *
from cifra_num_final import *
controle = "S"
escolha = ""
#Conexão do banco de dados
def main():
    connection = connect_to_database()
    if controle == "N":
        connection.close()
#repetição do teste até o fim do usuário
while controle == "S":
    escolha = input("Escolha uma opção:\n1 - Cadastrar\n2 - Consultar\n")
    while escolha != "1" and escolha != "2":
        escolha = input("Valor inválido, escolha 1 ou 2: ")
    if escolha == "1":
        print("Cadastro")
        if __name__ == "__main__":
            main()
#Entrada de data do usuário e validação do dado
        try:
            data = (input("Informe a data de hoje: "))
            while int(data) > 31:
             data = input("Data inválida, insira uma data válida: ")
        except ValueError:
            data = input("Data inválida, insira uma data válida: ")
        dataC = cifra_cesar(data, key_matrix)
    #Entrada de consumo de água e validação do dado
        try:
            consumoagua = float(input("Informe seu consumo de água informado na conta de água(Litros/Dia): "))
            while consumoagua == 0 or consumoagua < 0:
                consumoagua = float(input("Valor inválido, insira um valor válido: "))
        except ValueError:
            consumoagua = float(input("Valor inválido, insira um valor válido: "))
        consumoaguaC = cifra_cesar(str(consumoagua).replace(".", ""), key_matrix)
    #Entrada do Lixo Reciclável e validação do dado
        try:
            LixoR = float(input("Informe a porcentagem de lixo reciclável: "))
            while LixoR < 0 or LixoR > 100:
                LixoR = float(input("Valor inválido, insira um valor válido: "))
        except ValueError:
            LixoR = float(input("Valor inválido, insira um valor válido: "))
        LixoRC = cifra_cesar(str(LixoR).replace(".", ""), key_matrix)

    
    #Entrada do Lixo Total e validação do dado
        try:
            LixoT = float(input("Informe quantos Kg de lixo total você produz: "))
            while LixoT == 0 or LixoT < 0:
                LixoT = float(input("Valor inválido, insira um valor válido: "))
        except ValueError:
            LixoT = float(input("Valor inválido, insira um valor válido: "))
        LixoTC = cifra_cesar(str(LixoT).replace(".", ""), key_matrix)
    
    #Entrada do consumo de energia e validação do dado
        try:
            consumoenergia = float(input("Informe seu consumo de energia informado na sua conta de energia(Kwh/Dia): "))
            while consumoenergia == 0 or consumoenergia < 0:
                consumoenergia = float(input("Valor inválido, insira um valor válido: "))
        except ValueError:
            consumoenergia = float(input("Valor inválido, insira um valor válido: "))
        consumoenergiaC = cifra_cesar(str(consumoenergia).replace(".", ""), key_matrix)
    #entrada da opção de veículos e validação da opção escolhida
        try:
            bicicleta = input("Você utiliza bicicleta como meio de transporte?(S / N): ")
            while bicicleta != "S" and bicicleta != "N":
                bicicleta = input("Valor inválido, escolha S ou N: ")
        except ValueError:
            bicicleta = input("Valor inválido, escolha S ou N: ")
        try:
            transportepublico = input("Você utiliza transporte público como meio de transporte?(S / N): ")
            while transportepublico != "S" and transportepublico != "N":
                transportepublico = input("Valor inválido, escolha S ou N: ")
        except ValueError:
            transportepublico = input("Valor inválido, escolha S ou N: ")
        try:
            caminhada = input("Você utiliza a caminhada como meio de transporte?(S / N): ")
            while caminhada != "S" and caminhada != "N":
                caminhada = input("Valor inválido, escolha S ou N: ")
        except ValueError:
            caminhada = input("Valor inválido, escolha S ou N: ")
        try:
            carroF = input("Você utiliza carro com combustível fósseis como meio de transporte?(S / N): ")
            while carroF != "S" and carroF != "N":
                carroF = input("Valor inválido, escolha S ou N: ")
        except ValueError:
            carroF = input("Valor inválido, escolha S ou N: ")
        try:
            carroE = input("Você utiliza carro elétrico como meio de transporte?(S / N): ")
            while carroE != "S" and carroE != "N":
                carroE = input("Valor inválido, escolha S ou N: ")
        except ValueError:
            carroE = input("Valor inválido, escolha S ou N: ")
        try:
            carona = input("Você utiliza carona como meio de transporte?(S / N): ")
            while carona != "S" and carona != "N":
                carona = input("Valor inválido, escolha S ou N: ")
        except ValueError:
            carona = input("Valor inválido, escolha S ou N: ")

        if (bicicleta == "S" or caminhada == "S" or carroE == "S" or transportepublico == "S") and (carroF == "N" and carona == "N"):
            op = "ALTA"
        elif (bicicleta == "S" or caminhada == "S" or carroE == "S" or transportepublico == "S") and (carroF == "S" or carona == "S"):
            op = "MODERADA"
        elif (bicicleta == "N" and caminhada == "N" and carroE == "N" and transportepublico == "N") and (carroF == "S" or carona == "S"):
            op = "BAIXA"
        else:
            op = "NA"
        opC = cifra_palavra(op, key_matrix)
        #inserção dos dados no banco de dados
        if __name__ == "__main__":
            insert_data(consumoagua, LixoR, LixoT, consumoenergia, op, data)

    if escolha == "2":     
        try:
            data = int(input("Informe uma data para consultar: "))
            while int(data) > 31:
                data = int(input("Data inválida, insira uma data válida: "))
        except ValueError:
            data = int(input("Data inválida, insira uma data válida: "))
        dataC = cifra_cesar(str(data), key_matrix)
        fetch_averages_by_date(data)
    #ver se o usuário quer realizar denovo
    controle = input("Quer fazer uma nova consulta?(S / N): ")
    while controle != "S"and controle != "N":
        controle = input("Valor inválido, escolha S ou N: ")