
import json


# Write JOSN

# students = {
#     "S001": {
#         "name": "Alice Johnson",
#         "age": 20,
#         "grade": "Sophomore",
#         "courses": ["Math 201", "Physics 101", "English 102"],
#         "gpa": 3.8,
#         "contact": {
#             "email": "alice.johnson@example.com",
#             "phone": "555-1234"
#         }
#     },
#     "S002": {
#         "name": "Bob Martinez",
#         "age": 22,
#         "grade": "Senior",
#         "courses": ["Chemistry 301", "Biology 202", "Philosophy 101"],
#         "gpa": 3.5,
#         "contact": {
#             "email": "bob.martinez@example.com",
#             "phone": "555-5678"
#         }
#     },
#     "S003": {
#         "name": "Catherine Lee",
#         "age": 19,
#         "grade": "Freshman",
#         "courses": ["Computer Science 101", "History 100", "Art 110"],
#         "gpa": 3.9,
#         "contact": {
#             "email": "catherine.lee@example.com",
#             "phone": "555-9012"
#         }
#     }
# }


# json.dump(
#     students,
#     open("students.json", "w"),
#     indent=1,
# )


# Read JSON

# students = json.load(open("students.json", "r"))

# print(type(students))


class Hello:

    def __init__(self):
        self.name = "Hello"

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __dict__(self):
        return {"name": self.name}


record = dict()

record["name"] = "Fname Lname"
record["age"] = 30
record["grade"] = [1, 2, 3, 4, 5, 6, 7]
record["active"] = True

record["Phone"] = None

record["email"] = (
    'fname.lname@example.com',
    'fname.lname@workplace.com'
)

# record['hello'] = Hello()


json.dump(
    record,
    open("record.json", "w"),
    indent=4,
)
