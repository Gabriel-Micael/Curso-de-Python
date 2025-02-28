# join une um iterável de Strings com um delimitador a sua escolha
# sintaxe: "<delimitador>".join(<iterável>)

# split separa os elementos de uma string dado um separador a sua escolha
# sintaxe: <String>.split("<separador>")

frase = "Testando o split e o join"
print("_".join(frase.split()))
print(frase.split(" "))
print(frase.split("split"))
print(frase.join("--"))