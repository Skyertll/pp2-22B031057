from math import *

#1
def degree_to_radian(degrees):
    return degrees * pi / 180


degree = int(input())
radian = degree_to_radian(degree)
print(f"{degree} degrees is  {radian} radians.")

#2
def trapezoid_area(base1, base2, height):
    return 0.5 * (base1 + base2) * height

base1, base2, height = int(input()), int(input()), int(input())
print(trapezoid_area(base1, base2, height))

#3
def polygon_area(n, s):
    return (n * s ** 2) / (4 * tan(pi / n))

n, s = int(input()), int(input())
print(int(polygon_area(n,s)))

#4
def parallelogram_area(base, height):
    return base * height

base, height = int(input()), int(input())
print(parallelogram_area(base, height))
