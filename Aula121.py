# Dicionários são similares a struct em C. possúi sempre chave - valor

# Exemplo

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

print(pessoa['redes']['Instagram'])
print(pessoa['redes']['Whatsapp'])
print(pessoa['nome'])
print(pessoa['idade'])