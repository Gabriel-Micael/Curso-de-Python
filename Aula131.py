"""
modificadores de conjunto

| -> Union
& -> Intersection
- -> Difference
^ -> symmetric difference
"""

# Exemplo

a = {1,2,3,4,5}
b = {1,3,5,7,8}

print(a & b)
print(a - b)
print(a | b)
print(a ^ b)