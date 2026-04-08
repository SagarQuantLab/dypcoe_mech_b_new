class Mathematics:

    def __init__(self, a, b):
        self.first_num = a
        self.second_num = b

    def addition(self, a, b):
        return a + b
    
    @staticmethod
    def subtraction(a, b):
        return a - b
    
# mathematicsIns = Mathematics(2, 3)
# print(mathematicsIns.addition(mathematicsIns.first_num, mathematicsIns.second_num))

# print(Mathematics.subtraction(mathematicsIns.first_num, mathematicsIns.second_num))
subtraction = Mathematics.subtraction(4, 5)
print(subtraction)