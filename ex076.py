lista = ('CEL SAMSUNG A12','US$ 158,00',
'CEL SAMSUNG M21S','US$ 199,00',
'CEL SAMSUNG M21S','US$ 199,50',
'CEL SAMSUNG M31','US$ 213,00',
'CEL SAMSUNG M31','US$ 213,00',
'CEL SAMSUNG M31','US$ 219,50',
'CEL XIAOMI MI 10','US$ 330,00',
'CEL XIAOMI NOTE 9','US$ 155,00',
'CEL XIAOMI NOTE 9T','US$ 239,00',
'CEL XIAOMI REDMI 9','US$ 120,00',
'CEL XIAOMI REDMI 9','US$ 120,00',
'CEL XIAOMI REDMI 9','US$ 120,00',
'CEL XIAOMI REDMI 9A','US$ 106,50',
'CEL XIAOMI REDMI 9A','US$ 99,50',
'CEL XIAOMI REDMI 9C','US$ 121,00',
'CEL XIAOMI REDMI 9C','US$ 121,00',
'CEL XIAOMI REDMI 9I','US$ 125,00',
'CEL XIAOMI REDMI 9I','US$ 125,00',
'CEL XIAOMI REDMI 9T','US$ 160,00')

print("{:=^40}".format('Lista de Precos'))
for count, dado in enumerate(lista):
    if count % 2 == 0:
        print(f"{lista[count]:.<25}{lista[count+1]:.>15}")