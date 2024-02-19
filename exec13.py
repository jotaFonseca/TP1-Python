# Solicita ao usuário que insira uma palavra ou frase
palavra_frase = input("Digite uma palavra ou frase: ")

# Remove espaços em branco e converte para minúsculas
palavra_frase = palavra_frase.replace(" ", "").lower()

# Verifica se a palavra ou frase é um palíndromo
if palavra_frase == palavra_frase[::-1]:
    print("A palavra ou frase é um palíndromo.")
else:
    print("A palavra ou frase não é um palíndromo.")