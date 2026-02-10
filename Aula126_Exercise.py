perguntas = [
    {
        'enunciado':'Quem descobriu o Brasil?',
        'opcoes':['Pedro Álvares Cabral', 'Dom Pedro I', 'Américo Vespucci', 'Cristóvão Colombo'],
        'respota':'0'
    },
    {
        'enunciado':'Quem inventou a corrente alternada?',
        'opcoes':['Westinghouse','Thomas Edison','Nikola Tesla','Benjamin Franklin'],
        'respota':'2'
    },
    {
        'enunciado':'Quando os escravos foram libertos pela lei?',
        'opcoes':['1895','1830','1888','1902'],
        'respota':'2'
    }
]



def exibe_prova(perguntas):

    def exibe_questao(pergunta):

        def exibe_enuciado(pergunta):
            print(pergunta['enunciado'])

        def exibe_opcoes(pergunta):
            for opcao, i in zip(pergunta['opcoes'], range(len(pergunta['opcoes']))):
                print(f'{i}) {opcao}.')
            escolha = input('Escolha uma opção: ')
            return escolha

        def verifica_respota(escolha):
            if int(escolha) in range(0, len(pergunta['opcoes']), 1):
                if escolha == pergunta['respota']:
                    print('Você acertou!\n')
                    return int(1)
            print('Você errou!\n')
            return 0

        exibe_enuciado(pergunta)
        escolha = exibe_opcoes(pergunta)

        return verifica_respota(escolha)

    pontos = 0
    for pergunta in perguntas:
        pontos += exibe_questao(pergunta)
    return pontos

pontuacao = exibe_prova(perguntas)
print(f'As pergutas acabaram. Você acertou {pontuacao} de {len(perguntas)} perguntas.')