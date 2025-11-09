
class Vehicle():
    transportationType = "rail"
    
    def __init__(self,maxSpeed,mileage,transportationType):
        self.maxSpeed = maxSpeed
        self.mileage = mileage


    def show(self):
        print(f"The maximum speed for this vehicle is {self.maxSpeed} mph, and its current mileage is {self.mileage} miles.")
        print(f"\nThe transportation type of this vehicle is {self.transportationType}.")

    @classmethod
    def newType(cls,newType):
        cls.transportationType = newType
        print(f"The new transportation type of this vehicle is {cls.transportationType}")
        
    
def main():
    veh_1 = Vehicle(220,2050,"road")
    veh_1.show()
    veh_1.newType(input())

if __name__ == "__main__":
    main()
