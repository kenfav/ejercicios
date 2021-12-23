from classes import carrinho, Produtos


carrinho = carrinho()


p1 = Produtos('Mouse', 25)
p2 = Produtos('Celular', 50)
p3 = Produtos('Cha', 5)

carrinho.inserir_produtos(p1)
carrinho.inserir_produtos(p2)
carrinho.inserir_produtos(p3)

print(carrinho.soma_total())
