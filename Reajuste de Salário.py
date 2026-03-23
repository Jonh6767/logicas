salario = float(input("Digite o salário do funcionário: R$ "))

if salario <= 1000:
    percentual = 20
elif salario <= 1700:
    percentual = 15
elif salario <= 2300:
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100)
novo_salario = salario + aumento

print(f"Salário digitado: R$ {salario:.2f}")
print(f"Aumento         : {percentual}%")
print(f"Valor do aumento: R$ {aumento:.2f}")
print(f"Novo salário    : R$ {novo_salario:.2f}")