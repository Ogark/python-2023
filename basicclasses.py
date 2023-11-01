# Оголошення базового класу "Vehicle"
class Vehicle:
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def get_info(self): 
        print("Creating a new object: ") 
        print("make: ", self.make, 
              ", model: ", self.model,  
              ", Year: ", self.year, 
              ", Color: ", self.color) 

# Оголошення підкласу "Car", успадковує властивості і методи від "Vehicle"        
class Car(Vehicle):
    def __init__(self, make, model, year, color, num_passenger):
        super().__init__(make, model, year, color)
        self.num_passenger = num_passenger

    def get_info(self):
        print(f"The car {self.make} {self.model} is drives with {self.num_passenger} passenger.")

# Оголошення підкласу "Bicycle", успадковує властивості і методи від "Vehicle"
class Bicycle(Vehicle):
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)

    def get_info(self):
        print(f"The bicycle {self.make} {self.model} rides on the field.")

# Оголошення підкласу "Airplane", успадковує властивості і методи від "Vehicle"
class Airplane(Vehicle):
    def __init__(self, make, model, year, color, max_speed):
        super().__init__(make, model, year, color)
        self.max_speed = max_speed

    def get_info(self):
        print(f"The airplane {self.make} {self.model} is airing at a maximum speed of {self.max_speed} kilometers.")
        
# Основна частина програми    

# Створення об'єкта "Vehicle" зі значеннями атрибутів
vehicle = Vehicle('Toyota', 'Camry', 2020, 'red') 
# Вивід інформації про об'єкт "Vehicle"
vehicle.get_info()
 
 # Створення об'єкта "Car" зі значеннями атрибутів та додатковим параметром "num_passenger"
car = Car('Toyota', 'Camry', 2020, 'red', 4)  
car.get_info()
 
bicycle = Bicycle('Ukraine', 'B-120', 1965, 'red') 
bicycle.get_info()

# Створення об'єкта "Airplane" зі значеннями атрибутів та додатковим параметром "max_speed"
airplane = Airplane('Boeing', 777, 2003, 'white', 900) 
airplane.get_info()