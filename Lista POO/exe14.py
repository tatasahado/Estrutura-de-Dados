class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario

    def aumentarSalario(self, percentualDeAumento):
        aumento = self.salario * percentualDeAumento / 100
        self.salario += aumento


pessoa = Funcionario("Harry", 25000)

print("Nome:", pessoa.getNome())
print(f"Salário antes do aumento: R$ {pessoa.getSalario():.2f}")

pessoa.aumentarSalario(10)

print(f"Salário depois do aumento: R$ {pessoa.getSalario():.2f}")