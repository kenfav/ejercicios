from random import choice
from datetime import datetime, timedelta
print("-="*25)
print(f"{'PROGRAMACAO DE REUNIOES DE SERVICO DE CAMPO':^50}")
print("-="*25 +'\n')
while True:  # Menu de opcoes
    print('''MENU:
    [1] DIGITAR CONDUTORES:
    [2] LER ARQUIVO COM DADOS DOS CONDUTORES
    [3] SAIR''')
    opcao = int(input("Digite sua opcao e aperte ENTER: "))
    if opcao == 1:
        f = open('data', 'w')
        conductor_for_wednesday: str = input("Escreva o conductor das quartas: ")
        conductor_for_thursday = input("Escreva o conductor das quintas: ")
        f.write(conductor_for_wednesday + "\n")  # linha 1 condutor da quarta
        f.write(conductor_for_thursday + "\n")  # linha 2 condutor da quinta
        conductors_for_weekend = []
        while True:
            conductor = input("Escreva um condutor de fim de semana (deixe em branco para terminar): ")
            if conductor == "":
                break

            conductors_for_weekend.append(conductor)
        f.write(str(conductors_for_weekend) + "\n")  # linha 3 condutores do fim de semana
        f.close()
        break
    elif opcao == 2:
        try:
            with open('data') as f:
                conductor_for_wednesday = str(f.readline()).replace('\n', '')
                conductor_for_thursday = str(f.readline()).replace('\n', '')
                conductors_for_weekend = str(f.readline()).replace('\n', '').replace('[', '').replace("'", '').replace(
                    "]", '').split(', ')
                f.close()
                break
        except FileNotFoundError:
            print('Arquivos de Datos nao encontrado. Escolha opcao 1 por favor.')
    elif opcao == 3:
        break
    else:
        print('Valor digitado invalido.')


while True:
    try:
        date = datetime.fromisoformat(input("Escreva a data de início (YYYY-MM-DD): "))
        break
    except ValueError:
        print("Data nao válida.")
    finally:
        print("Final")

working_month = date.month
current_month = date.month


def prints(name, date):
    line = date.strftime("%d-%m-%Y") + ": " + name
    
    print(line)
    try:
        d = open('programa.txt', 'a')
        d.write(line + "\n")
        d.close()
    except PermissionError:
        pass

try:
    writable = True
    with open("programa.txt", 'w') as d:
        d.write("Programa de predicación - Congregación PORVENIR LSP\n")
except PermissionError:
    writable = False
    

while current_month <= working_month + 1:
    weekday = date.weekday()
    if weekday == 2:
        prints(conductor_for_wednesday, date)
    elif weekday == 3:
        prints(conductor_for_thursday, date)
    elif weekday == 5 or weekday == 6:
        conductor = choice(conductors_for_weekend)
        prints(conductor, date)

    date = date + timedelta(days=1)
    current_month = date.month

if not writable:
    print("Nao foi possível escrever o arquivo de programacao")