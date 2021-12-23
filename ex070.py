def resposta() -> object:
    while True:
        print("Quer continuar? [S/N]", end=" ")
        opcao = str(input("")).upper()
        print()
        if opcao == 'N':
            return False
            break
        elif opcao == 'S':
            return True
            break
        else:
            pass


print(f'{"Loja Baratao":-^30}')

soma = 0
maisde100 = 0
maisbaratopreco = 0
maisbarato = ''
while True:
    produto = str(input("Digite o produto: "))
    produtopreco = float(input("Digite o valor do produto. R$ "))
    soma = soma + produtopreco
    if maisbaratopreco == 0:
        maisbaratopreco = produtopreco
        maisbarato = produto
    elif produtopreco - maisbaratopreco > 0:
        pass
    else:
        maisbaratopreco = produtopreco
        maisbarato = produto
    if produtopreco > 1000:
        maisde100 += 1
    if not resposta():
        break


print(f"O Total da sua compra foi de {soma:.2f}, o produto mais barato foi {maisbarato} e voce comprou {maisde100} itens acima de 1000 reais.")

