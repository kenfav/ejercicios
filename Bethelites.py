class Bethelites:
    total_de_betelitas = 0

    def __init__(self, nombre, apellido, id, dept, comienzotiempocompleto):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.dept = dept
        self.comienzotiempocompleto = comienzotiempocompleto

        Bethelites.total_de_betelitas += 1

    def fullname(self):
        return '{} {}'.format(self.nombre, self.apellido)


class BBR(Bethelites):
    totalbbr = 0

    def __init__(self, nombre, apellido, id, cuenta_gastos, estacionamiento, habitacion, dept, comienzotiempocompleto):
        super().__init__(nombre, apellido, id, dept, comienzotiempocompleto)
        self.cuenta_gastos = cuenta_gastos
        self.estacionamiento = estacionamiento
        self.habitacion = habitacion
        BBR.totalbbr += 1


class BBV(Bethelites):
    totalbbv = 0

    def __init__(self, nombre, apellido, id, dept, comienzotiempocompleto, diastrabajo=None):
        super().__init__(nombre, apellido, id, dept, comienzotiempocompleto)
        if diastrabajo is None:
            self.diastrabajo = []
        else:
            self.diastrabajo = diastrabajo
        BBV.totalbbv += 1

    def adcionardias(self, dias):
        if dias not in self.diastrabajo:
            self.diastrabajo.append(dias)

    def removerdias(self, dias):
        if dias in self.diastrabajo():
            self.diastrabajo.remove(dias)

    def listardias(self):
        if self.diastrabajo is None:
            print("Este voluntario nao trabalha nenhum dia")
        else:
            for dia in self.diastrabajo:
                print(dia, end=' ')



print(f'O total de BBV e de {BBV.totalbbv} pessoas.')
print(f"O total de betelitas foi de {Bethelites.total_de_betelitas} pessoas.")
print(f"o total de BBR foi de {BBR.totalbbr} pessoas.")

bbv1 = BBV("Juan", "El Bautista", 6668855, "Servicio", 2018, ['Miercoles','Jueves'])
bbv2 = BBV("Maxi", "Paz", 6669999, "TRANS", 2002)
bbr1 = BBR("David", "de Belem", 8885562, 500.25, 18, 1001, "LDC", 2025)

print(f'O total de BBV e de {BBV.totalbbv} pessoas.')
print(f"O total de betelitas foi de {Bethelites.total_de_betelitas} pessoas.")
print(f"o total de BBR foi de {BBR.totalbbr} pessoas.")

