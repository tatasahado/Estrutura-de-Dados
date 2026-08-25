class BichinhoVirtual:

    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def alterar_nome(self, novo_nome):
        self.nome = novo_nome

    def alterar_fome(self, nova_fome):
        self.fome = nova_fome

    def alterar_saude(self, nova_saude):
        self.saude = nova_saude

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    def retornar_humor(self):
        return self.fome + self.saude


bichinho = BichinhoVirtual("Rex", 70, 80, 2)

print("Nome:", bichinho.retornar_nome())
print("Fome:", bichinho.retornar_fome())
print("Saúde:", bichinho.retornar_saude())
print("Idade:", bichinho.retornar_idade())
print("Humor:", bichinho.retornar_humor())

bichinho.alterar_fome(50)
bichinho.alterar_saude(90)

print("\nDepois das alterações:")
print("Fome:", bichinho.retornar_fome())
print("Saúde:", bichinho.retornar_saude())
print("Humor:", bichinho.retornar_humor())