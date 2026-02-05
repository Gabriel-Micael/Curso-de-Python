# função com *args como parâmetro


def count_args(*args):
    i = 0
    for arg in args:
        i += 1
    return i

def sum_args_floats_ints(*args):
    i = 0
    for arg in args:
        if type(arg) == int or type(arg) == float:
            print('passou? {}'.format(arg))
            i += arg
    return i

print(count_args(1, 2, 3, 'Ola', True, False, (0.5, 'Nice'), [3,False]))

print(sum_args_floats_ints(1, 2, 3, 'Ola', True, False, (0.5, 'Nice'), [3,False]))