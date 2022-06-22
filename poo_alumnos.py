# En este segundo ejercicio, tendréis que crear un programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota. 
# Deberéis de definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

# Creo la clase
class Alumno():
    # Los atributos
    def inicializar(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota
    # Los metodos
    def imprimir(self):
        print("El alumno", self.nombre, "tiene un ", self.nota)

    def resultado(self):
        if self.nota < 6:
            print("El alumno reprobó")
        else:
            print("El alumno aprobó")

# Creo los objetos
alumno1 = Alumno()
alumno2 = Alumno()

alumno1.inicializar("Gabriel",10)
alumno2.inicializar("Gatik",2)

alumno1.imprimir()
alumno1.resultado()
alumno2.imprimir()
alumno2.resultado()