import pytest


def add(a, b):
   

    if(type(a) is int and type(b) is int and a > 0 and b > 0):
        c=a+b
        print(c)
        return(c) 

    else:
        c=a+b
        print("Invalid Input")
        return "Invalid Input"
def TestOne():
    assert(add(-2,1) == "Invalid Input")


def TestTwo():
    assert(add(1,1) == 2)


def TestThree():
    assert(add(1,1) ==2)


TestOne()
TestTwo()
TestThree()




a=int(input("Enter 1st Number"))
b=int(input("Enter 2nd Number"))
add(a,b)
