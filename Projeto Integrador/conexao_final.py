import mysql.connector
from cifra_de_palavra import *

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
    
def inserir_dados(consumoagua, LixoR, LixoT, consumoenergia, op, data):
    conn = connect_to_database()
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
        op = cifra_palavra("Alta", key_matrix)
    elif (bicicleta == "S" or caminhada == "S" or carroE == "S" or transportepublico == "S") and (carroF == "S" or carona == "S"):
        op = cifra_palavra("Media", key_matrix)
    elif (bicicleta == "N" and caminhada == "N" and carroE == "N" and transportepublico == "N") and (carroF == "S" or carona == "S"):
        op = cifra_palavra("Baixa", key_matrix)
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
    data = int(input("Informe a data que deseja alterar: "))
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
        op = cifra_palavra("Alta", key_matrix)
    elif (bicicleta == "S" or caminhada == "S" or carroE == "S" or transportepublico == "S") and (carroF == "S" or carona == "S"):
        op = cifra_palavra("Media", key_matrix)
    elif (bicicleta == "N" and caminhada == "N" and carroE == "N" and transportepublico == "N") and (carroF == "S" or carona == "S"):
        op = cifra_palavra("Baixa", key_matrix)
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
    certeza = ""
    data = int(input("Informe a data que deseja apagar: "))
    conn = connect_to_database()
    cursor = conn.cursor()
    while certeza != "S" and certeza != "N":
        certeza = input("Têm certeza que quer apagar?(S/N): ").upper()
    if certeza == "N":
        return
    cursor.execute('''
        DELETE FROM dados_sustentavel WHERE data_entrada = %s
    ''', (data,))
    conn.commit()
    cursor.close()
    conn.close()

def consultar_dados():
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT consumo_agua, lixo_reciclavel, lixo_total, consumo_energia, op_veiculos, data_entrada
        FROM dados_sustentavel
    ''')
    registros = cursor.fetchall()
    for registro in registros:
        consumo_agua = registro[0]
        lixo_reciclavel = registro[1]
        lixo_total = registro[2]
        consumo_energia = registro[3]
        data_entrada = registro[5]
        op_veiculos = decifra_palavra(registro[4], key_matrix)

        print(f"Data: {data_entrada}")
        print(f"Consumo de água: {consumo_agua} Litros/Dia {'(Alta Sustentabilidade)' if consumo_agua < 150 else '(Moderada Sustentabilidade)' if 150 <= consumo_agua <= 200 else '(Baixa Sustentabilidade)'}")
        print(f"Lixo reciclável: {lixo_reciclavel}% {'(Alta Sustentabilidade)' if lixo_reciclavel > 50 else '(Moderada Sustentabilidade)' if 20 <= lixo_reciclavel <= 50 else '(Baixa Sustentabilidade)'}")
        print(f"Lixo total: {lixo_total} Kg {'(Alta Sustentabilidade)' if lixo_reciclavel > 50 else '(Moderada Sustentabilidade)' if 20 <= lixo_reciclavel <= 50 else '(Baixa Sustentabilidade)'}")
        print(f"Consumo de energia: {consumo_energia} Kwh/Dia {'(Alta Sustentabilidade)' if consumo_energia < 5 else '(Moderada Sustentabilidade)' if 5 <= consumo_energia <= 10 else '(Baixa Sustentabilidade)'}")
        print(f"Opção de veículos: {op_veiculos.replace('X','')}")
        print("-" * 40)
    cursor.close()
    conn.close()

def consultar_medias():
    conn = connect_to_database()
    if conn is None:
        print("Erro ao conectar ao banco de dados.")
        return

    cursor = conn.cursor()
    cursor.execute('''
        SELECT consumo_agua, consumo_energia, lixo_total, lixo_reciclavel, op_veiculos
        FROM dados_sustentavel
    ''')
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum registro encontrado.")
        cursor.close()
        conn.close()
        return

    consumo_agua_decifrado = [registro[0] for registro in registros]
    consumo_energia_decifrado = [registro[1] for registro in registros]
    lixo_total_decifrado = [registro[2] for registro in registros]
    lixo_reciclavel_decifrado = [registro[3] for registro in registros]
    opcoes_veiculos = [decifra_palavra(registro[4], key_matrix) for registro in registros]

    media_consumo_agua = sum(consumo_agua_decifrado) / len(consumo_agua_decifrado)
    media_consumo_energia = sum(consumo_energia_decifrado) / len(consumo_energia_decifrado)
    media_lixo_total = sum(lixo_total_decifrado) / len(lixo_total_decifrado)
    media_lixo_reciclavel = sum(lixo_reciclavel_decifrado) / len(lixo_reciclavel_decifrado)

    if len(set(opcoes_veiculos)) == 1:
        resultado_op = opcoes_veiculos[0]
    else:
        resultado_op = "MODERADA"

    print(f"Média de consumo de água: {media_consumo_agua:.2f} Litros/Dia {'(Alta Sustentabilidade)' if media_consumo_agua < 150 else '(Moderada Sustentabilidade)' if 150 <= media_consumo_agua <= 200 else '(Baixa Sustentabilidade)'}")
    print(f"Média de consumo de energia: {media_consumo_energia:.2f} Kwh/Dia {'(Alta Sustentabilidade)' if media_consumo_energia < 5 else '(Moderada Sustentabilidade)' if 5 <= media_consumo_energia <= 10 else '(Baixa Sustentabilidade)'}")
    print(f"Média de lixo total: {media_lixo_total:.2f} Kg {'(Alta Sustentabilidade)' if media_lixo_reciclavel > 50 else '(Moderada Sustentabilidade)' if 20 <= media_lixo_reciclavel <= 50 else '(Baixa Sustentabilidade)'}")
    print(f"Média de lixo reciclável: {media_lixo_reciclavel:.2f}% {'(Alta Sustentabilidade)' if media_lixo_reciclavel > 50 else '(Moderada Sustentabilidade)' if 20 <= media_lixo_reciclavel <= 50 else '(Baixa Sustentabilidade)'}")
    print(f"Opção de veículos: {resultado_op}")

    cursor.close()
    conn.close()