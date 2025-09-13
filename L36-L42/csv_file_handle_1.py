

import csv


# Read CSV
# As a LIST
# with open('people-100.csv') as file:


#     reader = csv.reader(file)

#     # Skip the header row
#     header = next(reader)
#     print(header)

#     for row in reader:
#         print(row)

# with open('people-100.csv') as file:
#     reader = csv.DictReader(file)

#     for row in reader:
#         print(row)

# Write CSV

# data = [
#     ['Name', 'Age', 'City'],
#     ['Alice', 25, 'New York'],
#     ['Bob', 30, 'San Francisco']
# ]

# with open('output.csv', 'w') as file:
#     writer = csv.writer(file)

#     # writer = csv.writer(
#     #     file,
#     #     delimiter=';',
#     #     quotechar='"',
#     #     quoting=csv.QUOTE_NONNUMERIC
#     # )

#     # writer.writerow(['Name', 'Age', 'City'])
#     # writer.writerow(['Suvam', '25', 'Kolkata'])

#     writer.writerows(data)

# employees = [
#     {'name': 'Alice', 'age': 25, 'department': 'Engineering'},
#     {'name': 'Bob', 'age': 30, 'department': 'Marketing'},
#     {'name': 'Carol', 'age': 28, 'department': 'Sales'}
# ]


# with open('output.csv', 'w') as file:
#     writer = csv.DictWriter(file, fieldnames=['name', 'age', 'department'])

#     # writer = csv.writer(
#     #     file,
#     #     delimiter=';',
#     #     quotechar='"',
#     #     quoting=csv.QUOTE_NONNUMERIC
#     # )

#     # writer.writerow(['Name', 'Age', 'City'])
#     # writer.writerow(['Suvam', '25', 'Kolkata'])

#     writer.writerows(employees)


# Traditional read and csv read

# # Memory 469 MB
# with open('people-2000000.csv') as file:
#     content = file.read()
#     print(content)

# Memory 3.8 MB
with open('people-2000000.csv') as file:
    reader = csv.reader(file)

    # print(type(reader))
    for row in reader:
        print(row)
