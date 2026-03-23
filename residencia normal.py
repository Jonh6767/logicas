consumo = float(input("Digite o consumo de água em m3: "))

if consumo <= 10:
    valor = 22.38
elif consumo <= 20:
    valor = consumo * 3.50
elif consumo <= 50:
    valor = consumo * 8.75
else:
    valor = consumo * 9.64

print(f"Valor da conta de água (Residência Normal): R$ {valor:.2f}")