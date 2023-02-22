#1
def squares_to_N(N):
    for i in range(1, N+1):
        yield i*i

n = int(input())
for i in squares_to_N(n):
    print(i)

#2
def even_numbers(n):
    for i in range(0, n+1, 2):
        yield i

n = int(input())
print(",".join(str(x) for x in even_numbers(n)))

#3
def divisible_by_3_and_4(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input())
for number in divisible_by_3_and_4(n):
    print(number)

#4
def squares(a, b):
    for i in range(a, b+1):
        yield i*i

a, b = int(input()), int(input())
for i in squares(a, b):
    print(i)

#5
def countdown(n):
    for i in range(n, -1, -1):
        yield i

n = int(input())
for i in countdown(n):
    print(i)


