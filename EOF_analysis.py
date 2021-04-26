import numpy as np
import pandas as pd
import os
from eofs.standard import Eof 

df=pd.read_csv('East_NZ2009.csv', sep=' ',header=None)       # reading the .csv files and converting to dataframe
east_matrix = np.array(df.to_numpy())
east_matrix = east_matrix.T                        # converts pandas dataframe to numpy
m = len(east_matrix)
n = len(east_matrix[0])
east_matrix = np.nan_to_num(east_matrix)                        #converting nan values to 0
for j in range(n):                                              # subtracting the mean of each row from the values.
    sum=0.0
    for i in range(m):
        sum = sum+east_matrix[i][j]
    sum/=m
    for i in range(m):
        east_matrix[i][j]-=sum
solver = Eof(east_matrix)
                               # to check the number of components
pcs=solver.pcs(pcscaling = 0 , npcs=12)
eofs=solver.eofs(eofscaling = 0, neofs=12)
new_matrix = np.matmul(pcs,eofs)                        #creates new matrix using number of components
#print(new_matrix)
#print(east_matrix)
print(east_matrix)
eigenvalues =  solver.varianceFraction()
eigenvalue1 = solver.varianceFraction(neigs=99)
print(new_matrix)
sum=0.0
for i in range(len(eigenvalue1)):
    sum+=eigenvalue1[i]
print(sum)
for i in range(len(eigenvalue1)):
    eigenvalue1[i]*=100
    eigenvalue1[i]/=sum
x=np.round(eigenvalue1,decimals=1)
print(x)