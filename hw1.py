# Name: Nicholas Mendelson
# Evergreen Login: mennic31
# Computer Science Foundations
# Programming as a Way of Life
# Homework 1

# You may do your work by editing this file, or by typing code at the
# command line and copying it into the appropriate part of this file when
# you are done.  When you are done, running this file should compute and
# print the answers to all the problems.

import math                     # makes the math.sqrt function available


###
### Problem 1
###

print "Problem 1 solution follows:"

a = 1
b = -5.86
c = 8.5408

root1 = (-b+math.sqrt(b**2-4*a*c))/2*a
root2 = (-b-math.sqrt(b**2-4*a*c))/2*a
print root1
print root2

# root1 fides one root and root2 finds the other.


###
### Problem 2
###

print "Problem 2 solution follows:"

import hw1_test
print hw1_test.a
print hw1_test.b
print hw1_test.c
print hw1_test.d
print hw1_test.e
print hw1_test.f


# ... write your code and comments here (and remove this line)


###
### Problem 3
###

print "Problem 3 solution follows:"
#((a and b) or (not c) and not (d or e or f))

g = hw1_test.a == hw1_test.b
h = not hw1_test.c
i = not hw1_test.d | hw1_test.e |hw1_test.f

j = g | h
k = j != i
print k




# Each line tests one part of the question for g, h, and i. J and k repersent the "or" and "and not" in the question.


###
### Collaboration
###

# ... List your collaborators and other sources of help here (websites, books, etc.),
# ... as a comment (on a line starting with "#").

###
### Reflection
###

# ... Took a long time to figure out question 1. restarted problem after lab and finished it in over an hour. That did not include the hour of reading the Python book last night.
