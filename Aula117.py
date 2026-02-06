# Usando Clousure

def saudacao(saudacao):
    def saudar(nome):
        return saudacao + ', ' + nome
    return saudar

falar_bom_dia = saudacao('Bom dia')
falar_bom_noite = saudacao('Bom noite')

for nome in ['Joao', 'Teresa', 'Gabriel']:
    print(falar_bom_noite(nome))
    print(falar_bom_dia(nome))