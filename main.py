"""
Exercise 2

I am writing a version of the sum funciton in python

The challenge here is to write a mysum function that does the same thing as the
built-in sum function. However, instead of taking a single sequence as a parameter, it
should take a variable number of arguments. Thus, although you might invoke
sum([1,2,3]) , you would instead invoke mysum(1,2,3) or mysum(10,20,30,40,50).
"""

def mysum(*numbers):
    sum = 0
    for x in numbers:
        sum += x
    return sum

print(mysum(*[1, 3, 5]))
print(mysum(1, 2, 3, 4))