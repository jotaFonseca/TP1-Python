##Solicitando ao usuário que insira o valor da compra
valorCompra = float(input("digite o valor da compra: R$"))

##Aplicando os descontos com base no valor da compra
if valorCompra > 200:
    desconto = 0.15
elif valorCompra > 100:
    desconto = 0.10
else:
    desconto = 0
    
#Calculando o valor do desconto
valorDesconto = valorCompra * desconto

#Calculando o valor final da compra com o desconto aplicado
valorFinal = valorCompra - valorDesconto

#Saida do valor final da compra com o desconto aplicado
print(f"O desconto foi de {desconto*100:.0f}%\nO valor final da compra com desconto é de R${valorFinal:.2f}")