#--------------------------------------
# Question 1
# Question:

# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

# for item in range(2000, 3201):
#   if not item % 7 and item % 5:
#     print(item,end=",")
# print("\b")

#--------------------------------------
# Question 2
# Question:

#     Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8 Then, the output should be:40320

# from time import time

# n = int(input('enter factorial: '))

# t1 = time()

# def fact(n):
#     itr = iter(range(1, n + 1))
#     total = 1
#     for current in itr:
#         total *= current
#         yield total

# for item in fact(n):
#     item
# print(item)
# t2 = time()
# print(f'iterator timer: {round(t2 - t1, 3)}')

# t1 = time()

# def shortFact(x):
#     if x <= 1:
#         return 1
#     else:
#         return x * shortFact(x - 1)

# print(shortFact(n))
# t2 = time()
# print(f'recursion timer: {round(t2 - t1, 3)}')

#--------------------------------------
# Question 3
# Question:

#     With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 8

#     Then, the output should be:

# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# def squaredDict(n):
#   main = {}
#   for number in range(n, 0, -1): #reversed :)
#     main[number] = number**2
#     #or
#     #main.setdefault(number, number**2)
#   return main
# print(squaredDict(100))

#--------------------------------------
# Question 4
# Question:

#     Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.Suppose the following input is supplied to the program:

# 34,67,55,33,12,98

#     Then, the output should be:

# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

# def converter(nums):

#     return nums, tuple(nums)

# # using map
# num = list(map(str, input().split(',')))
# lst, tup = converter(num)
# print(f'{lst}\n{tup}')

# # or
# lst = input("Enter a series of numbers separated by a comma :").split(',')
# print(lst)
# print(tuple(lst))

#--------------------------------------
# Question 5
# Question:

#     Define a class which has at least two methods:

#         getString: to get a string from console input
#         printString: to print the string in upper case.

#     Also please include simple test function to test the class methods.

# class StringLover:
#   def __init__(self, imp):
#     self.imp = imp

#   def changeString(self):
#     self.imp = input('new string: ')
#     print('string updated')

#   def getString(self):
#     self.printString(self.imp)

#   def printString(self, n):
#     print(n.upper())

#   def __str__(self):
#     return f'This is the string: {self.imp}'

# x = input('enter string: ')
# obj1 = StringLover(x)
# obj1.getString()
# print(obj1)

#--------------------------------------
# Question 6
# Question:

#     Write a program that calculates and prints the value according to the given formula:

#     Q = Square root of [(2 _ C _ D)/H]

#     Following are the fixed values of C and H:

#     C is 50. H is 30.

#     D is the variable whose values should be input to your program in a comma-separated sequence.For example Let us assume the following comma separated input sequence is given to the program:

# 100,150,180

#     The output of the program should be:

# 18,22,24

# Hints:

#     If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26).In case of input data being supplied to the question, it should be assumed to be a console input.

# def makeit(n):

#   C, H = 50, 30
#   nums = []
#   for item in n:
#     Q = [(2 * C * item) / H]
#     nums.append(str(int(Q[0] ** 0.5)))
#   return ",".join(nums)

# k = [int(item) for item in input('').split(",")]
# print(makeit(k))

# FIBONACCI CHALLENGE:
#how long does it take you to creat a generator which will print the next
#number in the fibonacci sequence every time you press ENTER?
# def fib(n):
#   a, b = 0, 1

#   for _ in range(n):
#     a, b = b, a + b
#     yield a

# nx = 20
# a = fib(nx)
# for _ in a:
#   print(_,end="")
#   input()

# dataList = [item for item in input().split(",")]
# dataDict = {item : 0 for item in input().split(",")}

# print(dataList)
# print(dataDict)

#--------------------------------------
# Question 7
# Question:

#     _Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i _ j.*

#     Note: i=0,1.., X-1; j=0,1,¡­Y-1. Suppose the following inputs are given to the program: 3,5

#     Then, the output of the program should be:

# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

# def make_array(x, y):

#   rows = int(x)
#   columns = int(y)

#   outer, inner = [], []
#   for row in range(rows):
#     for column in range(columns):
#       inner.append(row * column)
#     outer.append(inner)
#     inner = []
#   return outer

# a, b = input(":").split(",")
# result = make_array(a, b)
# for row in result:
#   print(row)

#--------------------------------------
# Question 8
# Question:

#     Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.

#     Suppose the following input is supplied to the program:

# without,hello,bag,world

#     Then, the output should be:

# bag,hello,without,world

# def reorder(args):

#   args = sorted(args)
#   return ",".join(args)

# data = tuple([item for item in input(":").split(",")])
# print(reorder(data))

#--------------------------------------
# Question 9
# Question:

#     Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.

#     Suppose the following input is supplied to the program:

# Hello world
# Practice makes perfect

#     Then, the output should be:

# HELLO WORLD
# PRACTICE MAKES PERFECT

# Hints:

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# data = []
# while True:
#   d = input()
#   if not d:
#     break
#   else:
#     data.append(d.upper())
# for item in data:
#   print(item)

#--------------------------------------
# Question 10
# Question

#     Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.

#     Suppose the following input is supplied to the program:

# hello world and practice makes perfect and hello world again

#     Then, the output should be:

# again and hello makes perfect practice world

# def remove_dups_and_reorder(n):

#   # splitted = n.split()
#   # removed_dups = set(splitted)
#   # return " ".join(sorted(removed_dups))

#   #or

#   return " ".join(sorted(set(n.split())))

# text = "hello world and practice makes perfect and hello world again"
# print(remove_dups_and_reorder(text))

#--------------------------------------
# Question 11
# Question

#     Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.

#     Example:

# 0100,0011,1010,1001

#     Then the output should be:

# 1010

#     Notes: Assume the data is input by console.

# byfive = []
# def div_by_five(n):

#   byfive = [item for item in n if not int(item, 2) % 5]
#   return ",".join([item for item in byfive])

