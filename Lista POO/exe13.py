class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def getNome(self):
        return self.nome

    def getSalario(self):
        return self.salario


funcionario = Funcionario("Taissa", 3500.00)

print("Nome:", funcionario.getNome())
print(f"Salário: R$ {funcionario.getSalario():.2f}")