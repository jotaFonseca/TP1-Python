import random

# Solicita ao usuário que insira a quantidade de dados a serem jogados
num_dados = int(input("Quantos dados você gostaria de jogar? "))

# Loop para simular o lançamento de cada dado
for i in range(1, num_dados + 1):
    # Gera um número aleatório entre 1 e 6 para simular o resultado de um dado de seis lados
    resultado = random.randint(1, 6)

    # Exibe o resultado do lançamento de cada dado
    print(f"Resultado do dado {i}: {resultado}")