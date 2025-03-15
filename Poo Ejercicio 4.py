class Backpack:
    def __init__(self, color):
        self.items = []
        self.color = color

my_Backpack = Backpack("Blue")
your_backpack = Backpack ("Red")

print (my_Backpack.color)
print (your_backpack.color)

print ("Changig Color .....")
my_Backpack.color = "Green"

print (my_Backpack.color)
print (your_backpack.color)