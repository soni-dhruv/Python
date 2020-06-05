#Lambda Function(to write multiple arguments in single line)

a = lambda x,y: x+y
print(a(5,6))


#IF ELSE in single line using LAMBDA
"""
z = lambda m: "Pass" if(m>50) else "Fail"
print(z(60))
"""

#Exception Handling
"""
try:
    num = int(input("Enter a Number:"))

    if (num == 0):
        raise Exception("Cannot divide by 0")
    else:
        print(50/num)
except Exception as e:
    print(e)
    #pass
"""    
""" pass keyword is used when you know exception arises but you dont want to do any thing  """
    
#Break Continue
"""
li = [1,2,3,4,5]
for i in li:
    print(i)
    if (i==3):
        break
        #continue
"""
