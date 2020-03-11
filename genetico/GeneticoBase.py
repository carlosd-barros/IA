from math import fabs
from random import randint, random, choice, uniform
from string import ascii_letters, ascii_lowercase, ascii_uppercase

### FUNÇÕES GENERICAS ###
def decimalParaBinario(value):
    binario = ""
    count = 0

    while value > 0 and count < 8:
        mod = str( int(value % 2) )
        binario += mod
        value /= 2
        count += 1

    return int(binario[::-1])

def stringAleatoria(length=10):
    return "".join(
        choice(ascii_letters) for x in range(length)
    )


def numeroAleatorio(inteiro=2, decimal=2, is_float=True):
    num = random() * (10 ** inteiro)
    num = round(num, decimal)

    if not is_float:
        num = int(num)

    return num

#########################

# Questão 01
def binarioParaDecimal(value):
    inteiro = value[:2]
    inteiro = int(inteiro, base=2)

    fracionado = value[2:]
    fracionado = int(fracionado, base=2)

    real = f"{inteiro}.{fracionado}"
    real = float(real)

    return real

binario = '11111111'
b_para_d = binarioParaDecimal(binario)

print(f"""
    ## QUESTÃO 01
    Faça uma função que recebe uma string com oito valores zero ou um
    sendo os dois primeiros equivalentes à parte inteira
    e os seis restantes equivalente à parte fracionária de um número binário.
    A função deverá retornar este número convertido para um número real (float)

    ENTRADA: {binario}
    SAIDA: {b_para_d}
""")

# Questão 02

def floatDecimalParaBinario(value):
    if not isinstance(value, float):
        raise TypeError

    inteiro, fracionado = str(value).split('.')

    inteiro = int(inteiro)
    inteiro = decimalParaBinario(inteiro)

    fracionado = int(fracionado)
    fracionado = decimalParaBinario(fracionado)

    binario = f"{inteiro}{fracionado}"

    return binario

float_d_para_b = floatDecimalParaBinario(b_para_d)

print(f"""
    ## QUESTÃO 02
    Faça uma função que recebe um valor real (float) e converte para binário fracionário no formato
    de uma string com oito valores zero ou um, sendo os dois primeiros equivalentes à parte inteira e
    os seis restantes equivalente à parte fracionária do número binário. A função deve retornar esta
    string.

    ENTRADA: {b_para_d}
    SAÍDA: {float_d_para_b}
    INVERSO: {binarioParaDecimal(float_d_para_b)}
""")


# Questão 03
def gerarBinarioString():
    return "".join([
        str([0,1][randint(0,1)]) for i in range(8)
    ])

print(f"""
    ## QUESTÃO 03
    Faça uma função que cria uma string com oito valores zeros ou uns, retornando-a

    SAÍDA: {gerarBinarioString()}
""")


# Questão 04
def gerarListaDeStrings(listLength=100, stringLength=10):
    return [
        stringAleatoria(stringLength) for i in range(listLength)
    ]

print(f"""
    ## QUESTÃO 04
    Função que cria uma lista com cem strings (podem ser criadas aleatoriamente), retornando-a

    SAÍDA: {gerarListaDeStrings()}
""")

# Questão 5
def stringParaLista(value, maxNum=1000):
    return [value, round(uniform(0, maxNum), 2)]


print(f"""
    ## QUESTÃO 05

    Faça uma função que recebe uma string e retorne uma lista no formato [string original, número real]
    (o número real pode ser gerado aleatoriamente)

    SAÍDA: {stringParaLista(stringAleatoria())}
""")


# Questão 6
def matrizDeStrings(lista):
    return [
        stringParaLista(string) for string in lista
    ]

lista_de_strings = gerarListaDeStrings()
matriz = matrizDeStrings(lista_de_strings)

print(f"""
    ## QUESTÃO 06

    Faça uma função que recebe uma lista de strings e retorna uma nova lista composta por sublistas
    criadas da seguinte forma: [string original, número real]. (o número real pode ser gerado
    aleatoriamente)

    ENTRADA: {lista_de_strings}
    SAÍDA: {matriz}
""")

# Questão 7
def moduloAoQuadrado(value):
    return fabs(2 - value**2)


print(f"""
    ## QUESTÃO 07
    Faça uma função que recebe um valor real e retorne o módulo (valor absoluto) do valor 2 menos
    este valor real ao quadrado, ou seja : |2 – real2|

    SAÍDA: {moduloAoQuadrado( numeroAleatorio(inteiro=1) )}
""")

# Questão 8
def selecionaMelhores(matriz, max=10):
    matriz.sort(
        reverse=True,
        key=lambda x: x[1]
    )

    melhores = [
        i[0] for i in matriz[:max]
    ]

    return melhores


matriz = matrizDeStrings( gerarListaDeStrings() )

print(f"""
    # QUESTÃO 08
    Faça uma função que recebe uma lista de cem sublistas que têm aseguinte
    forma: [string original, número real],
    ordene-as do menor para o maior número real, e retorne uma lista com as dez
    primeiras strings desta lista recém-ordenada.

    SAÍDA: {selecionaMelhores(matriz)}
""")

# Questão 9
def mutacao(value):
    index = randint(0, len(value)-1)

    value = [i for i in value]
    value[index] = '0' if value[index] == '1' else '1'
    value = ''.join(value)

    return value

individuo = gerarBinarioString()

print(f"""
    ## QUESTÃO 09
    Faça uma função que recebe uma string de oito valores zeros ou uns e, aleatoriamente, modifique
    um de seus valores trocando de zero para um ou vice-versa.

    ENTRADA: {individuo}
    SAÍDA: {mutacao(individuo)}
""")


# Questão 10
def cruzamento1(value1, value2):
    new_value1 = value2[:4] + value1[4:]
    new_value2 = value1[:4] + value2[:4]

    return new_value1, new_value2

individuo1 = gerarBinarioString()
individuo2 = gerarBinarioString()

print(f"""
    ## QUESTÃO 10
    Faça uma função que recebe duas strings de oito valores zeros ou uns e crie duas novas strings no
    seguinte formato: uma string será composta pelos quatro primeiros valores da primeira seguidos
    pelos quatro últimos da segunda; e a outra string será composta pelos quatro primeiros valores da
    segunda string seguidos pelos quatro últimos da segunda string.

    ENTRADA: {individuo1, individuo2}
    SAíDA: {cruzamento1(individuo1, individuo2)}
""")


# QUESTÃO 11
def cruzamento2(value1, value2):
    new_value1 = value2[:2] + value1[2:6] + value2[6:]
    new_value2 = value1[:2] + value2[2:6] + value1[6:]

    return new_value1, new_value2

individuo1 = gerarBinarioString()
individuo2 = gerarBinarioString()

print(f"""
    ## QUESTÃO 11
    Faça uma função que recebe duas strings de oito valores zeros ou uns e crie duas novas strings
    no seguinte formato: uma string será composta pelos dois primeiros valores da primeira seguidos
    pelos quatro do meio da segunda e pelos dois últimos da primeira; e a outra string será
    composta pelos dois primeiros valores da segunda string seguidos pelos quatro do meio da
    primeira e pelos dois últimos da segunda string.

    ENTRADA 1: {individuo2[:2], individuo1[2:6], individuo2[6:]}
    ENTRADA 2: {individuo1[:2], individuo2[2:6], individuo1[6:]}
    SAÍDA: {cruzamento2(individuo1, individuo2)}
""")