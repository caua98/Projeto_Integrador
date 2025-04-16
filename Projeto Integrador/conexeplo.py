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

def fetch_data(data):
    conn = connect_to_database()
    if conn is None:
        print("Não foi possível conectar ao banco de dados.")
        return

    cursor = conn.cursor()
    cursor.execute('''
        SELECT * FROM dados_sustentavel where data_entrada = %s
    ''', (data,))
    rows = cursor.fetchall()
    return rows

    # Exibindo os dados retornados
    cursor.close()
    conn.close()