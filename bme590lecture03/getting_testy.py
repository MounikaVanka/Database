import pytest
def add(a, b):
    a=input("enter 1st Number")
    b=input("Enter 2nd Number")
    if (type(a) or type(b)) is (int or float or double):
        print("INVALID INPUT")
    elif((a or b)<0):
        print(0)
        return 0
    else:
        c = a + b
        print(c)
        return c


def testOne():
    assert(add(-2, 1) == 0)

def testTwo():
    assert(add(1, 1) == 2)
        
def testThree():
    assert(add(1, 1) == 2)
        
def testFour():
    assert(add(3.1, 4.2) == 7.3) 
        
def testFive():
    assert(add(3.1, 1) == 4.1)  
        
def testSix():
    assert(add("3.1", 1) == "invalid input")  
    
testOne()
testTwo()
testThree()
testFour()
testFive()
testSix()
    


