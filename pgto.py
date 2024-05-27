def calcular_preco_final(preco, forma_pagamento, parcelas=1):
    # Função para calcular o preço final com base na forma de pagamento e no número de parcelas
    preco_final = preco  # Preço inicial é o preço da mercadoria

    if forma_pagamento == 1:  # Se a forma de pagamento for 1 (Débito ou PIX)
        preco_final *= 0.9  # Aplica desconto de 10%

    elif forma_pagamento == 2:  # Se a forma de pagamento for 2 (Parcelado)
        if parcelas >= 3:  # Se o número de parcelas for 3 ou mais
            preco_final *= 1.05  # Aplica juros de 5% a partir da 3ª parcela

    return preco_final  # Retorna o preço final

def calcular_valor_parcela(preco, parcelas):
    # Função para calcular o valor de cada parcela
    valor_parcela = preco / parcelas  # Divide o preço pelo número de parcelas
    return valor_parcela  # Retorna o valor de cada parcela

# Preço base da mercadoria
preco_mercadoria = 100.00

# Solicita a forma de pagamento ao usuário
print("Escolha a forma de pagamento:")
print("1 - Débito ou PIX (com 10% de desconto)")
print("2 - Parcelado (com juros de 5% a partir da 3ª parcela)")
forma_pagamento = int(input("Opção: "))

if forma_pagamento == 2:  # Se a forma de pagamento for parcelada
    parcelas = int(input("Digite o número de parcelas: "))  # Solicita o número de parcelas
    preco_final = calcular_preco_final(preco_mercadoria, forma_pagamento, parcelas)  # Calcula o preço final
    valor_parcela = calcular_valor_parcela(preco_final, parcelas)  # Calcula o valor de cada parcela
else:
    preco_final = calcular_preco_final(preco_mercadoria, forma_pagamento)  # Calcula o preço final sem parcelamento
    valor_parcela = None  # Define o valor de parcela como None, pois não é relevante nesse caso

print(f"Preço final: R${preco_final:.2f}")  # Exibe o preço final formatado com duas casas decimais

if valor_parcela:  # Se houver valor de parcela (ou seja, se não for None)
    print(f"Valor de cada parcela ({parcelas}x): R${valor_parcela:.2f}")  # Exibe o valor de cada parcela formatado

