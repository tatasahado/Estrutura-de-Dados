class TV:

    def __init__(self, canal, volume):
        self.canal = canal
        self.volume = volume

    def mudarCanal(self, novo_canal):
        if 1 <= novo_canal <= 100:
            self.canal = novo_canal
        else:
            print("Canal inválido.")

    def aumentarVolume(self):
        if self.volume < 100:
            self.volume += 1
        else:
            print("Volume já está no máximo.")

    def diminuirVolume(self):
        if self.volume > 0:
            self.volume -= 1
        else:
            print("Volume já está no mínimo.")

canal = int(input("Digite o número do canal: "))

tv1 = TV(canal, 50)

print("Canal:", tv1.canal)
print("Volume:", tv1.volume)

tv1.aumentarVolume()
tv1.diminuirVolume()

print("\nDepois das alterações:")
print("Canal:", tv1.canal)
print("Volume:", tv1.volume)