# binary = list(map(str, (input().split(','))))
# print(div_by_five(binary))

#--------------------------------------
# Question 12
# Question:

#     Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.The numbers obtained should be printed in a comma-separated sequence on a single line.

# Hints:

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# firstList = ",".join([str(num) for num in range(1000, 3001, 2) if not int(str(num)[0]) % 2 and not int(str(num)[1]) % 2 and not int(str(num)[2]) % 2])

# print(firstList)

#--------------------------------------
# Question 13
# Question:

#     Write a program that accepts a sentence and calculate the number of letters and digits.

#     Suppose the following input is supplied to the program:

# hello world! 123

#     Then, the output should be:

# LETTERS 10
# DIGITS 3

# def counter(n):

#   alph_count, num_count = 0, 0
#   for item in n:
#     if item.isalpha():
#       alph_count += 1
#     elif item.isdigit():
#       num_count += 1

#   return alph_count, num_count

# user_input = input()
# a, n = counter(user_input)
# print(f'LETTERS {a}')
# print(f'DIGITS {n}')

#--------------------------------------
# Question 14
# Question:

#     Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

#     Suppose the following input is supplied to the program:

# Hello world!

#     Then, the output should be:

# UPPER CASE 1
# LOWER CASE 9

# def distinguish(n):
#   low, high = 0, 0
#   for item in n:
#     low += item.islower() # counts True boolean as 1
#     high += item.isupper()
#   return low, high

# text = input()
# result = distinguish(text)
# print(f'UPPER CASE {result[-1]}')
# print(f'LOWER CASE {result[0]}')

#--------------------------------------
# Question 15
# Question:

#     Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

#     Suppose the following input is supplied to the program:

# 9

#     Then, the output should be:

# 11106

# def compute(n):

#   s = []
#   for m in range(1, 5):
#     s.append(int(str(n) * m))
#   return sum(s)

# print(compute(9))

#--------------------------------------
# Question 16
# Question:

#     Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers. >Suppose the following input is supplied to the program:

# 1,2,3,4,5,6,7,8,9

#     Then, the output should be:

# 1,9,25,49,81

# def find_odd_and_square(n):

#   return ",".join([str(int(item)*int(item)) for item in n if int(item) % 2 != 0])

# user_input = [item for item in input('enter nums: ').split(",")]
# print(find_odd_and_square(user_input))

#--------------------------------------
# Question 17
# Question:

#     Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200

#     D means deposit while W means withdrawal.

#     Suppose the following input is supplied to the program:

# D 300
# D 300
# W 200
# D 100

#     Then, the output should be:

# 500

# class Net:

#   def __init__(self):
#     self.net_amount = 0

#   def __add__(self, n):
#     self.net_amount += n

#   def __sub__(self, n):
#     self.net_amount -= n

#   def print_net(self):
#     print(self.net_amount)

# net = Net()
# D = net
# net + 500
# net - 251
# D + 300
# net.print_net()

# net_worth = 0
# while True:
#   def calculate(depOrWith, num, net):
#     if depOrWith.lower() == "d":
#       net += num
#     elif depOrWith.lower() == "w":
#       net -= num
#     return net

#   try:
#     action, amount = input().split(" ")
#   except (TypeError, ValueError):
#     print('invalid input')
#     continue
#   if action != "d" and action != "w":
#     print('invalid input')
#     continue
#   net_worth = calculate(action, int(amount), net_worth)
#   print(net_worth)

#--------------------------------------
# Question 18
# Question:

#     A website requires the users to input username and password to register. Write a program to check the validity of password input by users.

#     Following are the criteria for checking the password:

#     At least 1 letter between [a-z]
#     At least 1 number between [0-9]
#     At least 1 letter between [A-Z]
#     At least 1 character from [$#@]
#     Minimum length of transaction password: 6
#     Maximum length of transaction password: 12

#     Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

#     Example

#     If the following passwords are given as input to the program:

# ABd1234@1,a F1#,2w3E*,2We3345

#     Then, the output of the program should be:

# ABd1234@1

# alph = "abcdefghijklmnopqrstuvwxyz"
# nums = "0123456789"
# syms = "$#@"
# alphUp = alph.upper()

# candidates = [item for item in input().split(",")]
# passed = []
# for pw in candidates:
#   a, b, c, d = False, False, False, False
#   if 6 <= len(pw) <= 12:
#     for chr in pw:
#       if chr in alph:
#         a = True
#     for chr in pw:
#       if chr in nums:
#         b = True
#     for chr in pw:
#       if chr in syms:
#         c = True
#     for chr in pw:
#       if chr in alphUp:
#         d = True
#     if a == True and b == True and c == True and d == True:
#       passed.append(pw)

# print(",".join(passed))

#--------------------------------------
# Question 19
# Question:

#     You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:

#     1: Sort based on name
#     2: Then sort based on age
#     3: Then sort by score

#     The priority is that name > age > score.

#     If the following tuples are given as input to the program:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85

#     Then, the output of the program should be:

# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

# allData = []
# while True:
#   data = tuple(input().split(","))
#   if not data[0]:
#     break
#   elif len(data) > 3:
#     print('invalid')
#     continue
#   try:
#     newdata = (data[0], int(data[1]), int(data[2]))
#   except (ValueError, IndexError):
#     print('invalid')
#     continue
#   allData.append(newdata)
#   newdata = ()

# final = sorted(allData)
# print(final)

#--------------------------------------
# Question 20
# Question:

#     Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

#     Suppose the following input is supplied to the program:

# 7

#     Then, the output should be:

# 0
# 7
# 14

# class Nexter:
#   def __init__(self, ceiling=200):
#     self.ceiling = ceiling
#     self.result = 0

#   def __iter__(self):
#     self.counter = 0
#     return self

#   def __next__(self):
#     self.result = self.counter * 7
#     if self.result <= self.ceiling:
#       self.counter += 1
#       return self.result
#     else:
#       raise StopIteration

