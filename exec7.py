##Calculo do IMC
#Entrada do peso e da altura
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

#Calculando o IMC
imc = peso / (altura**2)
print("-"*25)
#Avaliando as condições
if imc < 18.5:
    print(f"Abaixo do peso.\nSeu IMC é de: {imc:.2f}")
elif imc >= 18.5 and imc < 25:
    print(f"Peso normal.\nSeu IMC é de: {imc:.2f}")
elif imc >= 25 and imc < 30:
    print(f"Sobrepeso.\nSeu IMC é de: {imc:.2f}")
else:
    print(f"Obesidade.\nSeu IMC é de: {imc:.2f}")