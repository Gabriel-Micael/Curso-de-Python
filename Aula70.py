frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

frase = frase.replace(' ','')

i = 0
maior = 0
letra_mais_repetida = ''
while i < len(frase):
    letra_atual = frase[i]
    qtd_letra = frase.count(letra_atual)
    print(letra_atual, qtd_letra)
    if qtd_letra > maior:
        maior = qtd_letra
        letra_mais_repetida = letra_atual
    i = i + 1

print('a letra mais repetida é: "{letra_mais_repetida}"'.format(letra_mais_repetida=letra_mais_repetida))
