# Criando um dicionário de um produto

produto = {
    'nome': 'Notebook',
    'preco': 3500.00,
    'em_estoque': True
}

# Acessando valores pela chave
print(produto['nome']) #Saída: Notebook

# Acesso seguro usando .get() (evita erros se a chave não existir)
print(produto.get('marca')) # Saída: None

# Modificando um valor existente
produto['preco'] = 3200.00

# Adicionando uma nova chave-valor
produto["cor"] = "Cinza"

print(produto)
# Saída: {'nome': 'Notebook', 'preco': 3200.00, 'em_estoque': True, 'cor': 'cinza'}

#ITERANDO SOBRE CHAVES E VALORES COM .ITEMS()
for chave, valor in produto.items():
    print(f'{chave.capitalize()}: {valor}')