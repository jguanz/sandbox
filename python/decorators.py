import sys
import os
import random

def squared(func):
    def q_wrapper():
        if(random.randint(1,10) % 2 == 0):
            print func()
        else:
            print "hello"
    return q_wrapper

# def squared2(func):


@squared
@squared
def add():
   return 0

add()
