# Name: Nicholas Mendelson
# Evergreen Login: mennic31
# Computer Science Foundations
# Programming as a Way of Life
# Homework 2

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math

###
### Problem 1
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 1 solution follows:"

import hw2_test
x = 0
answer1 = 0
while (x<hw2_test.n):
    x = x+1
    answer1 = answer1 + x

print "The Answer to Gauss's Problem is " ,answer1







###
### Problem 2
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 2 solution follows:"

num = 0.00
den = 1.00


for num in range(2, 11):
    a = (num) / den
    print a


###
### Problem 3
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 3 solution follows:"

n = 10
triangular = 0
for i in range(n+1):
    triangular += i

print "Triangular number", n, "via loop:", triangular
print "Triangular number", n, "via formula:", n*(n+1)/2


###
### Problem 4
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 4 solution follows:"

result = 1



###
### Problem 5
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 5 solution follows:"

for i in range(n):
    result *=i+1
    n = n-1
    print result

###
### Problem 6
###

# DO NOT CHANGE THE FOLLOWING LINE
print "Problem 6 solution follows:"


n = 10
f1=1
f2 = 1
for i in range(n):
    f2 = f2 + (1/f1)
    f1=1
    x = n-i 
    for j in range(x):
        f1= f1*(j+1)/1.0
        
    print f2




###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").
# Grading partner: ngutro25

###
### Reflection
###

# ... Write how long this assignment took you, including doing all the readings
# ... and tutorials linked to from the homework page. Did the readings, tutorials,
# ... and lecture contain everything you needed to complete this assignment?
