a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# Verifica se forma triângulo
if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os valores formam um triângulo!")
    if a == b == c:
        print("Tipo: Triângulo Equilátero")
    elif a == b or a == c or b == c:
        print("Tipo: Triângulo Isósceles")
    else:
        print("Tipo: Triângulo Escaleno")
else:
    print("Os valores NÃO formam um triângulo.")