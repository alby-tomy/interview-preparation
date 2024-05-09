class Circle:
    pi = 3.14 #class attribute
    
    def __init__(self,radius):
        self.radius = radius #instance arrtibute
        
    def display(self):
        print("Radius : {}".format(self.pi * self.radius **2))
        
    
area = Circle(6)
area.display()