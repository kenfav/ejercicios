n1 = int(input("Digite um valor"))
n2 = int(input("Digite um valor"))
n3 = int(input("Digite um valor"))
n4 = int(input("Digite um valor"))
tupla = (n1, n2, n3, n4)
print(f"Voce digitou os valores {tupla}")
print(f"O valor 9 apareceu {tupla.count(9)} vez(es)")
if 2 in tupla:
    print(f"O valor 2 apareceu na posicao {tupla.index(2)+1}")
print(f"Valores Pares: ", end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=" ")