numeroextenso = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez')
while True:
    nuemero = int(input("Escolha um numero: "))
    if nuemero not in range(0, 11):
        print('Numero invalido')


    else:
        print(f"O numero escolhido foi {numeroextenso[nuemero]}.")
        resp = str(input("Quer continuar: [S/N]")).strip().upper()[0]
        if resp == 'N':
            break
        elif resp == 'S':
            pass
        else:
            print('Opcion invalida')
print("Obrigado por escolher um numero")