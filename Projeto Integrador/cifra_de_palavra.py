import numpy as np

# Dicionário de letras para números
letras_num = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4,
    'E': 5, 'F': 6, 'G': 7,
    'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13,
    'N': 14, 'O': 15, 'P': 16,
    'Q': 17, 'R': 18, 'S': 19,
    'T': 20, 'U': 21, 'V': 22,
    'W': 23, 'X': 24, 'Y': 25, 'Z': 26,
     # Caractere de preenchimento
}

# Dicionário inverso para decodificação
num_letras = {v: k for k, v in letras_num.items()}

# Matriz-chave (2x2 para pares de letras)
key_matrix = np.array([[3, 3], [2, 5]])

# Função para calcular o inverso modular de uma matriz
def inversa_modular(matrix, mod):
    det = int(np.round(np.linalg.det(matrix)))  # Determinante da matriz
    det_inv = pow(det, -1, mod)  # Inverso modular do determinante
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % mod  # Matriz adjunta
    return (det_inv * adjugate) % mod

# Função para codificar usando a cifra de Hill
def cifra_palavra(palavra, key_matrix):
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
        resultado = np.dot(key_matrix, vetor) % 26
        
        # Converte os números de volta para letras
        mensagem_codificada += num_letras[resultado[0][0] if resultado[0][0] != 0 else 26]
        mensagem_codificada += num_letras[resultado[1][0] if resultado[1][0] != 0 else 26]
    
    return mensagem_codificada

# Função para descriptografar usando a cifra de Hill
def decifra_palavra(mensagem_codificada, key_matrix):
    inversa_key_matrix = inversa_modular(key_matrix, 26)  # Calcula a matriz inversa no módulo 26
    pares = [mensagem_codificada[i:i+2] for i in range(0, len(mensagem_codificada), 2)]
    
    mensagem_decodificada = ""
    for par in pares:
        # Converte o par de letras em números
        vetor = np.array([[letras_num[par[0]]], [letras_num[par[1]]]])
        
        # Multiplica pela matriz inversa e aplica módulo 26
        resultado = np.dot(inversa_key_matrix, vetor) % 26
        
        # Converte os números de volta para letras
        mensagem_decodificada += num_letras[resultado[0][0] if resultado[0][0] != 0 else 26]
        mensagem_decodificada += num_letras[resultado[1][0] if resultado[1][0] != 0 else 26]
    
    return mensagem_decodificada
