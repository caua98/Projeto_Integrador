import mysql.connector
from cifra_de_palavra import *
from cifra_num_final import *
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
    consumoagua = cifra_hill(str(consumoagua), key_matrix)
    LixoR = float(input("Informe a porcentagem de lixo reciclável: "))
    LixoR = cifra_hill(str(LixoR), key_matrix)
    LixoT = float(input("Informe quantos Kg de lixo total você produz: "))
    LixoT = cifra_hill(str(LixoT), key_matrix)
    consumoenergia = float(input("Informe seu consumo de energia informado na sua conta de energia(Kwh/Dia): "))
    consumoenergia = cifra_hill(str(consumoenergia), key_matrix)
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
    novaagua = cifra_hill(str(novaagua), key_matrix)
    novalixoR = float(input("Informe a nova porcentagem de lixo reciclável: "))
    novalixoR = cifra_hill(str(novalixoR), key_matrix)
    novalixoT = float(input("Informe quantos Kg de lixo total você produz: "))
    novalixoT = cifra_hill(str(novalixoT), key_matrix)
    novaenergia = float(input("Informe seu novo consumo de energia informado na sua conta de energia(Kwh/Dia): "))
    novaenergia = cifra_hill(str(novaenergia), key_matrix)
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
    if data is None:
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
        # Decifra os dados, substitui 'X' por '.' e converte para float
        consumo_agua = float(decifra_num(registro[0], key_matrix).replace('X', '.'))
        lixo_reciclavel = float(decifra_num(registro[1], key_matrix).replace('X', '.'))
        lixo_total = float(decifra_num(registro[2], key_matrix).replace('X', '.'))
        consumo_energia = float(decifra_num(registro[3], key_matrix).replace('X', '.'))
        data_entrada = registro[5]
        op_veiculos = decifra_palavra(registro[4], key_matrix)

        # Exibe os dados com os testes condicionais
        print(f"Consumo de água: {consumo_agua} Litros/Dia {'(Alta Sustentabilidade)' if consumo_agua < 150 else '(Moderada Sustentabilidade)' if 150 <= consumo_agua <= 200 else '(Baixa Sustentabilidade)'}")
        print(f"Lixo reciclável: {lixo_reciclavel}% {'(Alta Sustentabilidade)' if lixo_reciclavel > 50 else '(Moderada Sustentabilidade)' if 20 <= lixo_reciclavel <= 50 else '(Baixa Sustentabilidade)'}")
        print(f"Lixo total: {lixo_total} Kg {'(Alta Sustentabilidade)' if lixo_reciclavel > 50 else '(Moderada Sustentabilidade)' if 20 <= lixo_reciclavel <= 50 else '(Baixa Sustentabilidade)'}")
        print(f"Consumo de energia: {consumo_energia} Kwh/Dia {'(Alta Sustentabilidade)' if consumo_energia < 5 else '(Moderada Sustentabilidade)' if 5 <= consumo_energia <= 10 else '(Baixa Sustentabilidade)'}")
        print(f"Opção de veículos: {op_veiculos.replace('X','')}")
        print(f"Data de entrada: {data_entrada}")
    cursor.close()
    conn.close()

def consultar_medias():
    data = int(input("Informe a data que deseja consultar: "))
    conn = connect_to_database()
    if conn is None:
        print("Erro ao conectar ao banco de dados.")
        return

    cursor = conn.cursor()

    # Consulta para buscar os dados da data fornecida
    cursor.execute('''
        SELECT consumo_agua, consumo_energia, lixo_total, lixo_reciclavel, op_veiculos
        FROM dados_sustentavel
        WHERE data_entrada = %s
    ''', (cifra_hill(str(data), key_matrix),))
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum registro encontrado para a data fornecida.")
        cursor.close()
        conn.close()
        return

    # Decifrar os dados
    consumo_agua_decifrado = [float(decifra_num(registro[0], key_matrix)) for registro in registros]
    consumo_energia_decifrado = [float(decifra_num(registro[1], key_matrix)) for registro in registros]
    lixo_total_decifrado = [float(decifra_num(registro[2], key_matrix)) for registro in registros]
    lixo_reciclavel_decifrado = [float(decifra_num(registro[3], key_matrix)) for registro in registros]
    opcoes_veiculos = [decifra_palavra(registro[4], key_matrix) for registro in registros]

    # Calcular as médias
    media_consumo_agua = sum(consumo_agua_decifrado) / len(consumo_agua_decifrado)
    media_consumo_energia = sum(consumo_energia_decifrado) / len(consumo_energia_decifrado)
    media_lixo_total = sum(lixo_total_decifrado) / len(lixo_total_decifrado)
    media_lixo_reciclavel = sum(lixo_reciclavel_decifrado) / len(lixo_reciclavel_decifrado)

    # Determinar a sustentabilidade com base nas opções de veículos
    if len(set(opcoes_veiculos)) == 1:
        resultado_op = opcoes_veiculos[0]
    else:
        resultado_op = "MODERADA"

    # Exibir os resultados
    print(f"Média de consumo de água: {media_consumo_agua:.2f} Litros/Dia {'(Alta Sustentabilidade)' if media_consumo_agua < 150 else '(Moderada Sustentabilidade)' if 150 <= media_consumo_agua <= 200 else '(Baixa Sustentabilidade)'}")
    print(f"Média de consumo de energia: {media_consumo_energia:.2f} Kwh/Dia {'(Alta Sustentabilidade)' if media_consumo_energia < 5 else '(Moderada Sustentabilidade)' if 5 <= media_consumo_energia <= 10 else '(Baixa Sustentabilidade)'}")
    print(f"Média de lixo total: {media_lixo_total:.2f} Kg {'(Alta Sustentabilidade)' if media_lixo_reciclavel > 50 else '(Moderada Sustentabilidade)' if 20 <= media_lixo_reciclavel <= 50 else '(Baixa Sustentabilidade)'}")
    print(f"Média de lixo reciclável: {media_lixo_reciclavel:.2f}% {'(Alta Sustentabilidade)' if media_lixo_reciclavel > 50 else '(Moderada Sustentabilidade)' if 20 <= media_lixo_reciclavel <= 50 else '(Baixa Sustentabilidade)'}")
    print(f"Opção de veículos: {resultado_op}")
    print(f"Data de entrada: {data}")

    cursor.close()
    conn.close()

