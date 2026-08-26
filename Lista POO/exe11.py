class Carro:

    def __init__(self, consumo):
        self.consumo = consumo
        self.gasolina = 0

    def andar(self, distancia):
        gasolina_gasta = distancia / self.consumo
        self.gasolina -= gasolina_gasta

    def obterGasolina(self):
        return self.gasolina

    def adicionarGasolina(self, quantidade):
        self.gasolina += quantidade


meuFusca = Carro(15)

meuFusca.adicionarGasolina(40)
print("Gasolina obtida: ", meuFusca.obterGasolina(), "litros")

meuFusca.andar(100)

print("\nApós andar 100km:")
print(f"Gasolina restante:  {meuFusca.obterGasolina():.2f} litros")