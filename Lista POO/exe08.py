class Macaco:

    def __init__(self, nome):
        self.nome = nome
        self.bucho = [] # lista vazia

    def comer(self, alimento):
        self.bucho.append(alimento)

    def verBucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []


macaco1 = Macaco("Will")
macaco2 = Macaco("Chico")

# Alimentando o primeiro macaco
macaco1.comer("Banana")
macaco1.comer("Maçã")
macaco1.comer("Laranja")

# Alimentando o segundo macaco
macaco2.comer("Banana")
macaco2.comer("Uva")
macaco2.comer("Manga")

print("Bucho do", macaco1.nome, ":", macaco1.verBucho())
print("Bucho do", macaco2.nome, ":", macaco2.verBucho())

macaco1.digerir()

print("\nDepois de digerir:")
print("Bucho do", macaco1.nome, ":", "Está vazio!", macaco1.verBucho())