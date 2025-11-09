from math import pi
from abc import ABC, abstractmethod

##################################### COST CALCULATIONS #####################################

class Cost():
    # Cost of each component of the order has a price (per m^2), area, and a calculated cost.
    # Only Labour uses VAT
    _vat = 1.2
    _discount = None
    
    def __init__(self, given_area):
        self._price = None
        self._area = given_area
        self._cost = None
        
    def _apply_disc(self):
        return self._cost * self._discount

    def show_cost(self):
        print(f"\nThis will cost you £{self._cost}")


class Carpet(Cost):
    _discount = 0.85

    def __init__(self, given_area):
        Cost.__init__(self, given_area)
        self.__type_price = [19.99, 12.49, 24.49, 33.59]
        self._cost = self.__calc_cost()
    
    def __choose_price(self):
        print(f"\nCarpets : \n1 - Duchess Twist Carpet: £{self.__type_price[0]}\n2 - Hamptons Twist Carpet: £{self.__type_price[1]}\n3 - Columbus Patterned Carpet: £{self.__type_price[2]}\n4 - Soho Stripe Loop Carpet: £{self.__type_price[3]}")

        while True:
            try:
                choice_index = int(input("\nWhich carpet do you choose 1-4 ?:\n\n")) - 1
                
                if choice_index in range(3):
                    break
                else:
                    raise ValueError
            except:
                print("\nInvalid input, try again.")

        self._price = self.__type_price[choice_index]

    def __calc_cost(self):
        self.__choose_price()
        
        if self._area >= 20:
            print("\nYou qualify for a 15% discount on your carpet price.")
            return round(self._area * self._price * self._discount, 2)
        else:
            return round(self._area * self._price, 2)

        
class Underlay(Cost):
    def __init__(self, given_area):
        Cost.__init__(self, given_area)

    def __choose_price(self):
        self._price = float(input("\nWhat is the price per m² of your underlay?:\n\n"))

    def __calc_cost(self):
        self.__choose_price()

        self._cost = self._price * self._area

    
class Labour(Cost):
    def __init__(self, given_area):
        Cost.__init__(self, given_area)


class Room():
    def __init__(self):
        self.__shape = Rectangle("room")
        
        self.__obj_to_rem = [
            Rectangle("cupboard"),
            Triangle("tiles"),
            Rectangle("shelf"),
            Circle("table")
        ]
        
        self.__total_area = self.__calc_total_area()
    
    def __calc_total_area(self):
        temp = self.__shape.get_area()

        for obj in self.__obj_to_rem:
            if temp <= 0:
                print("Invalid measurements.")
                break
            else:
                temp -= obj.get_area()
        
        return round(temp,2)
    
    def set_area(self, given_area):
        self.__total_area = given_area

    def get_area(self):
        return self.__total_area

    def show_area(self):
        print(f"Total floor space to cover is {self.__total_area} m²")

##################################### AREA CALCULATIONS #####################################

class Shape(ABC): 

    def _input_dims(self, given_name, is_circle = False):
        if is_circle:
            while True:
                try:
                    return(float(input(f"Enter the diameter of the {given_name.lower()}:\n\n")))
                except:
                    print("\nInvalid diameter entered, try again.\n\n")
        else:
            while True:
                try:
                    return(float(input(f"Enter the width of the {given_name.lower()}:\n\n")), float(input(f"Enter the length of the {given_name.lower()}:\n\n")))
                except:
                    print("\nInvalid dimensions entered, try again.\n\n")

    
    def get_area(self):
        return self._area

    @abstractmethod
    def calc_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, given_name):
        self.__dims = self._input_dims(given_name)
        self._area = self.calc_area()

    def calc_area(self):
        return self.__dims[0] * self.__dims[1]

class Triangle(Shape):
    def __init__(self, given_name):
        self.__dims = self._input_dims(given_name)
        self._area = self.calc_area()
    
    def calc_area(self):
        return (self.__dims[0] * self.__dims[1]) / 2


class Circle(Shape):
    def __init__(self, given_name):
        self.__dims = self._input_dims(given_name, True)
        self._area = self.calc_area()
    
    def calc_area(self):
        return pi * ((self.__dims / 2) ** 2)
    

if __name__ == "__main__":
    room_1 = Room()

    room_1.show_area()

    carp_1 = Carpet(room_1.get_area())

    carp_1.show_cost()
