while True:
    try:
        escolha = int(input("Escolha a operação: \n1 - Adição \n2 - Subtração \n3 - Multiplicação \n4 - Divisão \n5 - Sair \n-> "))
        
        if (escolha == 1):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 + num2
            print(f"O resultado da soma é: {resultado}")
        elif (escolha == 2):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
        elif (escolha == 3):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
        elif (escolha == 4):
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            resultado = num1 / num2
            print(f"O resultado da divisão é: {resultado:.2f}")
        elif (escolha == 5):
            print("Saindo do programa...")
            break
        else:
            print("Operação inválida")
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro.")