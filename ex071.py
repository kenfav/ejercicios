print("{:-^45}".format('Bancon Central'))
print("Disponemos de cedulas de 50, 20, 10, 5, 1\n")
valor = int(input("Digite o valor que deseja sacar: R$ "))
ced = 50
cont50 = 0
while valor >= ced:
        valor = valor - ced
        cont50 += 1
ced = 20
cont20 = 0
while valor >= ced:
        valor = valor - ced
        cont20 += 1
ced = 10
cont10 = 0
while valor >= ced:
    valor = valor - ced
    cont10 += 1
ced = 5
cont5 = 0
while valor >= ced:
    valor = valor - ced
    cont5 += 1
ced = 1
cont1 = 0
while valor >= ced:
    valor = valor - ced
    cont1 += 1
print(f"Voce recebera \n{cont50} notas de R$50,\n{cont20} notas de R$20,\n{cont10} notas de R$10,\n{cont5} notas de R$5 e\n{cont1} notas de 1.")


