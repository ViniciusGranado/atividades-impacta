# Programação Orientada a Objetos
# AC01 POO-EaD - Números especiais
#
# Email Impacta: vinicius.granado@aluno.faculdadeimpacta.com.br


def eh_primo(n):
    if (n < 2):
        return False

    divisores = 0

    for i in range(2, n):
        if (n % i == 0):
            divisores += 1

    return divisores == 0


def lista_primos(n):
    primos = []
    for i in range(2, n):
        if eh_primo(i):
            primos.append(i)

    return primos


def conta_primos(s):
    primos = {}

    for i in s:
        if (eh_primo(i)):
            if i in primos:
                primos[i] += 1
            else:
                primos[i] = 1

    return primos


def eh_armstrong(n):
    str_number = str(n)
    digits = len(str_number)

    acc = 0
    for number in str_number:
        acc += int(number) ** digits

    return acc == n


def eh_quase_armstrong(n):
    if not eh_armstrong(n):
        return True

    str_number = str(n)
    digits = len(str_number)

    acc = 0
    for number in str_number:
        acc += int(number) ** digits

    return acc == n - 1 or acc == n + 1


def lista_armstrong(n):
    list = []

    for i in range(n):
        if (eh_armstrong(i)):
            list.append(i)

    return list


def eh_perfeito(n):
    if n < 2:
        return False

    soma_divisores = 0

    for i in range(1, n):
        if n % i == 0:
            soma_divisores += i

    return soma_divisores == n


def lista_perfeitos(n):
    list = []

    for i in range(n):
        if (eh_perfeito(i)):
            list.append(i)

    return list
