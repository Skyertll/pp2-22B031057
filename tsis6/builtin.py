#1
from functools import *
numbers = [1, 456, 95, 34, 346, 38]
result = reduce(lambda x, y: x*y, numbers)
print(result)

#2
string = "Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters"
upper_count = 0
lower_count = 0

for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1

print(upper_count)
print(lower_count)

#3
def is_palindrome(string):
    string = string.replace(" ", "")
    string = string.lower()
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False
    
#4
import time
import math

number = int(input())
delay = int(input())

delay = delay / 1000
time.sleep(delay)
sqrt = math.sqrt(number)

print(f'Square root of {number} after {delay}*1000 milliseconds is {sqrt}')

#5
def all_true(tuple):
    return all(tuple)

tuple1 = (True, True, True)
tuple2 = (True, False, True)

if all_true(tuple1):
    print(tuple1, "contains only true values")
else:
    print(tuple1, "contains at least one false value")

if all_true(tuple2):
    print(tuple2, "contains only true values")
else:
    print(tuple2, "contains at least one false value")