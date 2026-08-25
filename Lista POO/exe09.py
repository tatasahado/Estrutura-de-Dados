class Ponto:

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Retangulo:

    def __init__(self, largura, altura, vertice):
        self.largura = largura
        self.altura = altura
        self.vertice = vertice

    def encontrar_centro(self):
        centro_x = self.vertice.x + self.largura / 2
        centro_y = self.vertice.y + self.altura / 2

        return Ponto(centro_x, centro_y)


def imprimir_ponto(ponto):
    print("X:", ponto.x)
    print("Y:", ponto.y)


ponto1 = Ponto(0, 0)
ponto2 = Ponto(10, 5)

retangulo1 = Retangulo(8, 4, ponto1)
retangulo2 = Retangulo(6, 10, ponto2)

centro1 = retangulo1.encontrar_centro()
centro2 = retangulo2.encontrar_centro()

print("Centro do Retângulo 1:")
imprimir_ponto(centro1)

print("\nCentro do Retângulo 2:")
imprimir_ponto(centro2)