# obj1 = Nexter()
# iter1 = iter(obj1)
# for item in iter1:
#   print(item)

#--------------------------------------
# Question 21
# Question:

#     A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

#     The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer. Example: If the following tuples are given as input to the program:

# UP 5
# DOWN 3
# LEFT 3
# RIGHT 2

#     Then, the output of the program should be:

# 2

# input
# directions = ["UP","DOWN","LEFT","RIGHT"]
# route = []
# while True:
#   movement_data = input().split(" ")
#   if not movement_data[0]:
#     break
#   elif len(movement_data) < 2 or len(movement_data) > 2:
#     print('invalid')
#     continue
#   elif movement_data[0] not in directions:
#     print('invalid')
#     continue
#   else:
#     try:
#       movement_data[-1] = int(movement_data[-1])
#     except ValueError:
#       print('invalid')
#       continue
#     route.append(tuple(movement_data))

# # aggregate route
# origin = [0, 0]
# current = [0, 0]
# for movement in route:
#   if movement[0] == "UP":
#     current[0] += movement[-1]
#   elif movement[0] == "DOWN":
#     current[0] -= movement[-1]
#   elif movement[0] == "LEFT":
#     current[-1] += movement[-1]
#   elif movement[0] == "RIGHT":
#     current[-1] -= movement[-1]

# # plot distance - (((x1 - x2) ** 2) + ((y1 - y2) ** 2)) ** .5
# distance = (((current[0] - origin[0]) ** 2) + ((current[-1] - origin[-1]) ** 2)) ** .5
# print(round(distance))

#--------------------------------------
#   Question 22
# Question:

#     Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

#     Suppose the following input is supplied to the program:

# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.

#     Then, the output should be:

# 2:2
# 3.:1
# 3?:1
# New:1
# Python:5
# Read:1
# and:1
# between:1
# choosing:1
# or:2
# to:1

# from collections import Counter

# result = Counter(input().split())
# output_list = [str(k + ":" + str(v)) for k, v in result.items()]
# for item in sorted(output_list):
#   print(item)

#--------------------------------------
# Question 23
# Question:

#     Write a method which can calculate square value of number

# class Sqaured:
#   def __init__(self, num):
#     self.num = num

#   def __pow__(self, num):
#     self.squared = self.num ** 2

#   def __str__(self):
#     return f"square of {self.num} is {self.squared}"

# num = int(input("enter num"))
# obj1 = Sqaured(num)
# obj1 ** obj1
# print(obj1)

#--------------------------------------
# Question 24
# Question:

#     Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. But Python has a built-in document function for every built-in functions.

#     Please write a program to print some Python built-in functions documents, such as abs(), int(), raw_input()

#     And add document for your own function

# from os import system

# def print_docs():
#   """
#   this function will print out the explanation of abs(), int(), and input()
#   """
#   print(abs.__doc__)
#   print(int.__doc__)
#   print("----------")
#   print(input.__doc__)

# print_docs()
# print(print_docs.__doc__)

#--------------------------------------
# Question 25
# Question:

#     Define a class, which have a class parameter and have a same instance parameter.

# class Classroom:

#   def __init__(self, num):
#     self.instance_parameter = num
#     Classroom.class_parameter = self.instance_parameter

#   def show_params(self):
#     print(f'object parameter: {self.instance_parameter}')
#     print(f'class parameter: {Classroom.class_parameter}')

#   def __add__(self, num):
#     self.instance_parameter += num

# x = int(input("enter value: "))
# obj1 = Classroom(x)
# obj1.show_params()
# obj1 + 25
# obj1.show_params()

#--------------------------------------
# Question 26
# Question:

#     Define a function which can compute the sum of two numbers.

# def summit(nums):

#   total = sum([num for num in nums])
#   return total

# user_input = [int(num) for num in input("enter 2 numbers to sum (num,num): ").split(",")]
# print(summit(user_input))

#OR - lambda
# summ = lambda a,b: a + b
# print(summ(3,5))

#---------------------------------------
# Question 27
# Question:

#     Define a function that can convert a integer into a string and print it in console.

# def converter(n):

#   try:
#     n + 1
#   except TypeError:
#     return "not an integer"

#   return str(n), type(str(n))

# print(converter(55))

#---------------------------------------
# Question 28
# Question:

#     Define a function that can receive two integer numbers in string form and compute their sum and then print it in console.

# def string_2_int(a, b):

#   # a, b = int(a), int(b)

#   return int(a) + int(b)

# num1, num2 = input("enter 2 numbers (ex: 1 2): ").split(" ")
# print(string_2_int(num1, num2))

#---------------------------------------
# Question 29
# Question:

#     Define a function that can accept two strings as input and concatenate them and then print it in console.

# conc = lambda a, b : a + b
# while True:
#   try:
#     first, second = input("enter 2 strings: ").split(" ")
#   except ValueError:
#     continue
#   break

# print(conc(first, second))

#---------------------------------------
# Question 30
# Question:

#     Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print all strings line by line.

# def bigger_string(a, b):
#   length1, length2 = len(a), len(b)

#   if length1 > length2:
#     return a
#   elif length1 < length2:
#     return b
#   else:
#     return a + "\n" + b

# while True:
#   try:
#     first, second = input("enter 2 strings: ").split(" ")
#   except ValueError:
#     continue
#   break
# print(bigger_string(first, second))

#---------------------------------------
# Question 31
# Question:

#     Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys.

# def make_dict(n):

#   return {item : item ** 2 for item in range(1, n + 1)}

# max_num = int(input("enter max: "))
# print(make_dict(max_num))

#---------------------------------------
# Question 32
# Question:

#     Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

# def keys_only():

#   dic = {}
#   for num in range(1,21):
#     dic[num] = num ** 2

#   print(dic.keys())

# keys_only()

#---------------------------------------
# Question 33
# Question:

#     Define a function which can generate and print a list where the values are square of numbers between 1 and 20 (both included).

