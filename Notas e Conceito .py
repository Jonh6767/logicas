n1 = float(input("Digite a nota 1: "))
n2 = float(input("Digite a nota 2: "))
n3 = float(input("Digite a nota 3: "))
n4 = float(input("Digite a nota 4: "))

media = (n1 + n2 + n3 + n4) / 4

if 9.0 <= media <= 10.0:
    conceito = "A"
elif 7.5 <= media < 9.0:
    conceito = "B"
elif 6.0 <= media < 7.5:
    conceito = "C"
elif 4.0 <= media < 6.0:
    conceito = "D"
else:
    conceito = "E"

print("\n--- Resultados ---")
print(f"Notas bimestrais: {n1}, {n2}, {n3}, {n4}")
print(f"Média final: {media:.2f}")
print(f"Conceito: {conceito}")

if conceito in ["A", "B", "C"]:
    print("Status: APROVADO")
else:
    print("Status: REPROVADO")