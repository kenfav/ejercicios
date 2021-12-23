num = list()
while True:
    n = int(input("Digite um numero"))
    if n not in num:
        num.append(n)
        print('Numero adcionado com sucesso')
    else:
        print('Numero ja existe')

    r = str(input("Quer continuar: [S/N]: ")).strip()[0]
    if r in 'Nn':
        break
print(sorted(num))