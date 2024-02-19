def minutos_para_horas_minutos(totalMinutos):
    horas = totalMinutos // 60
    minutos = totalMinutos % 60
    return horas, minutos

def horas_minutos_para_minutos(horas, minutos):
    totalMinutos = horas * 60 + minutos
    return totalMinutos

def main():
    while True:
        try:
            escolha = int(input("Escolha uma opção:\n1. Converter minutos para horas e minutos\n2. Converter horas e minutos para minutos totais\n3. Sair\n-> "))
            if escolha == 1:
                minutos = int(input("Digite o número total de minutos: "))
                horas, minutosRestantes = minutos_para_horas_minutos(minutos)
                print(f"{minutos} minutos é igual a {horas} horas e {minutosRestantes} minutos.")
            elif escolha == 2:
                horas = int(input("Digite o número de horas: "))
                minutos = int(input("Digite o número de minutos: "))
                totalMinutos = horas_minutos_para_minutos(horas, minutos)
                print(f"{horas} horas e {minutos} minutos é igual a {totalMinutos} minutos.")
            elif escolha == 3:
                print("Saindo do programa...")
                break
            else:
                print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")           
if __name__ == "__main__":
    main()