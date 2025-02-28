from code import interact

lista = list()
while True:
    opcao = input('Digite uma opção [Inserir - 1 ; Remover - 2 ; Listar - 3 ; Sair - 4]: ')
    if opcao.isnumeric():
        opcao = int(opcao)
    if opcao == 1:
        item = input('Digite um item para inserir: ')
        lista.append(item)
    elif opcao == 2:
        idx = int(input('Digite o id do item a remover: '))
        try:
            lista.pop(idx)
        except ValueError:
            print("Erro no valor digitado!")
        except IndexError:
            print("Valor não encontrado!")

    elif opcao == 3:
        for indice, value in enumerate(lista):
            print(indice, value)
    elif opcao == 4:
        break
    else:
        print("Opção invalida!")
