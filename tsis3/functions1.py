from math import pi
from random import randint
#1
def grams_to_ounces(grams):
    return 28.3495231 * grams

#2
def fahrenheit_to_centigrade(F):
    return (5 / 9) * (F - 32)

#3
def solve(numheads, numlegs):
    flag = True
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if chickens * 2 + rabbits * 4 == numlegs:
            break
    if flag:
        return chickens, rabbits
    else:
        return 'No solutions'

#4
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True

def filter_prime(input_list):
    input_list.append('end')
    i = 0
    while input_list[i] != 'end':
        if is_prime(input_list[i]):
            i += 1
        else:
            del input_list[i]
    del input_list[-1]
    return input_list

        

'''numbers = [int(i) for i in input().split()]
print(numbers)
print(filter_prime(numbers))'''

#5
def permutate(input_string, first, length):
    input_list = list(input_string)
    if first == length:
        print(''.join(input_list))
    else:
        for i in range(first, length+1):
            input_list[first], input_list[i] = input_list[i], input_list[first]
            permutate(input_list, first + 1, length)
            input_list[first], input_list[i] = input_list[i], input_list[first]
permutate('abcd', 0, len('abcd') - 1)

#6
def reverse(input_string):
    return ' '.join(input_string.split()[::-1])

print(reverse('asd akhl hoikh'))

#7
def has_33(nums):
    for i in range(1, len(nums)):
        if nums[i] == nums[i-1] == 3:
            return True
    return False
print(has_33([1, 3, 1, 3, 1]))

#8
def spy_game(nums):
    for i in range(2, len(nums)):
        if nums[i-1] == nums[i-2] == 0 and nums[i] == 7:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))

#9
def sphere_volume(radius):
    return 4/3*pi*radius**3

print(sphere_volume(3))

#10
def unique_list(input_list):
    res = []
    for i in unique_list:
        if i not in res:
            res.append(i)
    return res

#11
def is_palindrome(input_smth):
    if list(input_smth) == list(input_smth)[::-1]:
        return True
    return False

#12
def histogram(parameters):
    for i in parameters:
        print('*' * i, end='\n')

#13

def compare(number, choice):
    if number > choice:
        print(f'Your guess is too low.\nTake a guess.\n')
        return False
    elif number < choice:
        print(f'Your guess is too high.\nTake a guess.\n')
        return False
    else:
        return True


number = randint(1,20)
counter = 1
name = input('Hello! What is your name?\n')
choice = int(input(f'Well, {name}, I am thinking of a number between 1 and 20.\nTake a guess.\n'))
while not compare(number, choice):
    choice = int(input())
    counter += 1
print(f'Good job, {name}! You guessed my number in {counter} guesses!')
