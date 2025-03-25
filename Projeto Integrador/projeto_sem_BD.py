# Código do projeto integrador
controle = "S"

#repetição do teste até o fim do usuário
while controle == "S":
    
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
    print("[1] Bicicleta, transporte público ou elétrico")
    print("[2] Uso misto de transporte público ou privado")
    print("[3] Uso exclusivo de transporte a combustíveis fósseis")
    op = input("Informe o tipo de veículo que você mais utiliza: ")
    while op != "1" and op != "2" and op != "3":
        op = input("Opção inválida, escolha uma opção apresentada: ")

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
    if op == "1":
        print("Seu uso de transporte é de alta sustentabilidade!!!")
    elif op == "2":
        print("Seu uso de transporte é de moderada sustentabilidade!!!")
    elif op == "3":
        print("Seu uso de transporte é de baixa sustentabilidade!!!")

    #ver se o usuário quer realizar denovo
    controle = input("Quer fazer uma nova consulta?(S / N): ")
    while controle != "S"and controle != "N":
        controle = input("Valor inválido, escolha S ou N: ")