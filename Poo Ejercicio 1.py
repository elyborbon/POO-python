class Estudiante:
    #Atributos
    def __init__(self, nombre, edad, grado ):
        self.nombre = nombre 
        self.edad = edad
        self.grado = grado

    def estudiar (self):
        print ("Estudiando:....")

nombre = input ("Diga su nombre: ")
edad = input ("Ahora su edad: ")
grado = input ("Por ultimo, su grado: ")

estudiante = Estudiante(nombre, edad, grado)

print (f""" DATOS DEL ESTUDIANTE: \n \n
        Nombre: {estudiante.nombre} \n
        Edad: {estudiante.edad} \n
        Grado: {estudiante.grado} \n
        """
       )
