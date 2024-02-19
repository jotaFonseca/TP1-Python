##Entrada dos dados
idade = int(input("Digite sua idade: "))

##Verificação dos dados
if idade == 18:
    print("Você atingiu a maioridade.")
elif idade < 18:
    print("Você ainda não atingiu a maioridade.")
else:
    print("Você ultrapassou a maioridade.")