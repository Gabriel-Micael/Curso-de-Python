import decimal
# PROBLEMAS
# num1 = decimal.Decimal(0.9)
# num2 = decimal.Decimal(0.003)

#SOLUÇÂO
num1 = decimal.Decimal('0.9')
num2 = decimal.Decimal('0.003')

num3 = num1 + num2
print(num3)
print(f'{num3:.3f}')
print(round(num3, 3))