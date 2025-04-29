import mysql.connector
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user= 'root',
            password= '',
            database= 'sustentabilidade'
        )
        if connection.is_connected():
            print("Conectado ao banco de dados")
            return connection
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None
    
def inserir_dados():
    conn = connect_to_database(consumoagua, LixoR, LixoT, consumoenergia, op, data)
    consumoagua = float(input("Informe seu consumo de água informado na conta de água(Litros/Dia): "))
    LixoR = float(input("Informe a porcentagem de lixo reciclável: "))
    LixoT = float(input("Informe quantos Kg de lixo total você produz: "))
    consumoenergia = float(input("Informe seu consumo de energia informado na sua conta de energia(Kwh/Dia): "))
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
        op = "Alta sustentabilidade"
    elif (bicicleta == "S" or caminhada == "S" or carroE == "S" or transportepublico == "S") and (carroF == "S" or carona == "S"):
        op = "Media sustentabilidade"
    elif (bicicleta == "N" and caminhada == "N" and carroE == "N" and transportepublico == "N") and (carroF == "S" or carona == "S"):
        op = "Baixa sustentabilidade"
    else:
        op = None
    data = int(input("Informe a data de hoje: "))
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_sustentavel (
            consumo_agua FLOAT,
            lixo_reciclavel FLOAT,
            lixo_total FLOAT,
            consumo_energia FLOAT,
            op_veiculos VARCHAR(255),
            data_entrada int not NULL
        )
    ''')
    cursor.execute('''
        INSERT INTO dados_sustentavel (consumo_agua, lixo_reciclavel, lixo_total, consumo_energia, op_veiculos, data_entrada)
        VALUES (%s, %s, %s, %s, %s, %s)
    ''', (consumoagua, LixoR, LixoT, consumoenergia, op, data))
    conn.commit()
    cursor.close()
    conn.close()

def alterar_dados(novaagua, novalixoR, novalixoT, novaenergia, op, data):
    novaagua = float(input("Informe seu novo consumo de água informado na conta de água(Litros/Dia): "))
    novalixoR = float(input("Informe a nova porcentagem de lixo reciclável: "))
    novalixoT = float(input("Informe quantos Kg de lixo total você produz: "))
    novaenergia = float(input("Informe seu novo consumo de energia informado na sua conta de energia(Kwh/Dia): "))
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
        op = "Alta sustentabilidade"
    elif (bicicleta == "S" or caminhada == "S" or carroE == "S" or transportepublico == "S") and (carroF == "S" or carona == "S"):
        op = "Media sustentabilidade"
    elif (bicicleta == "N" and caminhada == "N" and carroE == "N" and transportepublico == "N") and (carroF == "S" or carona == "S"):
        op = "Baixa sustentabilidade"
    else:
        op = None
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE dados_sustentavel
        SET consumo_agua = %s, lixo_reciclavel = %s, lixo_total = %s, consumo_energia = %s, op_veiculos = %s
        WHERE data_entrada = %s
    ''', (novaagua, novalixoR, novalixoT, novaenergia, op, data))
    conn.commit()
    cursor.close()
    conn.close()

def apagar_dados(data):
    data = int(input("Informe a data que deseja apagar: "))
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM dados_sustentavel WHERE data_entrada = %s
    ''', (data,))
    conn.commit()
    cursor.close()
    conn.close()

def consultar_dados(data):
    data = int(input("Informe a data que deseja consultar: "))
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT consumo_agua, lixo_reciclavel, lixo_total, consumo_energia, op_veiculos, data_entrada
        FROM dados_sustentavel
        WHERE data_entrada = %s
    ''', (data,))
    registros = cursor.fetchall()
    for registro in registros:
        print(f"Consumo de água: {registro[0]} Litros/Dia {"(Alta Sustentabilidade)" if registro[0] < 150 else "(Moderada Sustentabilidade)" if registro[0] >= 150 and registro[0] <= 200  else "(Baixa Sustentabilidade)"}, ")
        print(f"Lixo reciclável: {registro[1]}% {"(Alta Sustentabilidade)" if registro[1] > 50 else "(Moderada Sustentabilidade)" if registro[1] >= 20 and registro[1] <= 50  else "(Baixa Sustentabilidade)"},")
        print(f"Lixo total: {registro[2]} {"(Alta Sustentabilidade)" if registro[1] > 50 else "(Moderada Sustentabilidade)" if registro[1] >= 20 and registro[1] <= 50  else "(Baixa Sustentabilidade)"},")
        print(f"Consumo de energia: {registro[3]} Kwh/Dia {"(Alta Sustentabilidade)" if registro[3] < 5 else "(Moderada Sustentabilidade)" if registro[3] >= 5 and registro[3] <= 10 else "(Baixa Sustentabilidade)"},")
        print(f"Opção de veículos: {registro[4]}")
        print(f"Data de entrada: {registro[5]}")
    cursor.close()
    conn.close()

def consultar_medias(data):
    data = int(input("Informe a data que deseja consultar: "))
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT DISTINCT op_veiculos
        FROM dados_sustentavel
        WHERE data_entrada = %s
    ''', (data,))
    opcoes = cursor.fetchall()

    # Determinar o resultado com base nos valores de op_veiculos
    opcoes = [op[0] for op in opcoes]  # Extrair os valores da consulta
    if len(opcoes) == 1 and opcoes[0] == "ALTA":
        resultado_op = "ALTA"
    elif len(opcoes) == 1 and opcoes[0] == "BAIXA":
        resultado_op = "BAIXA"
    else:
        resultado_op = "MODERADA"
    cursor.execute('''
        SELECT AVG(consumo_agua) AS media_consumo_agua,
               AVG(consumo_energia) AS media_consumo_energia,
               AVG(lixo_total) AS media_lixo_total,
               AVG(lixo_reciclavel) AS media_lixo_reciclavel
        FROM dados_sustentavel
        WHERE data_entrada = %s
    ''', (data,))
    medias = cursor.fetchone()
    print(f"Média de consumo de água: {medias[0]} Litros/Dia {"(Alta Sustentabilidade)" if medias[0] < 150 else "(Moderada Sustentabilidade)" if medias[0] >= 150 and medias[0] <= 200  else "(Baixa Sustentabilidade)"}, ")
    print(f"Média de consumo de energia: {medias[1]} Kwh/Dia {"(Alta Sustentabilidade)" if medias[3] < 5 else "(Moderada Sustentabilidade)" if medias[3] >= 5 and medias[1] <= 10 else "(Baixa Sustentabilidade)"},")
    print(f"Média de lixo total: {medias[2]} Kg {"(Alta Sustentabilidade)" if medias[3] > 50 else "(Moderada Sustentabilidade)" if medias[3] >= 20 and medias[3] <= 50  else "(Baixa Sustentabilidade)"},")
    print(f"Média de lixo reciclável: {medias[3]}% {"(Alta Sustentabilidade)" if medias[3] > 50 else "(Moderada Sustentabilidade)" if medias[3] >= 20 and medias[3] <= 50  else "(Baixa Sustentabilidade)"},")
    print(f"Opção de veículos: {resultado_op}")
    print(f"Data de entrada: {data}")
    cursor.close()
    conn.close()

