import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user= 'caua',
            password= 'Talita01$',
            database= 'sustentabilidade'
        )
        if connection.is_connected():
            print("Conectado ao banco de dados")
            return connection
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return None

def insert_data(consumoagua, LixoR, LixoT, consumoenergia, op):
    conn = connect_to_database()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dados_sustentavel (
            consumo_agua FLOAT,
            lixo_reciclavel FLOAT,
            lixo_total FLOAT,
            consumo_energia FLOAT,
            op_veiculos VARCHAR(255)
        )
    ''')
    cursor.execute('''
        INSERT INTO dados_sustentavel (consumo_agua, lixo_reciclavel, lixo_total, consumo_energia, op_veiculos)
        VALUES (%s, %s, %s, %s, %s)
    ''', (consumoagua, LixoR, LixoT, consumoenergia, op))
    conn.commit()
    cursor.close()
    conn.close()