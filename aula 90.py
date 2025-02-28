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
        except IndexError:
            print("Erro no valor a remover!")

    elif opcao == 3:
        for item in enumerate(lista):
            indice, value = item
            print(indice, value)
    elif opcao == 4:
        break
    else:
        print("Opção invalida!")
