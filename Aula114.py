def multiply(*args):
    multi = 1
    for arg in args:
        multi *= arg
    return multi

def par_or_impar(arg):
    if arg % 2 == 0:
        return 'Par'
    return 'Impar'

print(multiply(1,2,3,4))

print(par_or_impar(4))