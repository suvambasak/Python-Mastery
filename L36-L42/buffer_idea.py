

import time

f = open('new_file', 'w')


while True:
    time.sleep(1)

    f.write('Hello, World!\n')
    f.flush()

f.close()
