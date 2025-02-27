import requests

def pegar_palavra_aleatoria():
    url = "https://random-word-api.herokuapp.com/word?lang=pt-br"
    resposta = requests.get(url)

    if resposta.status_code == 200:
        palavra = resposta.json()[0]  # A API retorna uma lista com uma palavra
        return palavra
    else:
        return "Erro ao buscar palavra"

sair = False
while not sair:
    alfabeto = "Q W E R T Y U I O P \n A S D F G H J K L \n Z X C V B N M"
    palavra_secreta = pegar_palavra_aleatoria()
    palavra_formatada = list("_" * len(palavra_secreta))
    letras_digitadas = ""
    tentativas = 15
    while True:
        if tentativas <= 0:
            print("\033[31m\nSUAS TENTATIVAS ACABARAM!\033[0m")
            break

        print("\nVocê ainda tem {} tentativas!".format(tentativas))
        letra_atual = input("Digite uma letra: ").lower()

        if len(letra_atual) != 1 or not(letra_atual.isalpha()):
            print("Digite apenas uma letra.")
            continue
        if not(letra_atual in palavra_secreta) and (letra_atual not in letras_digitadas):
            print("\033[31mQue pena! Você errou!\033[0m")
            alfabeto = alfabeto.replace(letra_atual.upper(), "\033[31m" + letra_atual.upper() + "\033[0m")
        elif letra_atual in letras_digitadas:
            print("\033[33mVocê já digitou essa letra!\033[0m")
        else:
            i = 0
            for letra in palavra_secreta:
                if letra == letra_atual:
                    palavra_formatada[i] = letra
                i = i + 1
            print("\033[32mVocê acertou uma letra!\033[0m")
            alfabeto = alfabeto.replace(letra_atual.upper(), "\033[32m" + letra_atual.upper() + "\033[0m")
        print("\nPalavra Formatada: {}".format("".join(palavra_formatada)))
        if "_" not in palavra_formatada:
            print("\033[32m\nPARABÉNS, VOCÊ CONSEGUIU!\033[0m")
            break
        letras_digitadas = letras_digitadas + letra_atual
        print("\n{}".format(alfabeto))
        tentativas = tentativas - 1
    while True:
        novamente = input("\nJogar novamente? [\033[32mS\033[0m/\033[31mn\033[0m]\n=>")
        if novamente not in "SsNn":
            print("Digite apenas S/s/N/n.")
            continue
        if  novamente in "Nn":
            sair = True
        else:
            sair = False
        break




