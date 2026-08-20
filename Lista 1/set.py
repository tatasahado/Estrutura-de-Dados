# Criando um set

frutas = {"maçã", "banana", "laranja"}
print(frutas)

# Set não permite elementos duplicados

numeros = {1,2,3,3,4,4,5}
print(numeros)

# Adicionando elementos

frutas = {"maçã, banana"}
frutas.add("laranja")
print(frutas)

# Adicionando vários elementos

frutas = {"maçã, banana"}
frutas.update(["laranja", "uva", "morango"])
print(frutas)

# Removendo elementos

frutas = {"morango", "laranja", "uva"}
frutas.remove("laranja")
print(frutas)

# Limpando um set

frutas = {"morango", "laranja", "uva"}
frutas.clear()
print(frutas)

# Verificando se um elemento existe

frutas = {"morango", "laranja", "uva"}

if 'banana' in frutas:
    print("A banana está no conjunto")
else:
    print("A banana não está no conjunto")