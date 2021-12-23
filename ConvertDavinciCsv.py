import tkinter as tk
from tkinter import filedialog

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

    def print_contents(self, event):
        print("Hi. The current entry content is:",
              self.contents.get())

root = tk.Tk()
root.title('Davinci CSV Converter')
root.geometry("200x200")


def open_file():
    root.filename = filedialog.askopenfilename(initialdir=".", title="Select a file",
                                               filetypes=[("Csv Files", "*.csv"), ("EDL Files", "*.edl")])

def do_save():
    if str(root.filename[-3:]).lower() == 'csv':
        with open(root.filename, 'r') as i:  # Generar lista con base en el archivo CSV
            archivo = []
            for linea in i:
                archivo.append(linea)
        lista = []
        for linea in archivo:  # Generar una lista 2d con las lineas de la primera lista
            columna = []
            for col in linea.replace('"', '').split(","):
                columna.append(col)
            lista.append(columna)

        for linea in range(len(lista)):  # Hacer cambios en las strings de la lista para que sea el formato sea el deseado
            for columna in range(len(lista[linea])):
                if columna != 19:  # Col number where the chapter markers is. We don't want to change a : for a ; here
                    for n, s in enumerate(lista[linea]):
                        lista[linea][columna] = lista[linea][columna].replace(":", ";").replace(" ", "")

        with open(output_file, 'w') as t:  # Escribir el header del archivo csv
            t.write("Marker Name\tDescription\tIn\tOut\tDuration\tMarker Type\t\n")

        with open(output_file, 'a') as o:
            for i, linea in enumerate(lista):
                if i == 0:  # ignora el header de la lista original
                    pass
                else:
                    o.write(linea[19])
                    o.write("\t\t")
                    if linea[6][:2] == "01":
                        o.write("00")
                        o.write(linea[6][2:])
                    else:
                        o.write(linea[6])
                    o.write("\t")
                    if linea[7][:2] == "01":
                        o.write("00")
                        o.write(linea[7][2:])
                    else:
                        o.write(linea[6])
                    o.write("\t")
                    o.write("00;00;00;00")
                    o.write("\t")
                    o.write("Chapter")
                    o.write("\t")
                    o.write("\n")
        print(f"Sucessful {output_file} file generated.")

    elif str(root.filename[-3:]).lower() == 'edl':
        print("Es un archivo EDL")


def where_save():
    global output_file
    root.output_dir = filedialog.askdirectory(initialdir=".", title="Save the exported CSV file in")
    output_file_full_path = str(root.filename).split("/")
    output_file = root.output_dir + "/" + output_file_full_path[-1]
    
    do_save()


button1 = tk.Button(root, text="Select a Davinci Resolve CSV File", command=open_file).pack()
button2 = tk.Button(root, text='Save Converted CSV File To', command=where_save).pack()

myapp = App(root)
myapp.mainloop()