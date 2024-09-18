print("Programacion POO")
# Definicion de clase
class Perro:
    #FUNCIONES dentro de la clase
    nombre="Boby"
    edad= 4
    def morder(self):
        print("El perro me mordio")
    def Datos_perro(self, nombre, edad):
        print(f" Nombre : {nombre} edad : {edad}")


# zona creacion de objetos
pitbull= Perro()


#zona uso de objetos
pitbull.Datos_perro("Boby",4)
pitbull.morder()