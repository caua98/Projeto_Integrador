import numpy as np

# Dicionário de letras para números
letras_num = {
    '1': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '0': 0,
    '.': 11,  # Adiciona o ponto com um valor único
    'X': 10
}

num_letras = {v: k for k, v in letras_num.items()}

CESAR_SHIFT = 3  # Deslocamento da cifra de César
CESAR_MOD = 12   # Modulo para cobrir 0-9, X(10), .(11)

def cifra_cesar(palavra):
    palavra = str(palavra).upper()
    mensagem_codificada = ""
    for char in palavra:
        if char in letras_num:
            valor = letras_num[char]
            cifrado = (valor + CESAR_SHIFT) % CESAR_MOD
            mensagem_codificada += num_letras[cifrado]
        else:
            mensagem_codificada += char  # mantém caracteres não mapeados
    return mensagem_codificada

def decifra_cesar(mensagem_codificada):
    mensagem_codificada = str(mensagem_codificada).upper()
    mensagem_decodificada = ""
    for char in mensagem_codificada:
        if char in letras_num:
            valor = letras_num[char]
            decifrado = (valor - CESAR_SHIFT) % CESAR_MOD
            mensagem_decodificada += num_letras[decifrado]
        else:
            mensagem_decodificada += char
    return mensagem_decodificada