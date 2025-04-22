import mysql.connector
import cifra_de_palavra
import cifra_num_final
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

def insert_data(consumoagua, LixoR, LixoT, consumoenergia, op, data):
    conn = connect_to_database()
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


def fetch_averages_by_date(data):
    conn = connect_to_database()
    if conn is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    cursor = conn.cursor()

    # Consulta para calcular as médias
    cursor.execute('''
        SELECT 
            AVG(consumo_agua) AS media_consumo_agua,
            AVG(consumo_energia) AS media_consumo_energia,
            AVG(lixo_total) AS media_lixo_total,
            AVG(lixo_reciclavel) AS media_lixo_reciclavel
        FROM dados_sustentavel
        WHERE data_entrada = %s
    ''', (data,))
    averages = cursor.fetchone()

    # Consulta para buscar todos os registros da data fornecida
    cursor.execute('''
        SELECT consumo_agua, lixo_reciclavel, lixo_total, consumo_energia, op_veiculos, data_entrada
        FROM dados_sustentavel
        WHERE data_entrada = %s
    ''', (data,))
    registros = cursor.fetchall()

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

    # Exibindo os registros
    print(f"\nRegistros encontrados para a data {data}:")
    if registros:
        for registro in registros:
            print(f"Consumo de Água: {registro[0]} Litros/Dia {"(Alta Sustentabilidade)" if registro[0] < 150 else "(Moderada Sustentabilidade)" if registro[0] >= 150 and registro[0] <= 200  else "(Baixa Sustentabilidade)"}, "
                  f"Lixo Reciclável: {registro[1]} % {"(Alta Sustentabilidade)" if registro[1] > 50 else "(Moderada Sustentabilidade)" if registro[1] >= 20 and registro[1] <= 50  else "(Baixa Sustentabilidade)"},"
                  f"Lixo Total: {registro[2]} Kg {"(Alta Sustentabilidade)" if registro[1] > 50 else "(Moderada Sustentabilidade)" if registro[1] >= 20 and registro[1] <= 50  else "(Baixa Sustentabilidade)"},"
                  f"Consumo de Energia: {registro[3]} Kwh/Dia {"(Alta Sustentabilidade)" if registro[3] < 5 else "(Moderada Sustentabilidade)" if registro[3] >= 5 and registro[3] <= 10 else "Baixa Sustentabilidade"}, "
                  f"Opção de Veículos: {registro[4]}, "
                  f"Data de Entrada: {registro[5]}")
    else:
        print("Nenhum registro encontrado para a data fornecida.")

    # Exibindo as médias
    if averages and any(averages):
        print(f"\nMédias para a data {data}:")
        print(f"Média de Consumo de Água: {averages[0]:.2f} Litros/Dia")
        print(f"Média de Consumo de Energia: {averages[1]:.2f} Kwh/Dia")
        print(f"Média de Lixo Total: {averages[2]:.2f} Kg")
        print(f"Média de Lixo Reciclável: {averages[3]:.2f} %")
        print(f"Resultado das Opções de Veículos: {resultado_op}")
    else:
        print(f"\nNenhuma média calculada para a data: {data}")

    cursor.close()
    conn.close()