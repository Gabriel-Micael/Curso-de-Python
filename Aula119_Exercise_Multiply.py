def multiplicador(a):
    def multiplicando(b):
        return a * b
    return multiplicando

dobro = multiplicador(2)
triplo = multiplicador(3)
quadruplo = multiplicador(4)

print(dobro(2))
print(triplo(2))
print(quadruplo(2))