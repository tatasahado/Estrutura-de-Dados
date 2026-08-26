class BichinhoVirtual:

    def __init__(self, nome, fome, tedio):
        self.nome = nome
        self.fome = fome
        self.tedio = tedio

    def alimentar(self, quantidade):
        self.fome -= quantidade

        if self.fome < 0:
            self.fome = 0

    def brincar(self, tempo):
        self.tedio -= tempo

        if self.tedio < 0:
            self.tedio = 0

    def retornarFome(self):
        return self.fome

    def retornarTedio(self):
        return self.tedio


bichinho = BichinhoVirtual("Minion", 80, 70)

print("Nome:", bichinho.nome)
print("Fome:", bichinho.retornarFome())
print("Tédio:", bichinho.retornarTedio())

quantidade = int(input("\nQuanto de comida você quer dar? "))
bichinho.alimentar(quantidade)

tempo = int(input("Por quantos minutos você quer brincar? "))
bichinho.brincar(tempo)

print("\nDepois das ações:")
print("Fome:", bichinho.retornarFome())
print("Tédio:", bichinho.retornarTedio())