class Bichinho:

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

    def __str__(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}"


bichinho = Bichinho("Minion", 80, 70)

while True:

    print("\n--- MENU ---")
    print("1 - Alimentar")
    print("2 - Brincar")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        quantidade = int(input("Quanto de comida deseja dar? "))
        bichinho.alimentar(quantidade)

    elif opcao == "2":
        tempo = int(input("Por quantos minutos deseja brincar? "))
        bichinho.brincar(tempo)

    elif opcao == "3":
        print("Programa encerrado.")
        break

    else:
        print("\n*** PORTA ESCONDIDA ***")
        print(bichinho)