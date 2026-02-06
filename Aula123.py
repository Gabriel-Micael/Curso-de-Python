"""
Métodos para lidar com dicionários
"""
import copy

# Usando o dicionário da Aula121
pessoa = {
    'nome': [
        'Gabriel', 'Micael', 'Henrique'
    ],
    'sexo': 'M',
    'idade': 22,
    'redes': {
        'Instagram': 'gabriel.micael71',
        'Whatsapp': '+55 35 99756-9858',
        'Github': 'https://github.com/Gabriel-Micael'
    }
}
# len - retorna a quantidade de chaves que há nesse dicionário
print(len(pessoa))
print(pessoa.__len__())

# keys - retorna só as chaves
print(list(pessoa.keys()))

# values - retorna um dicionário apenas com os valores
print(tuple(pessoa.values()))

# items - retorna um dicionário com tuples de (chave, valor)
print(pessoa.items())

# separando chave e valor
for chave, valor in pessoa.items():
    print(chave, valor)

# setdefault - deixa um valor padrão para uma chave, caso não exista
pessoa.setdefault('ensino_medio', None)
print(pessoa['ensino_medio'])

# copy e shallow copy

# similar a ponteiros, apenas aponta para o mesmo local na memória
pessoa2 = pessoa
pessoa2['ensino_medio'] = 'Completo'

# altera para pessoa e pessoa2
print(pessoa2['ensino_medio'])
print(pessoa['ensino_medio'])

# duplica os itens para pessoa3
pessoa3 = pessoa.copy()
pessoa3['ensino_medio'] = 'incompleto'

# não altera em pessoa, pois é um local diferente na memória
print(pessoa3['ensino_medio'])
print(pessoa['ensino_medio'])

# Essa copia é rasa, pois caso houvesse outro dicionário dentro de "pessoa"
# ou uma lista (mutáveis), pessoa e pessoa3 apontariam para o mesmo endereço
# Exemplo

pessoa['teste'] = [1, 2, 3]
pessoa4 = pessoa.copy()
pessoa4['teste'][0] = 5

print(pessoa4['teste'])
print(pessoa['teste'])

# deep copy (tem que importar a biblioteca copy) - copia TUDO, se exceção

pessoa5 = copy.deepcopy(pessoa)
pessoa5['teste'][0] = 9
print(pessoa5['teste'])
print(pessoa['teste'])

# get - pega um valor

print(pessoa.get('nome')[0])
print(pessoa.get('escola', 'chave não existe'))

# pop - remove uma chave

pessoa.pop('idade')
print(pessoa.get('idade', 'campo não existente'))

# popitem - remove e retorna o último elemento adicionado

pessoa.popitem()
print(pessoa.get('teste', 'não existente'))

# update - atualiza e cria chaves sem alterar o restante

pessoa.update({
    'idade': 22,
    'sexo': 'Masculino',
})

print(pessoa.get('idade'))
print(pessoa.get('sexo'))

tupla = ('idade', 23), ('sexo', 'masculino')
pessoa.update(tupla)

print(pessoa.get('idade'))
print(pessoa.get('sexo'))