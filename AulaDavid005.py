#POO
'''Programacao orientada a objetos surgiu nao so para solucionar problemas, se fosse so solucionar problemas, ficariamos
 no Assembly. A ideia e poder alterar o programa facilmente
 A POO ajuda a criar programas faceis de manter e modificar.
 A idea e que a POO seja um modelo do mundo real. Ex: Pessoas, lugares... tem o behavior do objeto
 Adcionar comportamentos sem ter que mudar o codigo existente.
 O codigo tem que ser fechado a modificacao mas aberto a extensao.
 Nao se corre o risco de modificar e quebrar outras partes do programa.
 Principios: separar responsabilidades
 Classes:
 define um tipo de objeto

class Person:
    def __init__(self):
        self.name = ""  #o primeiro parametro do metodo vai ser a instancia da classe com que

    def greet(self):
        print("Hello! I am " + self.name)

class Bethelite(Person):
    def greet(self):
        print("Eu sou " + self.name + "e eu sou um betelita")

p = Person()   # a variavel p vai receber uma nova instancia de um objeto de tipo pessoa
p.name = "Kenisson"                          ## estamos trabalhado
p.greet()
p = Bethelite()
p.name = "Kenisson"
p.greet()
Method is a function associated with a class..

'''


class Bethelites:
    total_de_betelitas = 0


    def __init__(self, nombre, apellido, id, dias_libres, cuenta_gastos, estacionamiento, habitacion, dept, comienzotiempocompleto):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id
        self.dias_libres = dias_libres
        self.cuenta_gastos = cuenta_gastos
        self.estacionamiento = estacionamiento
        self.habitacion = habitacion
        self.dept = dept
        self.seniority =

        Bethelites.total_de_betelitas += 1


    def fullname(self):
        return '{} {}'.format(self.nombre, self.apellido)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employees):
    pass

dev_1 = Developer('Kenisson', 'Favero', 5000)
dev_2 = Developer('Flavia', 'Favero', 6000)

print(dev_2.email)
print(dev_1.email)

