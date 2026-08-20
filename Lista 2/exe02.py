class product:

    def __init__(self, nome, marca, preco):
        self.nome = nome
        self.marca = marca
        self.preco = preco

    def get_nome(self):
        return self.nome

    def get_marca(self):
        return self.marca

    def get_preco(self):
        return self.preco

    def exibir_informacoes(self):
        print(f"Nome do produto: {self.nome}")
        print(f"Marca do produto: {self.marca}")
        print(f"Preço do produto: {self.preco}")

produto1 = product ("Camisa", "Vans", 259)

produto1.exibir_informacoes()