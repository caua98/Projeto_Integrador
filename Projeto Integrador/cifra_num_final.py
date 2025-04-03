import numpy as np

# Dicionário de letras para números
letras_num = {
    '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '0': 0,
    'X': 10
}

# Dicionário inverso para decodificação
num_letras = {v: k for k, v in letras_num.items()}

# Matriz-chave (2x2 para pares de letras)
key_matrix = np.array([[3, 3], [2, 5]])

def inversa_modular(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  # Determinante da matriz
    det_inv = pow(det, -1, mod)  # Inverso modular do determinante
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  # Matriz adjunta
    return (det_inv * adjugate) % mod
# Função para codificar usando a cifra de Hill
def cifra_hill(palavra, key_matrix):
    palavra = palavra.upper()
    pares = [palavra[i:i+2] for i in range(0, len(palavra), 2)]
    
    # Adiciona um caractere de preenchimento se o número de letras for ímpar
    if len(pares[-1]) == 1:
        pares[-1] += 'X'
    
    mensagem_codificada = ""
    for par in pares:
        # Converte o par de letras em números
        vetor = np.array([[letras_num[par[0]]], [letras_num[par[1]]]])
        
        # Multiplica pela matriz-chave e aplica módulo 26
        resultado = np.dot(key_matrix, vetor) % 10
        
        # Converte os números de volta para letras
        mensagem_codificada += num_letras[resultado[0][0] if resultado[0][0] != 0 else 10]
        mensagem_codificada += num_letras[resultado[1][0] if resultado[1][0] != 0 else 10]
    
    return mensagem_codificada

def decifra_hill(mensagem_codificada, key_matrix):
    inversa_key_matrix = inversa_modular(key_matrix, 10) # Calcula a matriz inversa no módulo 26
    pares = [mensagem_codificada[i:i+2] for i in range(0, len(mensagem_codificada), 2)]
    
    mensagem_decodificada = ""
    for par in pares:
        # Converte o par de letras em números
        vetor = np.array([[letras_num[par[0]]], [letras_num[par[1]]]])
        
        # Multiplica pela matriz inversa e aplica módulo 26
        resultado = np.dot(inversa_key_matrix, vetor) % 10
        
        # Converte os números de volta para letras
        mensagem_decodificada += num_letras[resultado[0][0] if resultado[0][0] != 0 else 10]
        mensagem_decodificada += num_letras[resultado[1][0] if resultado[1][0] != 0 else 10]
    
    return mensagem_decodificada
