opcoes = ["Opção 1", "Opção 2", "Opção 3"]
votos = [0, 0, 0]

print("Bem-vindo à votação!")
print("Por favor, vote nas opções abaixo:")
for i, opcao in enumerate(opcoes, 1):
    print(f"{i}. {opcao}")

# Loop para receber os votos do usuário
while True:
    voto = input("Digite o número da opção desejada (ou 'fim' para encerrar a votação): ")
    if voto.lower() == 'fim':
        break
    elif voto.isdigit() and 1 <= int(voto) <= len(opcoes):
        votos[int(voto) - 1] += 1
        print("Voto registrado!")
    else:
        print("Opção inválida! Por favor, escolha um número entre 1 e", len(opcoes))

# Exibe os resultados da votação
print("\nResultados da votação:")
for opcao, voto in zip(opcoes, votos):
    print(f"{opcao}: {voto} votos")