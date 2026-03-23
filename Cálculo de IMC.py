peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura * altura)
print(f"Seu IMC é: {imc:.2f}")

if imc < 16:
    print("Classificação: Magreza grave")
elif 16 <= imc < 17:
    print("Classificação: Magreza moderada")
elif 17 <= imc < 18.5:
    print("Classificação: Magreza leve")
elif 18.5 <= imc < 25:
    print("Classificação: Saudável")
elif 25 <= imc < 30:
    print("Classificação: Sobrepeso")
elif 30 <= imc < 35:
    print("Classificação: Obesidade Grau I")
elif 35 <= imc < 40:
    print("Classificação: Obesidade Grau II (severa)")
else:
    print("Classificação: Obesidade Grau III (mórbida)")