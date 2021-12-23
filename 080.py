from random import randint
lista = list()
for i in range(0,5):
    n = randint(0,5)
    print(f'Numero {n} ', end="")
    if i == 0 or n > max(lista):
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        for pos in range(0,5):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'adicionado na posicao {pos} da lista. ')
                break
print(lista)
