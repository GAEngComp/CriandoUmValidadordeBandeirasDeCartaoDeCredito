# CriandoUmValidadordeBandeirasDeCartaoDeCredito

# TODO O CÓDIGO ABAIXO FOI GERADO PELA FERRAMENTA DE IA CHAT GPT.
# NADA DO QUE ESTÁ ESCRITO ABAIXO FOI GERADO NA INTENÇÃO DE PLÁGIO, MAS PARA CONCLUSÃO DE UM DESAFIO DE PROJETO DA DIO, VISTO QUE NÃO SEI PROGRAMAR EM NÍVEIS AVANÇADOS.


import re

def validar_luhn(numero):
    """Valida o número do cartão usando o algoritmo de Luhn"""
    numero = numero[::-1]  # Inverter o número
    soma = 0

    for i, digito in enumerate(numero):
        n = int(digito)
        if i % 2 == 1:  # Dobrar a cada segundo dígito
            n *= 2
            if n > 9:
                n -= 9
        soma += n

    return soma % 10 == 0

def detectar_bandeira(numero):
    """Detecta a bandeira do cartão baseado em prefixo e comprimento"""
    numero = numero.replace(" ", "").replace("-", "")

    if not numero.isdigit():
        return "Número inválido"

    if re.match(r'^5[1-5][0-9]{14}$', numero):
        return "MasterCard"
    elif re.match(r'^4[0-9]{12}(?:[0-9]{3})?$', numero):
        return "Visa"
    elif re.match(r'^3[47][0-9]{13}$', numero):
        return "American Express"
    elif re.match(r'^3(?:0[0-5]|[68][0-9])[0-9]{11}$', numero):
        return "Diners Club"
    elif re.match(r'^6(?:011|5[0-9]{2})[0-9]{12}$', numero):
        return "Discover"
    elif re.match(r'^2(?:014|149)[0-9]{11}$', numero):
        return "EnRoute"
    elif re.match(r'^(?:2131|1800|35\d{3})\d{11}$', numero):
        return "JCB"
    elif re.match(r'^8699[0-9]{11}$', numero):
        return "Voyager"
    elif re.match(r'^(606282|3841)[0-9]{10,12}$', numero):
        return "HiperCard"
    elif re.match(r'^50[0-9]{14,17}$', numero):
        return "Aura"
    else:
        return "Bandeira desconhecida"

def validar_cartao(numero):
    """Combina detecção de bandeira com validação Luhn"""
    bandeira = detectar_bandeira(numero)
    if bandeira == "Número inválido" or bandeira == "Bandeira desconhecida":
        return f"{numero}: {bandeira}"
    elif validar_luhn(numero):
        return f"{numero}: {bandeira} (válido)"
    else:
        return f"{numero}: {bandeira} (inválido)"

# Exemplos de teste
cartoes_exemplo = [
    "5555555555554444",     # MasterCard
    "4111111111111111",     # Visa
    "378282246310005",      # American Express
    "30569309025904",       # Diners Club
    "6011111111111117",     # Discover
    "201400000000009",      # EnRoute
    "3530111333300000",     # JCB
    "8699123456789012",     # Voyager
    "6062825624254001",     # HiperCard
    "5078601870000127983"   # Aura
]

for numero in cartoes_exemplo:
    print(validar_cartao(numero))
