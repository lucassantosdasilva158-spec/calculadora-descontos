# Exibe o título da calculadora de descontos
print ("Calculadora de descontes aplicáveis")

# Solicita ao usuário que insira o valor total da compra separando reais e centavos com ponto
valor_da_compra = float(input("Digite o valor total da compra separando reais e centavos com ponto: R$"))
# Calcula o desconto aplicável com base no valor da compra
if valor_da_compra <= 199.99:
    desconto =  0.05
elif valor_da_compra <= 299.99:
    desconto = 0.10
else:
    desconto = 0.15

# Calcula o valor do desconto e o valor final da compra após o desconto aplicado
valor_do_desconto = valor_da_compra * desconto
valor_final = valor_da_compra - valor_do_desconto
# Valor final da compra com desconto aplicado para exibição ao usuário
print (f"O valor da compra com desconto é: R$ {valor_final:.2f}")