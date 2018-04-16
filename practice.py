# repl.it 2.1

# my solution : just consider a as 'string' type
a = input()
print(a[0] + " " + a[1])

# solution
a = int(input())
print(a // 10, a % 10)


# repl.it 2.2

# my solution
a = int(input())
b = a % 10
c = a // 10
print(10*b + c)

# solution
a = int(input())
print(a % 10 * 10 + a // 10


# repl.it 2.3

# my solution
a = int(input())
print((a % 100 - a % 10) + a % 10)

# solution
a = int(input())
print(a % 100)
