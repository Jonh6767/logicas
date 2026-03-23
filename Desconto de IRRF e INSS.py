salario_bruto = float(input("Digite o valor do salário bruto: R$ "))

# Cálculo simplificado do INSS 2023
if salario_bruto <= 1320.00:
    inss = salario_bruto * 0.075
elif salario_bruto <= 2571.29:
    inss = salario_bruto * 0.09
elif salario_bruto <= 3856.94:
    inss = salario_bruto * 0.12
elif salario_bruto <= 7507.49:
    inss = salario_bruto * 0.14
else:
    inss = 7507.49 * 0.14 # Teto do INSS

salario_base_irrf = salario_bruto - inss

# Cálculo do IRRF 2023 (Tabela a partir de maio/2023)
if salario_base_irrf <= 2112.00:
    irrf = 0.0
elif salario_base_irrf <= 2826.65:
    irrf = (salario_base_irrf * 0.075) - 158.40
elif salario_base_irrf <= 3751.05:
    irrf = (salario_base_irrf * 0.15) - 370.40
elif salario_base_irrf <= 4664.68:
    irrf = (salario_base_irrf * 0.225) - 651.73
else:
    irrf = (salario_base_irrf * 0.275) - 884.96

print(f"Desconto INSS: R$ {inss:.2f}")
print(f"Desconto IRRF: R$ {irrf:.2f}")
print(f"Salário Líquido: R$ {salario_bruto - inss - irrf:.2f}")