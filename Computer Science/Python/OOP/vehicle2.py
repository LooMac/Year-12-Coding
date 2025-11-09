

class Vehicle():
    transportationType = "track"
    
    def __init__(self, given_max_speed, given_mileage):
        self.maxSpeed = given_max_speed
        self.mileage = given_mileage

    @classmethod
    def setTransType(cls, given_trans_type):
        cls.transportationType = given_trans_type
    
class Car(Vehicle):

    def carInfo(self):
        print(f"The maximum speed for this car is: {self.maxSpeed} its mileage is {self.mileage}")
        print(f"This car is designed to run on {self.transportationType}")
        
class SportCar(Car,Vehicle):

    def carInfo(self):
        print(f"\nThe maximum speed for this sport car is: {self.maxSpeed} its mileage is {self.mileage}")
        print(f"This sport car is designed to run on {self.transportationType}")

sport_car_1 = SportCar(200,1000)

sport_car_1.setTransType("road")

sport_car_1.carInfo()
