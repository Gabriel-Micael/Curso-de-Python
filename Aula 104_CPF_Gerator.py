import random
cpf = ''
for i in range(9):
    cpf += str(random.randint(0,9))

print(cpf)

part1 = cpf[:9]

soma = 0
# CALCULO DO PRIMEIRO DIGITO

for part, dezDecrescente in zip(part1, range(10, 1, -1)):
    soma += int(part) * dezDecrescente

soma = soma * 10
resto = soma % 11
primeiro_digito = resto if resto <= 9 else 0

# CALCULO DO SEGUNDO DIGITO

part1 = part1 + str(primeiro_digito)
soma = 0

for part, dezDecrescente in zip(part1, range(11, 1, -1)):
    soma += int(part) * dezDecrescente

soma = soma * 10
resto = soma % 11
segundo_digito = resto if resto <= 9 else 0

cpf_novo = cpf + str(primeiro_digito) + str(segundo_digito)
print('Novo CPF: {}'.format(cpf_novo))