# def sqaureit():

#   print([item ** 2 for item in range(1, 21)])

# sqaureit()

#---------------------------------------
# Question 34
# Question:

#     Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the first 5 elements in the list.

# def first_five():

#   print([item ** 2 for item in range(1, 21)[:5]])
#   # or
#   print([item ** 2 for idx, item in enumerate(range(1, 21)) if idx < 5])

# first_five()

#---------------------------------------
# Question 35
# Question:

#     Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print the last 5 elements in the list.

# def last_five():

#   print([item ** 2 for item in range(1, 21)[-5:]])

# last_five()

#---------------------------------------
# Question 36
# Question:

#     Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). Then the function needs to print all values except the first 5 elements in the list.

# def except_first_five():

#   print([item ** 2 for item in range(1, 21)[5:]])

# except_first_five()

#---------------------------------------
# Question 37
# Question:

#     Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).

# def tuple_squares():

#   print(tuple(item ** 2 for item in range(1, 21)))

# tuple_squares()

#---------------------------------------
# Question 38
# Question:

#     With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and the last half values in one line.

# def send_five():
#   data = tuple(range(1, 11))
#   half_length = len(data) // 2
#   isOdd = len(data) % 2
#   if isOdd:
#     half_length += 1

#   for item in range(0, len(data), half_length):
#     yield data[item : item + half_length]

# rounds = send_five()
# for item in rounds: # break apart the generator
#   print(item)

#or Solution by: CoffeeBrakeInc (added \n new line)
# tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11)
# lt = int(len(tup)/2)
# print(str(tup[:lt]) + "\n" + str(tup[lt:]))

#---------------------------------------
# Question 39
# Question:
# Write a program to generate and print another tuple whose values are even numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).

# def only_even():

#   tup = tuple(range(1, 11))
#   return tuple(item for item in tup if item % 2 == 0)

# print(only_even())

#---------------------------------------
# Question 40
# Question:

#     Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

# def is_yes(n):
#   if n == "yes" or n == "YES" or n == "Yes":
#     return "Yes"
#   else:
#     return "No"

# while True:
#   data = input("enter string: ")
#   if not data:
#     break
#   print(is_yes(data))

#---------------------------------------
# Question 41
# Question:

#     Write a program which can map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].

# def square_it(n):

#   return n ** 2

# print(list(map(square_it, list(range(1, 11)))))

# #lambda
# print(list(map(lambda item: item ** 2, list(range(1, 11)))))

#---------------------------------------
# Question 42
# Question:

#     Write a program which can map() and filter() to make a list whose elements are square of even number in [1,2,3,4,5,6,7,8,9,10].

# def is_even(n):
#   return not n % 2

# print([item for item in map(lambda x: x, filter(is_even, list(range(1, 11))))])

#---------------------------------------
# Question 43
# Question:

#     Write a program which can filter() to make a list whose elements are even number between 1 and 20 (both included).

# print([item for item in filter(lambda x : x % 2 == 0, range(1, 21))])

#---------------------------------------
# Question 44
# Question:

#     Write a program which can map() to make a list whose elements are square of numbers between 1 and 20 (both included).

# print(list((map(lambda x : x ** 2, range(1, 21)))))

#---------------------------------------
# Question 45
# Question:

#     Define a class named American which has a static method called printNationality.

# class American:
#   def __init__(self, nationality="American"):
#     self.nationality = nationality

#   @staticmethod
#   def printNationality():
#     print("American")

# obj1 = American()
# obj1.printNationality()

#---------------------------------------
# Question 46
# Question:

#     Define a class named American and its subclass NewYorker.

# class American:
#   def __init__(self, nationality="American"):
#     self.nationality = nationality
#     self.cats = 2

# class NewYorker(American):

#   def identity(self):
#     print(f'I am {self.nationality}, and I have {self.cats} cats!')

# obj1 = NewYorker('Russian')

# obj1.identity()

#---------------------------------------
# Question 47
# Question

#     Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.

# class Circle:
#   def __init__(self, radius):
#     self.radius = radius

#   def find_area(self):
#     area = round((self.radius ** 2) * (22 / 7), 2)
#     print(area)

# circle1 = Circle(15)
# circle1.find_area()

#---------------------------------------
# Question 48
# Question

#     Define a class named Rectangle which can be constructed by a length and width. The Rectangle class has a method which can compute the area.

# class Rectangle:
#   def __init__(self, length, width):
#     self.length = length
#     self.width = width

#   def find_area(self):
#     print(f'The area of a rectangle with legnth {self.length} and height {self.width} is {self.calculate_area()}.')

#   def calculate_area(self):
#     return self.length * self.width

# rect1 = Rectangle(3, 5)
# rect1.find_area()

#---------------------------------------
# Question 49
# Question

#     Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

# class Shape:

#   default = 0

#   def __init__(self):
#     pass

#   def find_area():
#     print(Shape.default * Shape.default)

# class Square(Shape):
#   def __init__(self, length):
#     self.length = length

#   def find_area(self):
#     print(self.length * self.length)

# square1 = Square(5)
# square1.find_area()
# Shape.find_area()

#---------------------------------------
# Question 50
# Question

#     Please raise a RuntimeError exception.

# user_input = input("enter integer: ")
# if not type(user_input) is int:
#   raise ValueError("only integers are allowed!")

#---------------------------------------
# Question 51
# Question

#     Write a function to compute 5/0 and use try/except to catch the exceptions.

# def divider(x, y):

#   try:
#     return x / y
#   except (ZeroDivisionError):
#     return "cannot divide by zero"
#   except TypeError:
#     return "must provide integers"

# print(divider(5, 5))

#---------------------------------------
# Question 52
# Question

#     Define a custom exception class which takes a string message as attribute.

# class CustomExceptionClass(Exception):
#   def __init__(self, *args):
#     if args:
#       self.message = args[0]
#     else:
#       self.message = None

