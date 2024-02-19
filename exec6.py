from random import randint

##gerando um número secreto aleatório entre 1 e 100
numSecreto = randint(1, 100)

print("Bem vindo ao jogo de adivinhacão! Adivinha o número que estou pensando entre 1 a 100. Tente adivinhar. (Voce tem 5 chances)")
tentativas = 0

while True:
    ##Inserindo o palpite
    palpite = int(input("Qual seu palpite? \n-> "))
    
    ##Incremento de tentativas
    tentativas += 1
    
    ##Verificando os palpites
    if palpite == numSecreto:
        print(f"Parabéns! Voce acertou o número em {tentativas} tentativas!")
        jogarNovamente = input("Deseja jogar novamente? (s/n) \n-> ").lower()
        if jogarNovamente != "s":
            print("Obrigado por jogar! Até logo.")
            break
        else:
            tentativas = 0
    elif palpite > numSecreto:
        print(f"Seu palpite foi maior do que o número que eu estou pensando. Faltam {5 - tentativas} tentativas.")
    else:
        print(f"Seu palpite foi menor do que o número que eu estou pensando. Faltam {5 - tentativas} tentativas.")
    
    if tentativas == 5:
        print(f"Infelizmente você passou do limite de tentativas, o número correto era {numSecreto}. Tente novamente mais tarde.")
        jogarNovamente = input("Deseja jogar novamente? (s/n) \n-> ").lower()
        if jogarNovamente != "s":
            print("Obrigado por jogar! Até logo.")
            break
        else:
            tentativas = 0