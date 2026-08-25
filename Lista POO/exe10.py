class BombaCombustivel:

    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valorLitro

        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print("Quantidade abastecida:", litros, "litros")
        else:
            print("Quantidade de combustível insuficiente.")

    def abastecerPorLitro(self, litros):
        valor = litros * self.valorLitro

        if litros <= self.quantidadeCombustivel:
            self.quantidadeCombustivel -= litros
            print("Valor a pagar: R$", valor)
        else:
            print("Quantidade de combustível insuficiente.")

    def alterarValor(self, novoValor):
        self.valorLitro = novoValor

    def alterarCombustivel(self, novoCombustivel):
        self.tipoCombustivel = novoCombustivel

    def alterarQuantidadeCombustivel(self, novaQuantidade):
        self.quantidadeCombustivel = novaQuantidade


bomba = BombaCombustivel("Gasolina", 6.00, 1000)

print("Combustível:", bomba.tipoCombustivel)
print("Valor do litro: R$", bomba.valorLitro)
print("Quantidade disponível:", bomba.quantidadeCombustivel, "litros")

# Abastecendo por valor
print("\nAbastecimento por valor:")
bomba.abastecerPorValor(60)

print("Combustível restante:", bomba.quantidadeCombustivel, "litros")

# Abastecendo por litros
print("\nAbastecimento por litros:")
bomba.abastecerPorLitro(20)

print("Combustível restante:", bomba.quantidadeCombustivel, "litros")

# Alterando o valor do combustível
bomba.alterarValor(6.50)

print("\nNovo valor do litro: R$", bomba.valorLitro)