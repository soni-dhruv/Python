#module AND packages

"""
any .py file -> call one module to another module
"""
#import one as o
"""
one.function1()
one.function3()
"""

#o.function1()
"""
from one import function1 as f1, function2 as f2
f1()
f2()
"""


def guess_the_number():
    n = int(input("Enter number:"))
    if(n == 55):
        print("Won")
    elif(n > 55):
        print("Greater number")
        guess_the_number()
    elif(n < 55):
        print("Smaller")
        guess_the_number()
guess_the_number()


"""
def guess_the_number():
    while(True):
        n = int(input("Enter number:"))
        if(n == 55):
            print("Won")
            break
        elif(n > 55):
            print("Greater number")
        elif(n < 55):
            print("Smaller")
        
guess_the_number()
"""
