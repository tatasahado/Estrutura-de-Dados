class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.idade = self.idade + 1

        if self.idade < 21:
            self.altura += 0.5

    def engordar(self, quilos):
        self.peso += quilos

    def emagrecer(self, quilos):
        self.peso -= quilos

    def crescer(self, centimetros):
        self.altura += centimetros


pessoa1 = Pessoa("Ana", 19, 46, 1.60)

print("Nome: ", pessoa1.nome)
print("Idade: ", pessoa1.idade)
print("Peso: ", pessoa1.peso, "kg")
print(f"Altura:  {pessoa1.altura:.2f}", "m")


pessoa1.envelhecer()

print("\nDepois de envelhecer: ")
print("Idade: ", pessoa1.idade)
print(f"Altura:  {pessoa1.altura:.2f}", "m")