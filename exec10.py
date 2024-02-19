import random

# Listas de personagens, ações e locais
personagens = ["o mago", "o cavaleiro", "a princesa", "o dragão"]
acoes = ["encontrou um tesouro", "derrotou um monstro", "descobriu um segredo", "perdeu o caminho"]
locais = ["no castelo abandonado", "na floresta sombria", "no topo da montanha", "no fundo do mar"]

# Escolhe aleatoriamente elementos de cada lista
personagem = random.choice(personagens)
acao = random.choice(acoes)
local = random.choice(locais)

# Cria a história combinando os elementos escolhidos
historia = f"{personagem.capitalize()} {acao} {local}."

# Exibe a história criada
print("História curiosa:")
print(historia)