#   def __str__(self):
#     if self.message:
#       return f'CUSTOM ERROR: {self.message}'
#     else:
#       return f'CUSTOM ERROR HAS BEEN RAISED'

# try:
#   a = input("type \"a\": ")
#   if a != "a":
#     raise CustomExceptionClass("hey you didn't type \"a\"!")
# except CustomExceptionClass as er:
#   print(er.message)

#---------------------------------------
# Question 53
# Question

#     Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the user name of a given email address. Both user names and company names are composed of letters only.

#     Example: If the following email address is given as input to the program:

# john@google.com

#     Then, the output of the program should be:

# john

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# import re

# pattern = re.compile(r'(^[\w]+)')
# email = "john@google.com"

# result = pattern.match(email)

# print(result.group(0))

#---------------------------------------
# Question 54
# Question

#     Assuming that we have some email addresses in the "username@companyname.com" format, please write program to print the company name of a given email address. Both user names and company names are composed of letters only.

#     Example: If the following email address is given as input to the program:

# john@google.com

#     Then, the output of the program should be:

# google

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# import re

# def company_name(email):

#   pattern = re.compile(r'.+@(.+)\.')

#   result = pattern.match(email)

#   return result.group(1)

# data = input('enter email: ')
# print(company_name(data))

#---------------------------------------
# Question 55
# Question

#     Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

#     Example: If the following words is given as input to the program:

# 2 cats and 3 dogs.

#     Then, the output of the program should be:

# ['2', '3']

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# def only_digits(n):

#   s = n.split()
#   f = [item for item in s if item.isdigit()]
#   return f

# data = input("enter string: ")
# print(only_digits(data))

#---------------------------------------
# Question 56
# Question

#     Print a unicode string "hello world".

# Hints

#     Use u'strings' format to define unicode string.

# print("all strings are unicode in Python3!")

#---------------------------------------
# Question 57
# Question

#     Write a program to read an ASCII string and to convert it to a unicode string encoded by utf-8.

# s = input()
# u = s.encode('utf-8')
# print(u)

#---------------------------------------
# Question 58
# Question

#     Write a special comment to indicate a Python source code file is in unicode.

# -*- co_ding: utf-8 -*-

#---------------------------------------
# Question 59
# Question

#     Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

#     Example: If the following n is given as input to the program:

# 5

#     Then, the output of the program should be:

# 3.55

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# i = int(input("enter num: "))

# print(round(sum([item / (item + 1) for item in range(1, i + 1)]), 2))

#or as sum/map/lambda

# while True:
#   try:
#     user_input = int(input("num: "))
#   except ValueError:
#     continue
#   break

# print(round(sum(map(lambda num : num / (num + 1), range(1, user_input + 1))),2))

#---------------------------------------
# Question 60
# Question

#     Write a program to compute:

# f(n)=f(n-1)+100 when n>0
# and f(0)=0

#     with a given n input by console (n>0).

#     Example: If the following n is given as input to the program:

# 5

#     Then, the output of the program should be:

# 500

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# def f(n):
#   if n == 0:
#     return n

#   return 100 + f(n - 1)
# print(f(5))

#---------------------------------------
# Question 61
# Question

#     The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

#     Please write a program to compute the value of f(n) with a given n input by console.

#     Example: If the following n is given as input to the program:

# 7

#     Then, the output of the program should be:

# 13

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# while True:
#   try:
#     user_input = int(input("num: "))
#   except ValueError:
#     continue
#   break

# def fib(rounds):
#   a, b = 0, 1
#   count = 0
#   while count < rounds:
#     a, b = b, a + b
#     count += 1

#   return a

# print(f'while: {fib(user_input)}')

# # or recursive
# def fib_rec(rounds):

#   if rounds > 1:
#     return fib_rec(rounds - 1) + fib_rec(rounds -  2)
#   else:
#     return rounds

# print(f'recursive: {fib_rec(user_input)}')

#---------------------------------------
# Question 62
# Question

#     The Fibonacci Sequence is computed based on the following formula:

# f(n)=0 if n=0
# f(n)=1 if n=1
# f(n)=f(n-1)+f(n-2) if n>1

#     Please write a program to compute the value of f(n) with a given n input by console.

#     Example: If the following n is given as input to the program:

# 7

#     Then, the output of the program should be:

# 0,1,1,2,3,5,8,13

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# def fib(ceiling):

#     if ceiling < 2:
#         return ceiling
#     elif ceiling >= 2:
#         return fib(ceiling - 1) + fib(ceiling - 2)

# seq = []
# user_num = int(input('enter iterations: '))
# for iterations in range(0, user_num + 1):
#     seq.append(fib(iterations))
# print("\n" + ",".join([str(num) for num in seq]))

#---------------------------------------
# Question 63
# Question

#     Please write a program using generator to print the even numbers between 0 and n in comma separated form while n is input by console.

#     Example: If the following n is given as input to the program:

# 10

#     Then, the output of the program should be:

# 0,2,4,6,8,10

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# def only_twos(ceiling):

#   for number in range(0, ceiling + 1):
#     if not number % 2:
#       yield number

# user_num = int(input('enter num: '))
# x = only_twos(user_num)
# print(",".join([str(num) for num in x]))

#---------------------------------------
# Question 64
# Question

#     Please write a program using generator to print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.

#     Example: If the following n is given as input to the program:

# 100

#     Then, the output of the program should be:

# 0,35,70

#     In case of input data being supplied to the question, it should be assumed to be a console input.

# def div_by_five_or_seven(ceiling):

# sevens = {num for num in range(0, ceiling + 1, 7)}
# fives = {num for num in range(0, ceiling + 1, 5)}

# for num in fives:
#   if num in sevens:
#     yield num

#   for num in range(0, ceiling + 1, 35):
#     yield num

# user_input = int(input('enter num: '))
# print(",".join([str(num) for num in div_by_five_or_seven(user_input)]))

#---------------------------------------
# Question 65
# Question

