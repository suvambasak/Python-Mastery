class Student:

    def __init__(self, name: str, rollno: int) -> None:
        self.name: str = name
        self.rollno: int = rollno
        self.grade: list[float] = []

    def add_grade(self, grade: float) -> None:
        self.grade.append(grade)

    def get_CPI(self) -> float:
        return sum(self.grade)/len(self.grade)


students_list: list[Student] = []

students_list.append(Student('Alice', 1))
students_list.append(Student('Bob', 2))
students_list.append(Student('Charlie', 3))

for student in students_list:
    student.add_grade(9.5)
    student.add_grade(8.5)
    student.add_grade(7.5)

for student in students_list:
    print(f'{student.name} has CPI: {student.get_CPI()}')


# l = [
#     [1, 2, 3],
#     [1.0, 2.0, 3.0]
# ]


# l: list[
#     list[int],
#     list[float]
# ] = [
#     [1, 2, 3],
#     [1.0, 2.0, 3.0]
# ]
