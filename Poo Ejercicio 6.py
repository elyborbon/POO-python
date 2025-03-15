class Circle:
    radius = 5

    def __init__(self, color):
        self.color= color 

print (Circle.radius)

my_circle = Circle ("Blue")
you_circle = Circle ("Green")

print (my_circle.radius)
print (my_circle.radius)

Circle.radius = 10

print (Circle.radius)
print (my_circle.radius)
print (you_circle.radius)
    
