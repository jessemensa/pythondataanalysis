# import module 
from notes3 import compute 
compute([5, 7, 11])



# Python files typically import classes, modules and functions from other libraries 
import math 
math.exp(2) 
# or 
from math import exp 
exp(2) 

# The if__name__ == "__main__" statement 
# used so can execute script by itself and also used to imoport objects from script as if it was a regular module. 

# get the sum of numbers from 1 - 10 
result = 0 
for n in range(1,11):
    result += n 

print(result) 
# import this in console will print result again,when importing result, u just want the variable. 
# You dont expect it to print to the console 


# another way to fix this 
results = 0 
for n in range(1, 11):
    results += n 
if __name__ == '__main__': # python sets this special name variable to the main such that result is printed at the end of script
    # but when importing result, print statement is never reached. 
    print(results)

# Python Algorithms => series of instructions executed to perform a specific task or computation 
# for instance create an algorithm to find the maximum number and minimum number 
numbers = [4, 2, 3, 7]
# create a variable that will hold the maximum & minimum number 
maximum = 0 
minumum = 0 

for number in numbers: 
    if number > maximum: 
        maximum = number 
print(maximum) 

for number in numbers: 
    # number be less than minimum 
    if number < minumum: 
        minumum = number 
print(number) 


# Time complexity 
# Problem is 10x large, algo take 10x or 100x or 1000x to execute ?? 
# relation between size of the problem and steps taken is called time complexity. 

# Number of operations required to execute an algorithm. 
# Big-0 notation, counting the number of operations required to execute an algorithm. 
# ie 0(n) => problem size of n, the number of operations required is n or as the problem grows so does the number of steps 

# other time complexities 
# • 0(1) => constant time(time taken is always the same regardless of the problem size) 
# • 0(n^2) => Quadratic time(time taken is porpotional to the square of the problem size)
# • 0(logn) => Logarithmic time(time taken is porportional to the natural logarithm of the problem size)


# Sorting Algorithms => list of values and want to sort them in ordered list 
# ie database of contacts and want to see them alphabetically 
# retrieve five best test results or find out most recent insurance claims 


# Bubble sort algorithm 
# step 1 start with the first two elements in the list [5, 8, 1, 2, 3], so its 5 & 8 
# move on to the next two and switch positions [5, 1, 8, 2, 3]
# for next pair switch the positions [5, 1, 2, 8, 3]
# for the final pair, switch the positions again [5, 1, 2, 3, 8]
# go back and repeat the same process

# implement this in python 
list_ofnumbers = [5, 8, 1, 2, 3]
# indicator to tell us when to stop looping through the array 
still_swap = True 
# look through each number 
while still_swap: 
    still_swap = False 
    for i in range(len(list_ofnumbers) -1):
        if list_ofnumbers[i] > list_ofnumbers[i + 1]:
            list_ofnumbers[i], list_ofnumbers[i + 1] = list_ofnumbers[i + 1], list_ofnumbers[i]
            still_swap = True 
print(list_ofnumbers) 

# Bubble sort is simple but inefficient algorithm, time complexity is 0(n^2) 


# Searching Algorithms, 
# search through a list of contacts, searching through a list of emails to find a reply

listofnumbers = [5, 8, 1, 2, 3]
searchfor = 8 
result = -1 # if search is unsuccesful, value -1 will remain 
for i in range(len(listofnumbers)): 
    if searchfor == listofnumbers[i]:
        result = i 
        break 
print(result) # search found the required value at position 1 

# another common sorting algorithm is binary search 
# takes a sorted array and finds the position of the target value

listnumbers = [2, 3, 5, 8, 11, 12, 18]
searchfor = 11 
start_slice = 0 
slice_end = len(listnumbers) - 1 
found = False 

while start_slice <= slice_end and not found: 
    location = (start_slice + slice_end) 
    if listnumbers[location] == searchfor:
        found = True 
    else: 
        if searchfor < listnumbers[location]: 
            slice_end = location - 1 
        else:
            start_slice = location + 1 
print(found) 
print(location) 


# Basic Functions in Python 
def addup(x, y): 
    return x * y 
addup(1, 3) 

# defining and calling a function 
def get_second_element(inalist):
    if len(inalist) > 1:
        return inalist[1]
    else:
        return "List was too small"
get_second_element([1, 2, 3])
get_second_element([1])

# Arguments in a function => Positional Arguments 
def add_down(x, y): # two positional arguments 
    return x + y 

# keyword arguments => named arguments(optional inputs to functions) 
def add_suffix(suffix=' .com'):
    return 'google' + suffix 
add_suffix() 

# Positional arguments and keyword arguments 
def convert_to_cedis(amount, rate=0.8):
    return amount / rate 

# function that will take a list of amounts 
# convert them to cedis and return the sum 
def converttocedis(poundlist, rate=0.8):
    total = 0 
    for amount in poundlist:
        total + convert_to_cedis(amount, rate = rate)
    return total 
print(converttocedis([1 , 3]))

# use kwargs to achieve the same result above 
def converttocedis(poundlist, **kwargs):
    total = 0 
    for amount in poundlist: 
        total + convert_to_cedis(amount, **kwargs) 
    return total 
print(convert_to_cedis([1, 3], rate=0.8))


# Iterative functions ?? for loops ?? 
for i in range(5): print(i) 

# simple function w a for loop 
def sum_first(n):
    result = 0 
    for i in range(n):
        result += i + 1 
    return result 
sum_first(100)

# exiting => exit the function during any point of the iteration 
def is_prime(x):
    for i in range(2, x):
        if (x % 1) == 0:
            return False 
    return True 
# test the function 
is_prime(100) 
is_prime(7) 

# Recursive functions?? when a function calls itself??
# Recursive functions ?? infinite loops ?? 
def printthenextnumber(start):
    print(start + 1) 
    return printthenextnumber(start + 1) 
printthenextnumber(5) 

# Terminations ? avoid getting stuck at infinite loops
def printnextnumber(start):
    print(start + 1) 
    if start >= 7: # terminating case 
        return "I'm bored"
    return printnextnumber(start + 1)
printnextnumber(5)


# Lambda Functions => small anonymous functions that can be defined in one line syntax 
# this function 
def add_up(x, y):
    return x + y 
print(add_up(2, 5))

# this function can be written as
add_up_lambda = lambda x, y: x + y 
print(add_up_lambda(2, 5))

# Mapping and filtering with lambda functions ?? 
