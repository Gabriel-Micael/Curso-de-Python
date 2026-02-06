"""
Como atualizar, criar, deletar e acessar os dados em um dicionario
"""


computador = {}

chave = 'marca'

computador[chave] = 'Corsair'
computador['processador'] = 'i5 9400f'

print(computador)

print(computador['processador'])

computador['processador'] = 'i9 14900ks'

if computador.get('processador'): # Verifica se a chave "processador" existe dentro do dicionario "computador"
    print(computador['processador'])

del computador['processador']

if computador.get('processador'):
    print(computador['processador'])

print(computador)