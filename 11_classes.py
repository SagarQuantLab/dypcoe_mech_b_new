class papa:
    
    def __init__(self, car_name, car_maker_name, papa_salary):
        self.car_name = car_name
        self.car_maker_name = car_maker_name
        self.salary = papa_salary

    def __salary_details(self):
        return f"Salary is restricted : Papa"
    
    def _car_details(self):
        return f"Drive my car : Papa"
    
class rohan(papa):

    def __init__(self, car_name, car_maker_name, papa_salary, rohan_salary):
        papa.__init__(self, car_name, car_maker_name, papa_salary)
        self.rohan_salary = rohan_salary

    def access_papa_car(self):
        return self._car_details()
    
    def access_papa_salary(self):
        return self.__salary_details()
    
    def __access_rohan_salary(self):
        return f"Access rohan salary : {self.rohan_salary}"

class sohan(rohan):

    def __init__(self, car_name, car_maker_name, papa_salary, rohan_salary):
        rohan.__init__(self,  car_name, car_maker_name, papa_salary, rohan_salary)

    def run_grandpa_car(self):
        print(self._car_details())
        print(self.access_papa_car())

    def access_granpa_salary(self):
        return self.__salary_details()
    
    def access_papa_salary(self):
        return self._access_rohan_salary()
    

sohanInstance = sohan("Baleno", "Maruti", 50000, 100000)
print(sohanInstance.run_grandpa_car())
# print(sohanInstance.access_granpa_salary())
print(sohanInstance.access_papa_salary())
