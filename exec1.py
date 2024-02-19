##Entrada dos dados
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

escolha = int(input("Escolha a operação: \n1 - Soma \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Divisão Inteira \n-> "))

##Calculo dos dados
if (escolha == 1):
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif (escolha == 2):
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif (escolha == 3):
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif (escolha == 4):
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado:.2f}")
elif (escolha == 5):
    resultado = num1 // num2
    print(f"O resultado da divisão inteira é: {resultado}")
else:
    print("Operação inválida")