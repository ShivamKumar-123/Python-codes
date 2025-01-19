class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel
        # self.total_car += 1
        Car.total_car += 1

    def display(self):
        print(f"Car brand is : {self.__brand} and car model is : {self.model}")

    def full_name(self):
        return f"{self.__brand} {self.model}"
    
    def fuel_type(self):
        return "Petrol and Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"





class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size;

    def fuel_type(self):
        return "Electric Charge"




'''my_tesla = ElectricCar("Tesla","Model S","85KWH")'''


'''
 safari = Car("Tata","Safari");
 safariThree = Car("Tata","Nexon");

'''


my_car = Car("Tata","Safari")
Car("Tata","Nexon")

# par humne inka reference store nhi kiya hai

# print(Car.total_car)
#print(my_car.general_description())
print(Car.general_description())
