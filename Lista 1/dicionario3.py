produto = {
    "id": 101,
    "nome": "Notebook Galaxy Book 4",
    "categoria": "Informática",
    "preco": 3599.90,
    "quantidade": 15,
    "disponivel": True,
    "marca": "Samsung",
    "garantia_meses": 12,
    "cores": ["Preto", "Prata"],  # O valor será uma lista
    "especificacoes": {
        "processador": "Intel Core i5",
        "memoria_ram": "16 GB",
        "armazenamento": "512 GB SSD",
        "sistema_operacional": "Windows 11"
    },
    "fornecedor": {
        "nome": "Tech Distribuidora",
        "cidade": "Rio de Janeiro",
        "telefone": "(21) 99999-9999"
    },
    "avaliacoes": [5, 4, 5, 5, 3],
    "tags": ["promoção", "eletrônicos", "notebook"],
    "data_cadastro": "2026-08-05"
}

print(produto)

# Acessando valores
print(produto["nome"])
print(produto["preco"])
print(produto["especificacoes"]["memoria_ram"])
print(produto["cores"][0])  # Preto

# Alterando valores
produto["quantidade"] = 20
produto["preco"] = 4399.90
print(produto)

# Adicionando novos elementos
produto["desconto"] = "10%"
produto["fabricacao"] = "Brasil"
print(produto)

# Removendo elementos
del produto["garantia_meses"]
print(produto)

# Percorrendo o dicionário
for chave, valor in produto.items():
    print(f"{chave}: {valor}")


