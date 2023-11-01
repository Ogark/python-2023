# Клас Animal є базовим класом для ієрархії класів. Він містить метод __repr__ для представлення об'єктів.
class Animal:
    def __repr__(self):
        return f'{self.__class__.__name__}()'

# Клас Human успадковує від Animal, не має жодних додаткових атрибутів або методів.
class Human(Animal):
    pass

# Клас Person також успадковує від Human і додає атрибут tax_number для представлення податкового номера особи.
class Person(Human):
    def __init__(self, name, tax_number=None):
        self.name = name
        self.tax_number = tax_number

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}(name={self.name!r}, tax_number={self.tax_number!r})'

# Клас Vaccine представляє вакцину та її атрибути, такі як назва, дата та серійний номер.
class Vaccine:
    def __init__(self, name, date, serial_number):
        self.name = name
        self.date = date
        self.serial_number = serial_number

    def __repr__(self):
        return f'Vaccine(name={self.name!r}, date={self.date!r}, serial_number={self.serial_number!r})'

# Клас GenericChip представляє загальний чіп і має атрибути виробника та серійного номеру.
class GenericChip:
    def __init__(self, manufacturer, serial_number):
        self.manufacturer = manufacturer
        self.serial_number = serial_number

    def __repr__(self):
        return f'GenericChip(manufacturer={self.manufacturer!r}, serial_number={self.serial_number!r})'

# Клас DogChip успадковує від GenericChip і не має додаткових атрибутів або методів.
class DogChip(GenericChip):
    pass

# Клас CatChip успадковує від GenericChip і не має додаткових атрибутів або методів.
class CatChip(GenericChip):
    pass

# Клас Pet представляє домашню тварину з власником, інформацією про власника та методами для зміни власника.
class Pet(Animal):
    def __init__(self, owner):
        self.change_owner(owner)

    def change_owner(self, new_owner):
        self.owner = new_owner

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, value):
        if isinstance(value, Person):
            self.__owner = value
        else:
            err = f'{value!r} must be an instance or subclass of Person.'
            raise ValueError(err)

    def __repr__(self):
        clsname = self.__class__.__name__
        return f'{clsname}(owner={self.owner!r})'

# Клас Enterprise представляє підприємство, яке може володіти домашніми тваринами та має методи для додавання, видалення та отримання списку володіних тварин.
class Enterprise:
    def __init__(self, name):
        self.name = name
        self.owned_pets = []

    def add_pet(self, pet):
        self.owned_pets.append(pet)

    def remove_pet(self, pet):
        self.owned_pets.remove(pet)

    def get_owned_pets(self):
        return self.owned_pets

if __name__ == '__main__':
    # Створення об'єктів осіб (Person) з податковими номерами.
    person1 = Person(name="John", tax_number="1234567890")
    person2 = Person(name="Alice", tax_number="9876543210")

    # Створення об'єкта вакцини.
    vaccine1 = Vaccine(name="COVID-19", date="2023-01-15", serial_number="VAC123")
    
    # Створення об'єктів чіпів для собак та котів.
    dog_chip = DogChip(manufacturer="ChipCo", serial_number="DOGCHIP001")
    cat_chip = CatChip(manufacturer="ChipCo", serial_number="CATCHIP001")

    # Створення домашніх тварин і надання їм власників.
    pet1 = Pet(owner=person1)
    pet2 = Pet(owner=person2)
    
    # Створення підприємства та додавання до нього домашніх тварин.
    enterprise = Enterprise(name="My Enterprise")
    enterprise.add_pet(pet1)
    enterprise.add_pet(pet2)

    # Виведення інформації про створені об'єкти.
    print("Person1:", person1)
    print("Person2:", person2,"\n")
    print("Vaccine:",vaccine1,"\n")
    print("Dog_chip:", dog_chip)
    print("Cat_chip:", cat_chip,"\n")
    print("Pet1:", pet1)
    print("Pet2:",pet2,"\n")

    # Виведення інформації про домашніх тварин, що належать підприємству.
    owned_pets = enterprise.get_owned_pets()
    for pet in owned_pets:
        print(f"{enterprise.name} owns {pet} owned by {pet.owner.name}.","\n")
