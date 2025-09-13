

import yaml


# Writing YAML


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


# yaml.dump(students, open("students.yaml", "w"))

# Reading YAML

content = yaml.safe_load(open("students.yaml", "r"))

print(content)
