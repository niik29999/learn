class Car:

    wheels_number = 4

    def __init__(self, name, color, year, is_crashed):
        self.name = name
        self.color = color
        self.year = year
        self.is_crashed = is_crashed
        print('Car is created')

    def drive(self, city):      # метод класса
        print(self.name + ' is driving to ' + city)

    def change_color(self, new_color):
        self.color = new_color
        print('Color is changed to ' + new_color)


mazda_car = Car(name='Mazda CX7', color='red', year=2017, is_crashed=True)

print(mazda_car.name)
print(mazda_car.is_crashed)
print(mazda_car.wheels_number)

bmw_car = Car(name='BMW', color='black', year=2018, is_crashed=False)

print(bmw_car.name)
print(bmw_car.year)
print(bmw_car.wheels_number)

opel_car = Car('Opel Tigra', 'grey', '1999', True)
opel_car.drive('London')
mazda_car = Car('Mazda CX7', 'black', 2014, False)
mazda_car.drive('Paris')
mazda_car.change_color('yellow')
print(mazda_car.color)

# Inheritance
class Truck(Car):

    wheels_number = 6

    def __init__(self, name, color, year, is_crashed):
        Car.__init__(self, name, color, year, is_crashed)
        print('Truck is created')

    def drive(self, city):
        print('Truck ' + self.name + ' is driving to ' + city)

    def load_cargo(self, weight):
        print('The cargo is loaded. Weight is ' + str(weight) + ' kg')


man_truck = Truck('Man', 'white', 2015, False)

man_truck.drive('New York')
print(man_truck.wheels_number)
print(man_truck.color)
man_truck.change_color('red')
print(man_truck.color)
man_truck.load_cargo(2000)

# Polymorphis
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError('Class successor must implement '
                                  'this method')


class Dog(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying woof')


class Cat(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying meow')


class Mouse(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying pee-pee-pee')

class Fish(Animal):
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name + ' is saying nothing')


spike = Dog('Spike')
tom = Cat('Tom')
jerry = Mouse('Jerry')
freddy = Fish('Freddy')

pet_list = [spike, tom, jerry, freddy]

for pet in pet_list:
    pet.speak()

def pet_voice(pet):
    pet.speak()

pet_voice(spike)
pet_voice(tom)
pet_voice(jerry)


pet_voice(freddy)