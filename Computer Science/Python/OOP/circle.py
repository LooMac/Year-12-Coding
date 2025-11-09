from math import pi

class Circle():
    def __init__(self,inputRadius):
        self.radius = inputRadius

    def calcArea(self):
        return pi * (self.radius ** 2)

    def calcPerim(self):
        return 2 * pi * self.radius

def main():
    circ_1 = Circle(int(input()))
    print(f"The area of the circle is {circ_1.calcArea()}.")

main()
