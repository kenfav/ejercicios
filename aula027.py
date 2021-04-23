num1 = input("Digite o numero: ")
num2 = input("Digite o numero: ")

try:
    print(int(num1)+int(num2))
except ValueError:
    print(" valor digitado foi invalido.")


