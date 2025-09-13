

import sys


# data_list = [i for i in range(100)]

# print(sys.getsizeof(data_list))


def count_to_n(n):
    i = 0
    while i < n:
        yield i
        i += 1


my_generator = count_to_n(5)

print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))
print(next(my_generator))