#     Please write assert statements to verify that every number in the list [2,4,6,8] is even.

# some_list = [2,4,6,7]

# for item in some_list:
#   assert item % 2 == 0, f"{item} is not even"
# else:
#   print("all even")

#---------------------------------------
# Question 66
# Question

#     Please write a program which accepts basic mathematic expression from console and print the evaluation result.

#     Example: If the following n is given as input to the program:

# 35 + 3

#     Then, the output of the program should be:

# 38

# user_input = eval(input("enter expression: "))
# print(user_input)

#or

# square_root = eval(input("enter square root expression: "))
# z = 47
# for item in range(2, int(square_root) + 1):
#   if z % item == 0:
#     print("not prime")

# print("prime")

#---------------------------------------
# Question 67
# Question

#     Please write a binary search function which searches an item in a sorted list. The function should return the index of element to be searched in the list.

# Hints

#     Use if/elif to deal with conditions.

# import random

# def bubble():

#     numbers = random.sample(range(1, 100), 50)
#     limit = len(numbers)
#     while True:
#         for idx in range(0, limit):
#             if idx == limit - 1:
#                 return numbers
#             if numbers[idx:idx + 1] > numbers[idx + 1:idx + 2]:
#                 numbers[idx:idx + 1], numbers[idx + 1:idx +
#                                               2] = numbers[idx + 1:idx + 2], numbers[idx:idx + 1]
#                 break

# def binary(srted, base, ceil, num):

#     mid = (base + ceil) // 2
#     print(f'base: {base}, midL {mid}, ceil: {ceil}')
#     if num == srted[mid]:
#         return 'found at index: {}'.format(mid)
#     elif num > srted[mid] and (len(srted) - 1) - mid == 1 and num == srted[ceil]:
#         mid = ceil
#         return 'found at index: {}'.format(mid)
#     elif base == mid:
#         return 'not found'
#     elif num < srted[mid]:
#         ceil = mid
#         return binary(srted, base, ceil, num)
#     elif num > srted[mid]:
#         base = mid
#         return binary(srted, base, ceil, num)

# sorted_list = bubble()
# column = len(sorted_list) // 2
# print(f'sorted list:\b')
# for idx, item in enumerate(sorted_list):
#     if idx == column:
#         print("\b")
#     else:
#         print(item, end=",")
# print("\n")
# #
# number = eval(input("enter search item: "))
# print(binary(sorted_list, 0, len(sorted_list) - 1, number))

#---------------------------------------
# Question 68
# Question

#     Please generate a random float where the value is between 10 and 100 using Python module.

# import random

# print(random.uniform(10,100))

#---------------------------------------
# Question 69
# Question

#     Please generate a random float where the value is between 5 and 95 using Python module.

# import random
# print(round(random.uniform(5,95),2))

#---------------------------------------
# Question 70
# Question

#     Please write a program to output a random even number between 0 and 10 inclusive using random module and list comprehension.

# import random

# print([random.randrange(0,11,2) for _ in range(1)][0])

#---------------------------------------
# Question 71
# Question

#     Please write a program to output a random number, which is divisible by 5 and 7, between 10 and 150 inclusive using random module and list comprehension.

# import random

# while True:
#   rand_num = int(random.uniform(10,150))
#   if not rand_num % 7 and not rand_num % 5:
#     print(rand_num)
#     break
#   else:
#     continue

# print([random.choice([35,70,105,140]) for _ in range(1)][0])

# or

# print(random.choice([num for num in range(10, 151) if not num % 35]))

#---------------------------------------
# Question 72
# Question

#     Please write a program to generate a list with 5 random numbers between 100 and 200 inclusive.

# import random

# print(random.sample(range(100,201),5))

#---------------------------------------
# Question 73
# Question

# import random
#     Please write a program to randomly generate a list with 5 even numbers between 100 and 200 inclusive.

# print(random.sample([num for num in range(100,201,2)],5))

#---------------------------------------
# Question 74
# Question

#     Please write a program to randomly generate a list with 5 numbers, which are divisible by 5 and 7 , between 1 and 1000 inclusive.

# import random
# print(random.sample([num for num in range(1,1000 + 1) if not num % 35],5))

#---------------------------------------
# Question 75
# Question

#     Please write a program to randomly print a integer number between 7 and 15 inclusive.

# import random

# print(int(random.uniform(7,15)))
# or
# print(random.choice(range(7,16)))

#---------------------------------------
# Question 76
# Question

#     Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".

# import zlib

# s = b"bennyBoy_JP"

# s_compressed = zlib.compress(s)
# print(f'compressed: {s_compressed}')

# s_decompressed = zlib.decompress(s_compressed)
# print(f'decompressed: {s_decompressed}')

#---------------------------------------
# Question 77
# Question

#     Please write a program to print the running time of execution of "1+1" for 100 times.

# from time import time

# def main_prog(func):
#   def wrapper(*args, **kwargs):
#     time1 = time()
#     result = func(*args, **kwargs)
#     time2 = time()
#     print(f'time: {round(time2 - time1,2)}')
#     return result
#   return wrapper

# @main_prog
# def one_plus_one():
#   for _ in range(100):
#     1 + 1

# one_plus_one()

#---------------------------------------
# Question 78
# Question

#     Please write a program to shuffle and print the list [3,6,7,8].

# import random
# x = [3,6,7,8]
# random.shuffle(x)
# print(x)

#---------------------------------------
# Question 79
# Question

#     Please write a program to generate all sentences where subject is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

# import itertools
# master = master = [["My", "Your", "Our", "Their", "Its"],["favorite", "least liked"],["color is"],["Red", "Green", "Blue"]]

# for item in list(itertools.product(*master, repeat=1)):
#   print(" ".join(item) + ".")

#---------------------------------------
# Question 80
# Question

#     Please write a program to print the list after removing even numbers in [5,6,77,45,22,12,24].

