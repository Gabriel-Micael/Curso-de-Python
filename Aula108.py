def multiplicar(x,y,z=None):
    if z is not None:
        print(f'multiplicando entre {x=}, {y=} e {z=}')
        return x * y * z
    else:
        print(f'multiplicando entre {x=} e {y=}')
        return x * y

multiplicar(y=2,x=3)
multiplicar(2,y=3)
multiplicar(2,z=3,y=5)