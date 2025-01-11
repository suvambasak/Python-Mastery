from abc import ABC, abstractmethod

############################################
# Static method
############################################


# class Converter(ABC):
#     @abstractmethod
#     def convert(self, value):
#         pass

#     @staticmethod
#     def description():
#         return "This is a converter class"


# class CelsiusToFahrenheit(Converter):
#     def convert(self, value):
#         return (value * 9/5) + 32


# converter = CelsiusToFahrenheit()
# print(converter.convert(0))  # Output: 32.0
# print(CelsiusToFahrenheit.description())  # Output: This is a converter class


############################################
# Shared var
############################################


class Student:

    count = 0

    @staticmethod
    def registration(rollno):
        return f"UEM{rollno}"

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.grade = []
        Student.count += 1

    def add_grade(self, grade):
        self.grade.append(grade)

    def get_CPI(self):
        return sum(self.grade)/len(self.grade)


if __name__ == '__main__':

    print(Student.count)

    s1 = Student("S1", 1)
    print(s1.count)
    print(Student.registration(s1.rollno))

    s2 = Student("S2", 2)
    print(s2.count)

    print(Student.registration(s2.rollno))
    s3 = Student("S3", 3)
    print(s3.count)

    print(Student.count)
    print(s1.count)
    print(Student.registration(s3.rollno))
