"""
a = [1,2,3,4,5]
b = ['a','b','c','d','e']

c = []

z = 0
while(z < len(a)):
    c.append(a[z])
    c.append(b[z])
    z += 1
#print (c)
"""

"""
myStr = 'aaaaaaaaaasssssssssffffffdddddeeeccccccccccbbbbbbasssccccc'
di ={}

mySet = set(myStr)
for i in mySet:
    count = 0
    for j in myStr:
        if (i == j):
            count +=1
        di[i] = count
print (di)
"""

#list comprehensions
"""
for i in range(1,11):
   if(i%2==0):
       print(i)
"""
"""
myLi = range(1,11)
li = [i for i in myLi if(i%2 == 0)]
print(li)
"""

#Functions**********************
"""
def myFunction():
    print ("Hello World")
myFunction()

def addition(a,b):
    #print(a+b)
    return a+b

x = addition(5,6)
y = addition(8,9)

print (x,y)
"""

"""
def sq(a):
    return a*a
h = sq(5)
print(h)
"""

"""
def great(a,b):
    if a>b:
        return("A is greater")
    elif b>a:
        return("B is greater")
    else:
        return("Equal")
    return 
z = great(5,5)
print (z)
"""

"""
def great(a,b,c):
    if a>b and a>c:
        return("A is greater")
    elif b>a and b>c:
        return("B is greater")
    elif c>a and c>b:
        return("C is greater")
    else:
        return("Equal")
z = great(5,5,6)
print (z)
"""

"""
a = [5,6,7]
def grtli(a):
    b = 0
    for i in a:
        if i>b:
            b=i
    return b
print(grtli(a))
"""

"""
a = ['shiud','dfhdthxdthx','fghdzhdzfhdfhdf','dzfhzdf']
def great(a):
    b = ''
    for i in a:
        if len(i)>len(b):
            b=i
    return b
print(great(a))
 """

"""

**********
*we      *
*are     *  
*learning*
*python  *
**********

"""


li = ('we','are','learning','python')
x = ''
for i in li:
    if len(i)>len(x):
        x=i
print("Length of longest word:",len(x))

l = len(x)+2
print('*'*l)
for i in li:
    c = 0
    if(len(x)>len(i)):
        c = len(x) - len(i)
    print('*'+i+(' '*c)+'*')
print('*'*l)

















