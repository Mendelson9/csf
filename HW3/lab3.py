# Name: Nicholas Mendelson
# Evergreen Login: mennic31
# Computer Science Foundations
# Programming as a Way of Life
# Homework 3


n = 10
x = 0
series = 'fibonacci'
f1 = 1
f2 = 0
ans = 0
if 'fibonacci' == series:
    for x in range(0,n):
        
        ans = f1 + f2
        f1 = f2
        f2 = ans
    print ans
    
