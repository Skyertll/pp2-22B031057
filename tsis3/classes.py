#1
class test_string:
    def getString(self, input_string):
        self.value = input_string

    def printString(self):
        print(self.value.upper())

#2 & 3
class Shape:
    def __init__(self, length = 0, width = 0):
        self.length = length
        self.width = width

    def area(self):
        if self.length and not self.width:
            return self.length**2
        elif self.length and self.width:
            return self.length*self.width
        else:
            return 0
    
class Square(Shape):
    def __init__(self, length, width = 0):
        super(Shape, self).__init__()
        self.length = length
        self.width = width
    

class Rectangle(Shape):
    def __init__(self, length, width):
        super(Shape, self).__init__()
        self.length = length
        self.width = width


#4
class Point:
    def __init__(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def show(self):
        print(f'({self.x_coordinate};{self.y_coordinate})')

    def move(self, new_x, new_y):
        self.x_coordinate = new_x
        self.y_coordinate = new_y

    def dist(self, new_point):
        return ((self.x_coordinate - new_point.x_coordinate)**2 + (self.y_coordinate - new_point.y_coordinate)**2)**0.5

#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Средства успешно начислены. Баланс - {self.balance}$')

    def withdraw(self, amount):
        if amount > self.balance:
            print('Недостаточно средств')
        else:
            self.balance -= amount
            print(f'Выведено {amount}$, остаток на счетy - {self.balance}$')

Grisha = Account('Grisha', 500)
Vasya = Account('Vasya', 600)

for _ in range(3):
    Vasya.withdraw(500)

for _ in range(3):
    Grisha.deposit(200)

#6
def is_prime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True

def filter(input_list):
    input_list.append('end')
    i = 0
    while input_list[i] != 'end':
        if is_prime(input_list[i]):
            i += 1
        else:
            del input_list[i]
    del input_list[-1]
    return input_list

        

n = int(input())
numbers = [i for i in range(n)]
print(numbers)
print(filter(numbers))