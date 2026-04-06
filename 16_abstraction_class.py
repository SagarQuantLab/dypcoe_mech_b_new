from abc import ABC, abstractmethod

class Govt(ABC):

    def __init__(self, name, business_type):
        self.name = name
        self.business_type = business_type

    @abstractmethod
    def get_license_first(self):
        return f"License approved for {self.business_type} : Owner Name {self.name}"
    

class Pizza(Govt):

    def __init__(self, owner_name, owner_business):
        Govt.__init__(self, owner_name, owner_business)

    def get_license_first(self):
        return "I got the license"

pizzaIns = Pizza("Rohan", "PizzaShop")
print(pizzaIns.get_license_first())