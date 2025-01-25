
# class Student:

#     def __init__(self, name: str, rollno: int) -> None:
#         self.name: str = name
#         self.rollno: int = rollno
#         self.grade: list[float] = []

#     def add_grade(self, grade: float) -> None:
#         self.grade.append(grade)

#     def get_CPI(self) -> float:
#         return sum(self.grade)/len(self.grade)

#     def __repr__(self) -> str:
#         return f'Name: {self.name}\nRollno: {self.rollno}\nGrade(s): {self.grade}\nCPI: {self.get_CPI()}'

#     def __str__(self) -> str:
#         return f'Name: {self.name}\nRollno: {self.rollno}\nGrade(s): {self.grade}\nCPI: {self.get_CPI()}'


# s = Student('Alice', 1)
# s.add_grade(9.5)
# s.add_grade(8.5)

# print(s)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other.x, self.y * other.y)

    def __truediv__(self, other):
        return Vector(self.x / other.x, self.y / other.y)

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __eq__(self, value):
        pass

    def __ne__(self, value):
        pass

    def __le__(self, value):
        pass

    def __gt__(self, value):
        pass

    def __ge__(self, value):
        pass

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"


class VectorList:

    def __init__(self, *vectors):
        self.vectors = vectors

    def __repr__(self):
        return f"VectorList({', '.join([str(v) for v in self.vectors])})"

    def __len__(self):
        return len(self.vectors)

    def __getitem__(self, index):
        return self.vectors[index]


vl = VectorList(Vector(1, 2), Vector(3, 4), Vector(5, 6))
print(vl)
print(len(vl))

print(vl[2])
