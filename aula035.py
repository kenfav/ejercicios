frase = "O rato roeu a roupa do rei de roma"
tamanho = len(frase)
contador = 0

novastring = ''

while contador < tamanho:
    letra = frase[contador]
    if letra == 'o':
        novastring += '0'
        contador += 1
        print(novastring)
    else:
        novastring += letra
        contador += 1
        print(novastring)


