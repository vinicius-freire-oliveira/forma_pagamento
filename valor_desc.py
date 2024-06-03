# Definição da função para calcular o desconto
def calcular_desconto(preco, desconto):
    return preco * desconto / 100

# Definição da função para calcular o valor a pagar
def calcular_valor_a_pagar(preco, desconto):
    # Chama a função calcular_desconto para obter o valor do desconto
    valor_do_desconto = calcular_desconto(preco, desconto)
    # Calcula o valor final a ser pago após o desconto
    return preco - valor_do_desconto

# Função principal do programa
def main():
    # Solicita ao usuário que digite o preço da mercadoria e o percentual de desconto
    preco = float(input("Digite o preço da mercadoria: "))
    desconto = float(input("Digite o percentual de desconto: "))

    # Chama as funções para calcular o desconto e o valor a pagar
    valor_do_desconto = calcular_desconto(preco, desconto)
    a_pagar = calcular_valor_a_pagar(preco, desconto)

    # Imprime os resultados formatados na tela
    print(f"Um desconto de {desconto:.2f}% em uma mercadoria de R$ {preco:.2f} vale R$ {valor_do_desconto:.2f}.")
    print(f"O valor a pagar é de R$ {a_pagar:.2f}")

# Executa a função main quando o script é executado diretamente
if __name__ == "__main__":
    main()
