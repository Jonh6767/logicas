consumo = float(input("Digite o consumo de água em m3: "))

if consumo <= 10:
    valor = 44.95
elif consumo <= 20:
    valor = consumo * 8.75
elif consumo <= 50:
    valor = consumo * 16.76
else:
    valor = consumo * 17.46

print(f"Valor da conta de água (Comércio/Indústria): R$ {valor:.2f}")