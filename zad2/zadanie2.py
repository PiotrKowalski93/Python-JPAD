# -*- coding: utf-8 -*-
"""
Created on Sat Mar 24 09:07:16 2018

@author: Kowalski Piotr, Małgorzata Szymczyńska
"""
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.linear_model import LinearRegression

with open('iris.data') as my_file:
    testsite_array = my_file.readlines()

#print(testsite_array.count)

dataArray = []

#print(dataArray)

for i in range(len(testsite_array)):
    repleacedChars = testsite_array[i].replace('\n','')
    splitted = repleacedChars.split(",")
    for x in range(0, 4): 
        splitted[x] = float(splitted[x])
    dataArray.append(splitted)
    
#print(dataArray)
    
    
# -----------------------------------------------------------------------------
print()
print("--------- MinMax ---------")
    
    
# Max Sepal length
maxValue = 0;

for i in range(len(dataArray)):
    line = dataArray[i][0]
    value = line;
    if dataArray[i][0] > maxValue:
        maxValue = dataArray[i][0];
    

print('Max Sepal length: ' + str(maxValue));

# Min Sepal length
for i in range(len(dataArray)):
    line = dataArray[i][0]
    value = line;
    if dataArray[i][0] < maxValue:
        maxValue = dataArray[i][0];
    

print('Min Sepal length: ' + str(maxValue));

# Max Sepal width
maxValue = 0;

for i in range(len(dataArray)):
    line = dataArray[i][1]
    value = line;
    if dataArray[i][1] > maxValue:
        maxValue = dataArray[i][1];
    

print('Max Sepal width: ' + str(maxValue));

# Min Sepal width
for i in range(len(dataArray)):
    line = dataArray[i][1]
    value = line;
    if dataArray[i][1] < maxValue:
        maxValue = dataArray[i][1];
    

print('Min Sepal width: ' + str(maxValue));    
   
# Max Petal length
maxValue = 0;

for i in range(len(dataArray)):
    line = dataArray[i][2]
    value = line;
    if dataArray[i][2] > maxValue:
        maxValue = dataArray[i][2];
    

print('Max Petal length: ' + str(maxValue)); 
        

# Min Petal lenght
for i in range(len(dataArray)):
    line = dataArray[i][2]
    value = line;
    if dataArray[i][2] < maxValue:
        maxValue = dataArray[i][2];
    

print('Min Petal lenght: ' + str(maxValue));

# Max Petal width
maxValue = 0;

for i in range(len(dataArray)):
    line = dataArray[i][3]
    value = line;
    if dataArray[i][3] > maxValue:
        maxValue = dataArray[i][3];
    

print('Max Petal width: ' + str(maxValue));

# Min Petal width
for i in range(len(dataArray)):
    line = dataArray[i][3]
    value = line;
    if dataArray[i][3] < maxValue:
        maxValue = dataArray[i][3];
    

print('Min Petal width: ' + str(maxValue));

# -----------------------------------------------------------------------------
print()
print("--------- Median ---------")

# Mediana Sepal Length
x = len(dataArray) % 2;

if x == 0:
    centerIndex = len(dataArray) / 2;
    a = dataArray[int(centerIndex)][0]
    b = dataArray[int(centerIndex + 1)][0]
    m = ((a+b)/2)
    print('Median for Sepal Length: ' + str(m))
    
# Mediana Sepal Width
if x == 0:
    centerIndex = len(dataArray) / 2;
    a = dataArray[int(centerIndex)][1]
    b = dataArray[int(centerIndex + 1)][1]
    m = ((a+b)/2)
    print('Median for Sepal Width: ' + str(m))
    
# Mediana Petal Length
if x == 0:
    centerIndex = len(dataArray) / 2;
    a = dataArray[int(centerIndex)][2]
    b = dataArray[int(centerIndex + 1)][2]
    m = ((a+b)/2)
    print('Median for Petal Length: ' + str(m))

# Mediana Petal Width
if x == 0:
    centerIndex = len(dataArray) / 2;
    a = dataArray[int(centerIndex)][3]
    b = dataArray[int(centerIndex + 1)][3]
    m = ((a+b)/2)
    print('Median for Petal Width: ' + str(m))

print()
a = []
b = []
c = []
d = []


for i in range(len(dataArray)):
    a.append(dataArray[i][0])
    b.append(dataArray[i][1])
    c.append(dataArray[i][2])
    d.append(dataArray[i][3])

print()
print('Correlation: ')
print('a/a: ' + str(np.corrcoef(a, a)[1,0]))
print('a/b: ' + str(np.corrcoef(a, b)[1,0]))
print('a/c: ' + str(np.corrcoef(a, c)[1,0]))
print('a/d: ' + str(np.corrcoef(a, d)[1,0]))
print('b/b: ' + str(np.corrcoef(b, b)[1,0]))
print('b/c: ' + str(np.corrcoef(b, c)[1,0]))
print('b/d: ' + str(np.corrcoef(b, d)[1,0]))
print('c/c: ' + str(np.corrcoef(c, c)[1,0]))
print('c/d: ' + str(np.corrcoef(c, d)[1,0]))
print('d/d: ' + str(np.corrcoef(d, d)[1,0]))
# -----------------------------------------------------------------------------
print()
print("--------- Mode ---------")

i = 0;

satosa = 'Iris-setosa'
versicolor = 'Iris-versicolor'
virginica = 'Iris-virginica'

satosaCount = 0;
versicolorCount = 0;
virginicaCount = 0;

for i in range(len(dataArray)):
    rowType = dataArray[i][4]
    if rowType == satosa:
        satosaCount = satosaCount + 1
    if rowType == versicolor:
        versicolorCount = versicolorCount + 1
    if rowType == virginica:
        virginicaCount = virginicaCount + 1

print(satosa + ': ' + str(satosaCount))
print(versicolor + ': ' + str(versicolorCount))
print(virginica + ': ' + str(virginicaCount))

# -----------------------------------------------------------------------------
print()
print("--------- Histograms ---------")

# Petal Length
x = []

for i in range(len(dataArray)):
    x.append(dataArray[i][2])

plt.hist(x, density=False)
plt.title('Petal Lenght Histogram')
plt.xlabel('Petal Length');
plt.ylabel('Count');
plt.show()
plt.clf()

# Petal Width
x = []

for i in range(len(dataArray)):
    x.append(dataArray[i][3])

plt.hist(x, density=False)
plt.title('Petal Width Histogram')
plt.xlabel('Petal Width');
plt.ylabel('Count');
plt.show()
plt.clf()

# Linear Regression

def linearRegr(plotX,plotY):   
    x_data=np.array(plotX).reshape(len(plotX),1)
    y_data=np.array(plotY).reshape(len(plotY),1)
    plt.scatter(x_data, y_data,  color='r')
    regr = linear_model.LinearRegression()
    regr.fit(x_data, y_data)
    plt.plot(x_data, regr.predict(x_data), color='k',linewidth=3)
    
x = []
y= []

for i in range(len(dataArray)):
    x.append(dataArray[i][2])
for i in range(len(dataArray)):
    y.append(dataArray[i][3])
    
linearRegr(x,y)

"""
ar = [1,2,3]
print('array')
print(ar)
print('np.array')
print(np.array(ar))
print('reshape')
print(np.array(ar).reshape(len(ar),1))
"""

