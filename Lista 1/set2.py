# Operações com conjuntos

frutas = {"uva", "banana", "laranja"}
legumes = {"batata", "cenoura", "tomate"}

# União

sacolao = frutas | legumes
print(sacolao)

# Interseção

frutas = {"uva", "banana", "laranja"}
legumes = {"batata", "banana", "tomate"}

sacolao = frutas & legumes
print(sacolao)

# Diferença

frutas = {"uva", "banana", "laranja"}
legumes = {"uva", "banana"}

sacolao = frutas - legumes
print(sacolao)