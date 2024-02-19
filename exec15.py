print("Bem-vindo à aventura!")
print("Você está em uma encruzilhada. Você pode:")
print("1. Seguir pela trilha à esquerda.")
print("2. Seguir pela trilha à direita.")

escolha = input("Qual é a sua escolha? (1 ou 2): ")

if escolha == '1':
    print("Você segue pela trilha à esquerda e encontra um tesouro!")
elif escolha == '2':
    print("Você segue pela trilha à direita e se depara com um dragão!")
else:
    print("Escolha inválida! Você fica parado e a aventura termina.")