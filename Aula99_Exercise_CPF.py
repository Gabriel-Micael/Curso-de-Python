from itertools import count

cpf = input('Digite seu CPF: ')

cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')
if cpf.isnumeric() and len(cpf) == 11 and cpf != cpf[0] * 11:
    part1 = cpf[:9]
    part2 = cpf[-2:]
    part1 = part1.replace('.','')
    soma = 0

    # CALCULO DO PRIMEIRO DIGITO

    for part, dezDecrescente in zip(part1, range(10, 1, -1)):
        if part.isdigit():
            soma += int(part) * dezDecrescente
        else:
            print('Somente numeros!')

    soma = soma * 10
    resto = soma % 11
    primeiro_digito = resto if resto <= 9 else 0
    primeiro = int(part2[0]) == primeiro_digito
    if primeiro:
        print('O primeiro digito esta correto')
    else:
        print('O primeiro digito esta incorreto')

    # CALCULO DO SEGUNDO DIGITO

    part1 = part1 + str(primeiro_digito)
    soma = 0

    for part, dezDecrescente in zip(part1, range(11, 1, -1)):
        if part.isdigit():
            soma += int(part) * dezDecrescente
        else:
            print('Somente numeros!')

    soma = soma * 10
    resto = soma % 11
    segundo_digito = resto if resto <= 9 else 0
    segundo = int(part2[1]) == segundo_digito
    if segundo:
        print('O segundo digito esta correto')
    else:
        print('O segundo digito esta incorreto')

    if primeiro and segundo:
        print('Seu CPF e valido')
    else:
        print('Seu CPF e invalido')
else:
    print('CPF inválido')