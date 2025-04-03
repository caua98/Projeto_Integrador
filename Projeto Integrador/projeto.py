#Importação de bibliotecas
from conexeplo import *
controle = "S"
#Conexão do banco de dados
def main():
    connection = connect_to_database()
    if controle == "N":
        connection.close()
#repetição do teste até o fim do usuário
while controle == "S":
    if __name__ == "__main__":
        main()
#Entrada de data do usuário e validação do dado
    try:
        data = int(input("Informe a data de hoje: "))
        while data > 31:
            data = int(input("Data inválida, insira uma data válida: "))
    except ValueError:
        data =int(input("Data inválida, insira uma data válida: "))
    #Entrada de consumo de água e validação do dado
    try:
        consumoagua = float(input("Informe seu consumo de água informado na conta de água(Litros/Dia): "))
        while consumoagua == 0 or consumoagua < 0:
            consumoagua = float(input("Valor inválido, insira um valor válido: "))
    except ValueError:
        consumoagua = float(input("Valor inválido, insira um valor válido: "))

    #Entrada do Lixo Reciclável e validação do dado
    try:
        LixoR = float(input("Informe a porcentagem de lixo reciclável: "))
        while LixoR < 0 or LixoR > 100:
            LixoR = float(input("Valor inválido, insira um valor válido: "))
    except ValueError:
        LixoR = float(input("Valor inválido, insira um valor válido: "))
    
    #Entrada do Lixo Total e validação do dado
    try:
        LixoT = float(input("Informe quantos Kg de lixo total você produz: "))
        while LixoT == 0 or LixoT < 0:
            LixoT = float(input("Valor inválido, insira um valor válido: "))
    except ValueError:
        LixoT = float(input("Valor inválido, insira um valor válido: "))
    
    #Entrada do consumo de energia e validação do dado
    try:
        consumoenergia = float(input("Informe seu consumo de energia informado na sua conta de energia(Kwh/Dia): "))
        while consumoenergia == 0 or consumoenergia < 0:
            consumoenergia = float(input("Valor inválido, insira um valor válido: "))
    except ValueError:
        consumoenergia = float(input("Valor inválido, insira um valor válido: "))
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

    #teste água
    if consumoagua < 150:
        print("Seu consumo de água é de alta sustentabilidade!!!")
    elif consumoagua >= 150 and consumoagua <= 200:
        print("Seu consumo de água é de moderada sustentabilidade!!!")
    elif consumoagua > 250:
        print("Seu consumo de água é de baixa sustentabilidade!!!")
    
    if LixoR >= 50:
        print("Seu consumo de lixo reciclável é de alta sustentabilidade!!!")
    elif LixoR >= 30 and LixoR < 50:
        print("Seu consumo de lixo reciclável é de moderada sustentabilidade!!!")
    elif LixoR < 30:
        print("Seu consumo de lixo reciclável é de baixa sustentabilidade!!!")
    
    #teste energia
    if consumoenergia < 5:
        print("Seu consumo de energia é de alta sustentabilidade!!!")
    elif consumoenergia >= 5 and consumoenergia <= 10:
        print("Seu consumo de energia é de moderada sustentabilidade!!!")
    elif consumoenergia > 10:
        print("Seu consumo de energia é de baixa sustentabilidade!!!")
    
    #teste veículo
    if (bicicleta == "S" or caminhada == "S" or carroE == "S" or transportepublico == "S") and (carroF == "N" and carona == "N"):
        print("Seu uso de transporte é de Alta sustentabilidade")
        op = "Alta sustentabilidade"
    elif (bicicleta == "S" or caminhada == "S" or carroE == "S" or transportepublico == "S") and (carroF == "S" or carona == "S"):
        print("Seu uso de transporte é de Moderada sustentabilidade")
        op = "Moderada sustentabilidade"
    elif (bicicleta == "N" and caminhada == "N" and carroE == "N" and transportepublico == "N") and (carroF == "S" or carona == "S"):
        print("Seu uso de transporte é de Baixa sustentabilidade")
        op = "Baixa sustentabilidade"
    else:
        print("Você não escolheu nenhuma opção de transporte!!!")  

    #inserção dos dados no banco de dados
    if __name__ == "__main__":
        insert_data(consumoagua, LixoR, LixoT, consumoenergia, op)
    #ver se o usuário quer realizar denovo
    controle = input("Quer fazer uma nova consulta?(S / N): ")
    while controle != "S"and controle != "N":
        controle = input("Valor inválido, escolha S ou N: ")