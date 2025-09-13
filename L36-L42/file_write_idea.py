
# Bascic file operations in Python

# with open('file', 'w') as file:
#     file.write('Hello, World!\n')


# with open('file', 'a') as file:
#     file.write('Hello, World!\n')


# with open('file', 'r') as file:
#     content = file.read()
#     print(content)


# with open('file', 'r') as file:
#     # content = file.readline()
#     content = file.readlines()
#     print(content)


# Advanced file operations

# with open('file', 'r') as file:
#     file.seek(10)
#     content = file.read()
#     print(content)

# with open('file', 'r') as file:
#     file.seek(33)
#     position = file.tell()
#     print(position)


# with open('file', 'r') as file:
#     content = file.read(10)
# content = file.read()
# print(content)


# with open('file', 'a') as file:
#     file.truncate(6)


# Binary file operations

# with open('file', 'rb') as file:
#     content = file.read()
#     print(content)


# with open('solarCycle.png', 'rb') as file:
#     content = file.read()
#     # Decoding might not work for binary files, but this is just an example
#     print(content.decode('utf-8', errors='ignore'))
