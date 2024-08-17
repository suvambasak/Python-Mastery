import sys


# print(sys.stdin)
# print(sys.stdout)
# print(sys.stderr)


# sys.stdout.write('hello')
# sys.stderr.write('hello')
# sys.stdin.write('hello')


my_stdout = open('stdout', 'w')
sys.stdout = my_stdout

print('Hello')


# my_stderr = open('stderr', 'w')
# sys.stderr = my_stderr

# value = 3/0

my_stdin = open('stderr', 'r')
sys.stdin = my_stdin

value = input()

print(value)
