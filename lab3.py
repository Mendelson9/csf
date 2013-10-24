# Name: Nicholas Mendelson
# Evergreen Login: mennic31
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3

# defineing series, our main decider whether our program will print Fibonacci or 3*n 
#series shoudl equal "fibonacci" or "sum". Any other string will result in error.
series = 'fibonacci'

#pre defining variables: n is assigned some number the rest defines parts of fibonacci number
n = 12
x = 0
f1 = 1
f2 = 0
ans = 0

#function that calulates Fibonacci number n times or if false, will calculate n times 3.
#if both fail then we print "invalid string"
if 'fibonacci' == series:
    for x in range(0,n):
        
        ans = f1 + f2
        f1 = f2
        f2 = ans
    print ans
    
elif 'sum' == series:       #when if statement fails, function will check for sum
    sumAnswer = 3*n
    print sumAnswer
    
else:
    print "Invalid string"     