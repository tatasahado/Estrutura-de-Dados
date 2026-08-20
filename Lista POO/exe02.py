class Quadrado:
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def mudarTamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho

    def retornarTamanho(self):
        return self.tamanho

    def calcularArea(self):
        return self.tamanho ** 2

quadrado1 = Quadrado(3)

print("Tamanho do lado:", quadrado1.retornarTamanho(), "m")
print("Área:", quadrado1.calcularArea(), "m²")

quadrado1.mudarTamanho(10)

print("Novo Tamanho do lado:", quadrado1.retornarTamanho(), "m")
print("Nova Área:", quadrado1.calcularArea(), "m²")