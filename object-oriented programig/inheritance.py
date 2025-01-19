class Car:
    
    def __init__(self, userbrand, usermodel):
        self.brand = userbrand
        self.model = usermodel

    # def display(self):
    #     print(f"Car brand is : {self.brand} and car model is : {self.model}")

    def full_name(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size;

# my_car = Car("Toyota","Corolla");
# # print(my_car.brand)
# # print(my_car.model)
# print(my_car.full_name())
# # my_car.display()

# my_new_car = Car("Tata","Safari");
# # print(my_new_car.brand);
# # print(my_new_car.model);

my_tesla = ElectricCar("Tesla","Model S","85KWH")
print(my_tesla.model)
print(my_tesla.full_name())