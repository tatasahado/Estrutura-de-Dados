import random


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


fazenda = []

fazenda.append(Bichinho("Rex", random.randint(0, 100), random.randint(0, 100)))
fazenda.append(Bichinho("Luna", random.randint(0, 100), random.randint(0, 100)))
fazenda.append(Bichinho("Thor", random.randint(0, 100), random.randint(0, 100)))
fazenda.append(Bichinho("Mel", random.randint(0, 100), random.randint(0, 100)))


while True:

    print("\n--- FAZENDA DE BICHINHOS ---")
    print("1 - Alimentar todos")
    print("2 - Brincar com todos")
    print("3 - Ouvir todos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        quantidade = int(input("Quanto de comida deseja dar? "))

        for bichinho in fazenda:
            bichinho.alimentar(quantidade)

        print("Todos os bichinhos foram alimentados!")

    elif opcao == "2":

        tempo = int(input("Por quantos minutos deseja brincar? "))

        for bichinho in fazenda:
            bichinho.brincar(tempo)

        print("Você brincou com todos os bichinhos!")

    elif opcao == "3":

        print("\n--- BICHINHOS DA FAZENDA ---")

        for bichinho in fazenda:
            print(bichinho)

        break

    elif opcao == "4":

        print("Programa encerrado.")
        break

    else:
        print("Opção inválida!")