def edl2csv(filename):
    with open(filename, 'r') as i:  # Generar lista con base en el archivo CSV
        archivo = []
        for linea in i:
            archivo.append(linea)
    listaparte1 = []
    listaparte2 = []
    for n, linea in enumerate(archivo):  # Generar una lista 2d con las lineas de la primera lista
        if n in range(2,len(archivo),3):
            pass
        if n in range (3, len(archivo), 3):
            listaparte1.append(linea.replace('\n','').split(' '))
        if n in range(4, len(archivo), 3):
            listaparte2.append(linea.replace('\n','').split('|'))
    print(listaparte1)
    print(listaparte2)







edl2csv("C:/Users/ken_f/Desktop/CA-cotk21_S_005.edl")
exit()



