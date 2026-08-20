class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def mostraCor(self):
        print("A cor da bola é:", self.cor)

    def trocaCor(self, nova_cor):
        self.cor = nova_cor


bola1 = Bola("Azul", 20, "borracha")
bola1.mostraCor()

bola1.trocaCor("Vermelha")
bola1.mostraCor()