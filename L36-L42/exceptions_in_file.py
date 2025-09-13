

import os


if os.path.exists('file'):

    try:

        with open('file', 'r') as file:
            content = file.read()
            print(content)

    except PermissionError:
        print("Permission denied: Unable to read the file.")


os.remove('file')


print(os.access('file', os.R_OK))
print(os.access('file', os.W_OK))
print(os.access('file', os.X_OK))
