# '''
# Scope rule: LEGB
# - Local
# - Enclosing
# - Global and Built-in scopes
# '''


x = 'hello'


def outer_fun():
    x = 'outer_fun'

    def inner_fun():

        nonlocal x

        print(x)

        x = 'UEM'

        print(x)

    inner_fun()
    print(x)


outer_fun()
# print(x)


# def inner_fun():
#     x = 'inner_fun'
#     pprint.pprint(locals())
#     pprint.pprint(globals())
#     print(x)

# def fun_2():
#     print('_____INSIDE OF FUN_2________')
#     x = 'fun_2'
#     # pprint.pprint(locals())
#     # pprint.pprint(globals())
#     print(x)
#     print('__________________________')


# def fun_1():
#     print('_____INSIDE OF FUN_1________')
#     x = 'fun_1'
#     # pprint.pprint(locals())
#     # pprint.pprint(globals())
#     print(x)
#     print('__________________________')


# print('_____OUTSIDE OF FUN________')
# # pprint.pprint(locals())
# # pprint.pprint(globals())
# print(x)
# print('__________________________')


# fun_1()
# fun_2()
