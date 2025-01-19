class Human:

    population = 0
    data = []
    def __init__(self , name ,age):
        self.name = name
        self.age = age
        # self.population += 1
        Human.population += 1
        # self.data.append(self.name)
        Human.data.append(self.name)


r = Human("Rahul",23)
print(r.population)
print(Human.population)

print(r.data)
print(Human.data)