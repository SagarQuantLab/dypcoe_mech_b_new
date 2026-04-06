from abc import ABC, abstractmethod

class College(ABC):

    def __init__(self, name, section):
        self.name = name
        self.section = section

    @abstractmethod
    def come_in_dress_code(self):
        pass

class Tejas(College):

    def __init__(self, student_name, student_section):
        College.__init__(self, student_name, student_section)

    def come_in_dress_code(self):
        return "I came in dress code"

tejasIns = Tejas("Tejas", "B")
print(tejasIns.come_in_dress_code())