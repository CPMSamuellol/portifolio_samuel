# Protótipo de lógica em Python para diagnosticar sobras/faltas no caixa

# Suponha que temos registros das operações:
# Cada item é um dicionário com dados de vendas e eventos
vendas = [
    {"id": 1, "operador": "João", "forma_pagamento": "dinheiro", "valor": 100.0, "registrado": True},
    {"id": 2, "operador": "João", "forma_pagamento": "dinheiro", "valor": 50.0, "registrado": False},  # erro
    {"id": 3, "operador": "Ana", "forma_pagamento": "cartao", "valor": 200.0, "registrado": True},
    {"id": 4, "operador": "Pedro", "forma_pagamento": "dinheiro", "valor": 20.0, "registrado": True, "troco_esperado": 10.0, "troco_dado": 30.0},  # erro
    {"id": 5, "operador": "Pedro", "forma_pagamento": "dinheiro", "valor": 60.0, "registrado": True, "cancelada": True, "motivo": "Sem justificativa"},  # erro
]

# Função para diagnosticar possíveis falhas
def diagnosticar_falhas(vendas):
    relatorio = []
    for venda in vendas:
        if venda.get("forma_pagamento") == "dinheiro":
            if not venda.get("registrado"):
                relatorio.append({
                    "id": venda["id"],
                    "operador": venda["operador"],
                    "problema": "Venda em dinheiro não registrada",
                    "acao": "Verificar câmeras e questionar operador"
                })
            if venda.get("troco_esperado") and venda.get("troco_dado"):
                if venda["troco_dado"] != venda["troco_esperado"]:
                    relatorio.append({
                        "id": venda["id"],
                        "operador": venda["operador"],
                        "problema": f"Troco incorreto: esperado R$ {venda['troco_esperado']}, dado R$ {venda['troco_dado']}",
                        "acao": "Corrigir treinamento de troco"
                    })
        if venda.get("cancelada") and venda.get("motivo") == "Sem justificativa":
            relatorio.append({
                "id": venda["id"],
                "operador": venda["operador"],
                "problema": "Cancelamento sem justificativa",
                "acao": "Solicitar explicação ao operador"
            })
    return relatorio

# Exibir o relatório
erros = diagnosticar_falhas(vendas)
for erro in erros:
    print(f"Venda ID {erro['id']} | Operador: {erro['operador']} | Problema: {erro['problema']} | Ação: {erro['acao']}")
