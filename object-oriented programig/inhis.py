class Car:
    total_car = 0
    def __init__(self, userbrand, usermodel):
        self.__brand = userbrand
        self.__model = usermodel
        # self.total_car += 1
        Car.total_car += 1

    def display(self):
        print(f"Car brand is : {self.__brand} and car model is : {self.model}")

    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self):
        return "Petrol and Diesel"

    @staticmethod
    def general_description():
        return "Cars are means of transport"

    @property
    def model(self):
        return self.__model




class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size;

    def fuel_type(self):
        return "Electric Charge"



# my_car = Car("Tata","Safari")

# print(my_car.model)

# my_car.__brand = "volvo"
# print(my_car.__brand)


# #print(Car.general_description())

my_tesla = ElectricCar("Tesla","Model S","85KWH");

print(isinstance(my_tesla,Car))
print(isinstance(my_tesla,ElectricCar))