# def is_not_even(num):
#   if num % 2 != 0:
#     return num

# a_list = [5,6,77,45,22,12,24]
# print(list(filter(lambda x: x % 2 != 0, a_list)))

#---------------------------------------
# Question 81
# Question

#     By using list comprehension, please write a program to print the list after removing numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].

# l = [12,23,35,70,88]
# print(list(filter(lambda item : item % 7 != 0 and item % 5 != 0, l)))

#---------------------------------------
# Question 82
# Question

#     By using list comprehension, please write a program to print the list after removing the 0th, 2nd, 4th,6th numbers in [12,24,35,70,88,120,155].

# l = [12,24,35,70,88,120,155]
# print([l[num] for num in range(len(l)-1) if num % 2 != 0])

# or

# print([l[num] for num in range(1, len(l), 2)])

#---------------------------------------
# Question 83
# Question

#     By using list comprehension, please write a program to print the list after removing the 2nd - 4th numbers in [12,24,35,70,88,120,155].

# l = [12,24,35,70,88,120,155]

# print([l[num] for num in range(len(l)) if num < 2 or num > 4])

#---------------------------------------
# Question 84
# Question

#     By using list comprehension, please write a program generate a 3*5*8 3D array whose each element is 0.

# def create3D(a, b, c):
#   x, y, z = [], [], []
#   for _ in range(a):
#     for _ in range(b):
#       for _ in range(c):
#         z.append(0)
#       y.append(z)
#       z = []
#     x.append(y)
#     y = []

#   return x

# print(create3D(3, 5, 8))

#---------------------------------------
# Question 85
# Question

#     By using list comprehension, please write a program to print the list after removing the 0th,4th,5th numbers in [12,24,35,70,88,120,155].
# l = [12,24,35,70,88,120,155]
# print([l[num] for num in range(len(l)) if num not in [0,4,5]])

#---------------------------------------
# Question 86
# Question

#     By using list comprehension, please write a program to print the list after removing the value 24 in [12,24,35,24,88,120,155].

# l = [12,24,35,24,88,120,155]
# print([num for num in l if num != 24])

#---------------------------------------
# Question 87
# Question

#     With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155], write a program to make a list whose elements are intersection of the above given lists.

# l1 = [1,3,6,78,35,55,24]
# l2 = [12,24,35,24,88,120,155]
# print(list(filter(lambda x : x in l1, set(l2))))

# or

# print([l1[idx] for idx in range(len(l1)) if l1[idx] in l2])

#---------------------------------------
# Question 88
# Question

#     With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after removing all duplicate values with original order reserved.
# l = [12,24,35,24,88,120,155,88,120,155]

# hold = []
# for item in l:
#   if item not in hold:
#     hold.append(item)
# print(hold)

#---------------------------------------
# Question 89
# Question

#     Define a class Person and its two child classes: Male and Female. All classes have a method "getGender" which can print "Male" for Male class and "Female" for Female class.

# class Person:

#   universal = "teeth"
#   account = 0

#   def getGender(self):
#     print(self.gender, self.human)

#   def showMoney(self):
#     print(f'{self.name} has {self.account}!')

#   def addMoney(self, num):
#     self.account += num
#     print(f'{self.name} now has {self.account}!')

# class Male(Person):

#   def __init__(self, name="Lenny"):
#     self.name = name
#     self.gender = "MALE"
#     self.human = Person.universal
#     self.account = Person.account

# class Female(Person):

#   def __init__(self, name = "Sarah"):
#     self.name = name
#     self.gender = "FEMALE"
#     self.human = Person.universal
#     self.account = Person.account

# a, b = Male(), Female()
# a.getGender(), b.getGender()
# a.showMoney(), b.showMoney()
# a.addMoney(99999), b.addMoney(5555)

#---------------------------------------
# Question 90
# Question

#     Please write a program which count and print the numbers of each character in a string input by console.

#     Example: If the following string is given as input to the program:

# abcdefgabc

#     Then, the output of the program should be:

# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

# s = "abcdefgabc"
# for item in {(item,s.count(item)) for item in s}:
#   print(item[0],item[-1])

#---------------------------------------
# Question 91
# Question

#     Please write a program which accepts a string from console and print it in reverse order.

#     Example: If the following string is given as input to the program:*

# rise to vote sir

#     Then, the output of the program should be:

# ris etov ot esir

# print("".join([a for a in reversed(list(map(lambda item : item, input("string: "))))]))

#or

# print(input("string: ")[::-1])

#---------------------------------------
# Question 92
# Question

#     Please write a program which accepts a string from console and print the characters that have even indexes.

#     Example: If the following string is given as input to the program:

# H1e2l3l4o5w6o7r8l9d

#     Then, the output of the program should be:

# Helloworld

# s = "H1e2l3l4o5w6o7r8l9d"

# print("".join([s[item] for item in range(len(s)) if item % 2 == 0]))

#---------------------------------------
# Question 93
# Question

#     Please write a program which prints all permutations of [1,2,3]

# from itertools import permutations

# p = permutations(range(1,4))
# for item in p:
#   print(item)

#---------------------------------------
# Question 94
# Question

#     Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?

# heads = 35
# legs = 94

# possible_rabbits = legs / 2 - heads
# possible_chickens = heads - possible_rabbits

# if possible_rabbits % 1 != 0 or possible_chickens % 1 != 0:
#   print('unnatural')

# else:
#   print(f'rabbits: {int(possible_rabbits)}, chickens: {int(possible_chickens)}')

#---------------------------------------
# Question 95
# Question

# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given scores. Store them in a list and find the score of the runner-up.

# If the following string is given as input to the program:

# 5
# 2 3 6 6 5

# Then, the output of the program should be:

# 5

# scores = [2, 3, 6, 6, 5]
# runner_up = sorted(set(scores), reverse=True)[1]
# print(runner_up)

#---------------------------------------
# Question 96
# Question

#     You are given a string S and width W. Your task is to wrap the string into a paragraph of width.

