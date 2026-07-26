import json

notas_fiscais = [
    {
        "id": "NF-001",
        "cliente": "João Silva",
        "valor": 1500.00,
        "data_emissao": "2025-01-15"
    },
    {
        "id": "NF-002",
        "cliente": "Maria Santos",
        "valor": 2300.50,
        "data_emissao": "2025-02-20"
    }
]

with open("notas_fiscais_2025.json", "w", encoding="utf-8") as arquivo:
    json.dump(notas_fiscais, arquivo, ensure_ascii=False, indent=4)

print("Arquivo notas_fiscais_2025.json criado com sucesso!")