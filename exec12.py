# Solicita ao usuário que insira uma lista de palavras separadas por espaços
palavras = input("Digite uma lista de palavras separadas por espaços: ").split()

# Loop para classificar cada palavra como curta ou longa e exibir o resultado
for palavra in palavras:
    if len(palavra) < 5:
        print(f"{palavra} é uma palavra curta.")
    else:
        print(f"{palavra} é uma palavra longa.")