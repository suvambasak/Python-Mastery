'''
Recourse: https://docs.python.org/3/library/dataclasses.html

'''

from dataclasses import dataclass, field
import string
import random


@ dataclass
class Person:
    name: str
    address: str


# class Person:
#     def __init__(self, name: str, address: str):
#         self.name = name
#         self.address = address

#     def __repr__(self):
#         return f"Person(name='{self.name}', address='{self.address}')"


@ dataclass
class Person:
    name: str
    address: str
    blocked: bool = False


# p1 = Person("Suvam Basak", "IIT Kanpur")
# p2 = Person("Name 2", "Delhi")
# p3 = Person("Name 3", "Mumbai")


# person_list = [p1, p2, p3]

# person_list[2].blocked = True

# for p in person_list:
#     print(p)


@ dataclass(frozen=True)
class Person:
    name: str
    address: str
    valid: bool = True


# p1 = Person("Suvam Basak", "IIT Kanpur")
# p2 = Person("Name 2", "Delhi")
# p3 = Person("Name 3", "Mumbai")

# person_list = [p1, p2, p3]

# person_list[1].valid = False

# for p in person_list:
#     print(p)


def generate_id() -> str:
    return "".join(random.choices(string.ascii_letters, k=11))


@ dataclass
class User:
    name: str

    email: str
    password: str
    valid: bool = True
    # id: str = field(default_factory=generate_id)

    id: str = field(init=False, default_factory=generate_id)


u1 = User("Suvam Basak", "suvam@gmail.com", "123456")

print(u1)
