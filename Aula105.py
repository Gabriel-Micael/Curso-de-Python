"""
Funções são iniciadas com def e são
usadas para replicar códigos sem
copiá-los. Precisam ser chamar, podendo
ou não exigir parâmetros e retornar
valores
"""

def funcao(item_a, item_b):
    print(item_a, item_b)
    return item_a + item_b

def saudacao(nome):
    print(f'Ola, {nome}!')
    return nome

def saudacao2(nome1, nome2):
    print(f'Ola, {funcao(nome1, nome2)}!')

funcao('A', 'B')

saudacao('Gabriel')
saudacao('Henrique')
saudacao('Gabriel ' + saudacao('Micael Henrique'))

saudacao2(saudacao("Gabriel "), saudacao('Micael Henrique'))