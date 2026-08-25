class Retangulo:
    def __init__(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def mudarLados(self, ladoA, ladoB):
        self.ladoA = ladoA
        self.ladoB = ladoB

    def RetornarLados(self):
        return self.ladoA, self.ladoB

    def calcularArea(self):
        return (self.ladoA * self.ladoB)

    def calcularPerimetro(self):
        return 2 * (self.ladoA + self.ladoB)


ladoA = float(input("Digite o comprimento do local (em metros): "))
ladoB = float(input("Digite a largura do local (em metros): "))

retangulo1 = Retangulo(ladoA, ladoB)

print("Área do local: ", retangulo1.calcularArea())
print("Perímetro do local: ", retangulo1.calcularPerimetro())