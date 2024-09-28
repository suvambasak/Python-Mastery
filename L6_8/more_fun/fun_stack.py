

# def fact(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x*fact(x-1)


# x = 1000
# result = fact(x)

# print(result)


x = 1000
result = 1

for i in range(1, x+1):
    result *= i

print(result)
