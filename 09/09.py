import pandas as pd
import numpy as np

"""
data = pd.read_csv('studData.csv')
print(data)
#This structure is called Data Frame
"""

"""
di = {'col1':[1,2,3,4,5],'col2':[6,7,8,9,0]}
df = pd.DataFrame(di)
#print(df)
"""

"""
print(data['Physics'])
print(data['Physics'].tolist())
"""

"""
data['Total'] = data['Physics']+data['Chemistry']+data['Maths']
print(data)
"""

"""
print(data[data['Physics'] > 40])
print(data[(data['Physics'] > 40) & (data['Total'] > 200)])
"""

"""
data['col'] = [1,2,3,4,5,6,7,8,9,0]
print(data)
"""

"""
def get_result(x):
    if(x>40):
        return "Pass"
    else:
        return "Fail"
"""

""" 
data['result of Physics'] = data['Physics'].apply(get_result)
data['result'] = data['Physics'].apply(lambda x:"Pass" if(x>40) else "Fail")
print(data)

#axis 0 is row, 1 is column
print(data.drop(['Chemistry','Maths',],axis=1))
"""

"""
#to set Index Column from data
data.set_index('StudentID',inplace=True)

#to del or change in main file by making new file "data.to.csv(newData.csv)"
#have to make new excel file to make cahnges
#Main origin file data cannot be changed
data.to_csv('newData2.csv')
#print(data.to_csv)
"""

#1D array
"""
a = np.array([1,2,3])
print(a)
print(a[1])
"""

"""
#RESHAPE FUNCTION
#2D array using reshape function
b = np.arange(1,16).reshape(3,5)
print(b)

#3D array using reshape function
c = np.arange(1,65).reshape(4,4,4)
print(c)
print(c[0][2][2]) #printing element fron Index

#4D array using reshape function
d = np.arange(625).reshape(5,5,5,5)
print(d)

aa = np.arrange(30).reshape(2,5,3)

#Size of array
print(d.size)

#Shape of array
print(d.shape)

#Dimensions
print(d.dtype)

#Data Type
print(type(d))
"""