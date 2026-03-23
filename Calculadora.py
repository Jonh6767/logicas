num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\n1 - Adição\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
print("5 - Potência\n6 - Raiz quadrada (do 1º nº)\n7 - Número par (avalia o 1º nº)\n8 - Número ímpar (avalia o 1º nº)")
op = int(input("Escolha a operação: "))

if op == 1:
    print(f"Resultado: {num1 + num2}")
elif op == 2:
    print(f"Resultado: {num1 - num2}")
elif op == 3:
    print(f"Resultado: {num1 * num2}")
elif op == 4:
    if num2 != 0:
        print(f"Resultado: {num1 / num2}")
    else:
        print("Erro: Divisão por zero!")
elif op == 5:
    print(f"Resultado: {num1 ** num2}")
elif op == 6:
    print(f"Resultado (Raiz do 1º): {num1 ** 0.5}")
elif op == 7:
    if num1 % 2 == 0:
        print("O primeiro número é Par")
    else:
        print("O primeiro número não é Par")
elif op == 8:
    if num1 % 2 != 0:
        print("O primeiro número é Ímpar")
    else:
        print("O primeiro número não é Ímpar")
else:
    print("Operação inválida.")