
'''https://docs.python.org/3/library/typing.html'''


def merge(
        a: int | float | list[any],
        b: int | float | list[any]
) -> int | float | list[any]:
    print(a + b)


merge(1, 2)
merge(1.0, 2.0)
merge('hello', ' world')
merge([1, 2], [3, 4])

# merge([], set())
