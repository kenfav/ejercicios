from random import randint
tupla = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f"Os valores sorteados foram: ", end="")
for t in tupla:
   print(t, end=" ")
sorteado = sorted(tupla)
print(f"\nO maior numero foi {sorteado[-1]} e o menor foi {sorteado[0]}.")