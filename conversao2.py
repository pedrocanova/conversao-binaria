# Programa de conversão de decimal para binário e hexadecimal

def decimal_para_binario(numero):
    """
    Converte um número decimal em binário usando o algoritmo de divisões sucessivas.
    """
    if numero == 0:
        return "0"

    binario = ""
    num_temp = numero

    # Divisões sucessivas por 2
    while num_temp > 0:
        resto = num_temp % 2
        binario = str(resto) + binario
        num_temp = num_temp // 2

    return binario


def decimal_para_hexadecimal(numero):
    """
    Converte um número decimal em hexadecimal usando o algoritmo de divisões sucessivas.
    """
    if numero == 0:
        return "0"

    hex_chars = "0123456789ABCDEF"
    hexadecimal = ""
    num_temp = numero

    # Divisões sucessivas por 16
    while num_temp > 0:
        resto = num_temp % 16
        hexadecimal = hex_chars[resto] + hexadecimal
        num_temp = num_temp // 16

    return hexadecimal


def binario_em_quartetos(binario):
    """
    Separa um número binário em quartetos (grupos de 4 bits).
    """
    # Inverte para processar da direita para esquerda
    binario_invertido = binario[::-1]
    quartetos = []

    # Divide em grupos de 4
    for i in range(0, len(binario_invertido), 4):
        quarteto = binario_invertido[i:i+4]
        quartetos.append(quarteto[::-1])  # Inverte de volta

    # Inverte a lista para ordem correta
    quartetos.reverse()

    return " ".join(quartetos)


# Número decimal a ser convertido
numero_decimal = 24015032

# Conversão manual (algoritmo)
resultado_binario = decimal_para_binario(numero_decimal)
resultado_hexadecimal = decimal_para_hexadecimal(numero_decimal)
resultado_binario_quartetos = binario_em_quartetos(resultado_binario)

# Conversão usando funções nativas do Python
resultado_bin_nativo = bin(numero_decimal)[2:]  # [2:] remove o prefixo '0b'
resultado_hex_nativo = hex(numero_decimal)[2:].upper()  # [2:] remove o prefixo '0x'

# Exibindo os resultados
print("=" * 60)
print(f"Conversão de Decimal para Binário e Hexadecimal")
print("=" * 60)
print(f"Número decimal: {numero_decimal:,}")
print()
print(f"Número binário: {resultado_binario}")
print(f"Binário em quartetos: {resultado_binario_quartetos}")
print(f"Quantidade de bits: {len(resultado_binario)}")
print()
print(f"Número hexadecimal: {resultado_hexadecimal}")
print("=" * 60)
print(f"\nVerificações:")
print(f"Binário (bin() do Python): {resultado_bin_nativo}")
print(f"Binário coincide: {resultado_binario == resultado_bin_nativo}")
print(f"Hexadecimal (hex() do Python): {resultado_hex_nativo}")
print(f"Hexadecimal coincide: {resultado_hexadecimal == resultado_hex_nativo}")