#     If the following string is given as input to the program:

#     ABCDEFGHIJKLIMNOQRSTUVWXYZ
#     4

#     Then, the output of the program should be:

#     ABCD
#     EFGH
#     IJKL
#     IMNO
#     QRST
#     UVWX
#     YZ

# S = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
# W = 2

# break_at_W = 0

# for element in S:
#   break_at_W += 1
#   if break_at_W == W:
#     break_at_W = 0
#     print(element)
#   else:
#     print(element,end="")
# print()

#---------------------------------------
# Question 97
# Question

#     You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

#     Different sizes of alphabet rangoli are shown below:

#     #size 3

#     ----c----
#     --c-b-c--
#     c-b-a-b-c
#     --c-b-c--
#     ----c----

#     #size 5

#     --------e--------
#     ------e-d-e------
#     ----e-d-c-d-e----
#     --e-d-c-b-c-d-e--
#     e-d-c-b-a-b-c-d-e
#     --e-d-c-b-c-d-e--
#     ----e-d-c-d-e----
#     ------e-d-e------
#     --------e--------

# import string
# import random
# import time
# from os import system


# while True:

#   alph = string.ascii_lowercase[-1::-1]
#   size = random.choice([3,5,7,9,11,13,15])
#   board_size = (size * 2) - 1
#   dashes = board_size + (board_size - 1)
#   dash = "-"
#   chr_count = -1
#   center = dashes // 2

#   for row in range(0, board_size):
#       if row <= (board_size // 2):
#           chrs = alph[26 - size:26 - size + 1 + row]

#           if len(chrs) > 1:
#               chrs_mirror = chrs + chrs[len(chrs) - 2::-1]
#               chrs_mirror = dash.join([item for item in chrs_mirror])
#               print(chrs_mirror.center(dashes,dash))
#           else:
#               print(chrs.center(dashes,dash))
#       else:
#           chrs = alph[26 - size:chr_count]
#           chr_count -= 1
          
#           if len(chrs) > 1:
#               chrs_mirror = chrs + chrs[len(chrs) - 2::-1]
#               chrs_mirror = dash.join([item for item in chrs_mirror])
#               print(chrs_mirror.center(dashes,dash))
#           else:
#               print(chrs.center(dashes,dash))

#   time.sleep(1)
#   _ = system("clear")  


#---------------------------------------
# Question 98
# Question

#     You are given a date. Your task is to find what the day is on that date.

# Input

#     A single line of input containing the space separated month, day and year, respectively, in MM DD YYYY format.

#     08 05 2015

# Output

#     Output the correct day in capital letters.

#     WEDNESDAY

# from calendar import weekday
# """
# weekday(year, month, day)
#     Return weekday (0-6 ~ Mon-Sun) for year, month (1-12), day (1-31).
# """

# m, d, y = input("enter date MM DD YYYY: ").split(" ")
# m, d, y = int(m), int(d), int(y)

# a = weekday(y, m, d)
# days = ["MONDAY", "TUESDAY", "WEDNESDAY", 
#         "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"
#         ]
# print(days[a])

#---------------------------------------
# Question 99
# Question

#     Given 2 sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

# Input

#     The first line of input contains an integer, M.The second line contains M space-separated integers.The third line contains an integer, N.The fourth line contains N space-separated integers.

#     4
#     2 4 5 9
#     4
#     2 4 11 12

# Output

#     Output the symmetric difference integers in ascending order, one per line.

#     5
#     9
#     11
#     12

# import random

# M = set(random.sample(range(8),5))
# N = set(random.sample(range(8),5))
# print(f'set M: {M}')
# print(f'set N: {N}')
# result = M ^ N # <-- symmetric difference operator
# for item in result:
#   print(item)



#---------------------------------------
# Question 100
# Question

#     You are given words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. See the sample input/output for clarification.

#     If the following string is given as input to the program:

#     4
#     bcdef
#     abcdefg
#     bcde
#     bcdef

#     Then, the output of the program should be:

#     3
#     2 1 1

# word_list = []
# dup_words = {}
# number_of_words = int(input())

# while len(word_list) < number_of_words:
#   word = input()
#   word_list.append(word)

# for word in word_list:
#   dup_words[word] = word_list.count(word)

# print(len(dup_words))
# for count in dup_words.values():
#   print(count,end=" ")
# print()


#---------------------------------------
# Question 101
# Question

#     You are given a string.Your task is to count the frequency of letters of the string and print the letters in descending order of frequency.

#     If the following string is given as input to the program:

#     aabbbccde

#     Then, the output of the program should be:

#     b 3
#     a 2
#     c 2
#     d 1
#     e 1


# def count_freq(s):
  
#   hold = {}
#   for item in s:
#     hold.setdefault(item, s.count(item))
 
#   srt = sorted(hold.items(), key=lambda x : x[1], reverse=True)

#   for item in srt:
#     print(item[0],item[1])


# data = "aabbbccde"
# count_freq(data)


#---------------------------------------
# Question 102
# Question

#     Write a Python program that accepts a string and calculate the number of digits and letters.

# Input

#     Hello321Bye360

# Output

#     Digit - 6
#     Letter - 8

# def counttypes(s):
  
#   l, d = 0, 0
#   nums = "0123456789"
#   alph = "abcdefghijklmnopqrstuvwxyz"
#   for item in range(len(s)):
#     if s[item].lower() in alph:
#       l += 1
#     elif s[item] in nums:
#       d += 1
  
#   print(f'Digit - {d}')
#   print(f'Letter - {l}')

# data = "Hello321Bye360"
# counttypes(data)

#---------------------------------------
# Question 103
# Question

#     Given a number N.Find Sum of 1 to N Using Recursion

# Input

#     5

# Output

#     15

# def getsum(num):

#   if num == 0:
#     return num

#   return getsum(num - 1) + num
  
# print(getsum(eval(input())))

# :)

