class Mercado:

    def __init__(self, marca, tipo, validade, preco):
        self.marca = marca
        self.tipo = tipo
        self.validade = validade
        self.preco = preco

    def get_marca(self):
        return self.marca

    def get_tipo(self):
        return self.tipo

    def get_validade(self):
        return self.validade

    def get_preco(self):
        return self.preco

    def exibir(self):
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Validade: {self.validade}")
        print(f"Preço: {self.preco}")


caixa = Mercado(
    input("Digite a marca do produto: "),
    input("Digite o tipo do produto: "),
    input("Digite a validade do produto: "),
    float(input("Digite o preço do produto: ")),
)

caixa.exibir()