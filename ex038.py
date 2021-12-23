from random import choice
def topo():
    print('='*20)
    print('{:^20}'.format('JOKEMPO'))
    print('='*20)
    print(" "*20)

while True:
    topo()
    pc = ['Pedra', 'Papel', 'Tesoura']
    pcopcao = choice(pc)
    opcao = int(input('Escolha:\n(1) PEDRA\n(2) PAPEL\n(3) TESOURA\n(4) FINALIZAR\n\nDIGITE SUA OPCAO: '))

    if opcao == 1:
        pessoa = 'Pedra'
        print('O Computador escolheu {}.'.format(pcopcao))
        if pcopcao == pessoa:
            print('EMPATE')
        elif pcopcao == 'Papel':
            print('Voce perdeu Papel pega a Pedra')
        else:
            print('Voce ganhou! Pedra quebra tesoura')
    elif opcao == 2:
        pessoa = 'Papel'
        print('O Computador escolheu {}.'.format(pcopcao))
        if pcopcao == pessoa:
            print('EMPATE')
        elif pcopcao == 'Pedra':
            print('Voce ganhou. Papel pega a Pedra.')
        else:
            print('Voce perdeu. Tesoura corta Papel')
    elif opcao == 3:
        pessoa = 'Tesoura'
        print('O Computador escolheu {}.'.format(pcopcao))
        if pcopcao == pessoa:
            print("EMPATE")
        elif pcopcao == 'Pedra':
            print('Voce perdeu. Pedra quebra tesoura.')
        else:
            print('Voce ganhou! Tesoura corta papel')
    elif opcao == 4:
        break
    else:
        print('A sua opcao nao foi valida. Escolha outra opcao.')
