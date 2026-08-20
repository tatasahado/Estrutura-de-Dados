class Automovel:
    def __init__(self, marca, modelo, ano, placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def get_marca(self):
        return self.marca

    def get_modelo(self):
        return self.modelo

    def get_ano(self):
        return self.ano

    def get_placa(self):
        return self.placa

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Ano: {self.ano}")
        print(f"Placa: {self.placa}")

    def texto(self):
        print(f"O carro de modelo {self.modelo} da marca {self.marca}, do ano {self.ano}, com a numeração {self.placa}, é maravilhoso!")

carro = Automovel ("Ferrari", "F40", 2026, "RKB-7456")

carro.exibir_informacoes()

carro.texto()