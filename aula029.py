"""num1 = input("Digite um número: ")

try:
    intero = int(num1)
    if intero%2==0:
        print("O número é par")
    else:
        print("O número é impar")
except ValueError:
   print("O valor nao pode se convertido para inteiro")

hora = input("Digite a hora: ")
if hora[1] == ":":
    hora = "0"+ hora
try:
    if 0 <= int(hora[:2]) <= 11:
        print("Bom dia")
    elif 12 <= int(hora[:2]) <= 17:
        print("Boa tarde")
    elif 18 <= int(hora[:2]) <= 23:
        print("Boa noite")
    else:
        print("Hora digitada invalida")
except ValueError:
    print("Hora digitada foi invalida")

"""
nome = input("Digite o seu nome: ")
if len(nome) <= 4:
    print("Seu nome é curto")
elif 5 <= len(nome) <= 6:
    print("Seu nome é normal")
elif len(nome) > 6:
    print("Seu nome é comprido")
else:
    print("Valor digitado invalido")
print("Finalizado")
