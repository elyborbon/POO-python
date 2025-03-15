
#El 5 es un numero respaldo en caso de que no se agregue valor 
#los valores definidos como radius = 5 deben de ir al final para no interfer con los demas atributos
class Circle: 
    def __init__(self, color, radius =5,  ):
        self.radius =radius 
        self. color = color
my_circle = Circle( "blue")
print (my_circle.radius)
print (my_circle.color)
        