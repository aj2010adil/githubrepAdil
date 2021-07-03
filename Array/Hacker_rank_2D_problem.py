import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#
def hourglassSum(arr1):
    # Write your code here
    '''
    This is to find the hourglass array
     abc
      d
     efg
    '''
        





#hourglassSum(arr)

T = [[1,2,3,4], [5,6,7,8], [9,10,11,12],[13,14,15,16]]
#print(T[0][1])

#Starting point of finding the hourglass fo ra given column and row 
n=4
#for i in range(0,n):
#    for k in range(0,n):
#        print(T[i][k], end=" ")
#    print()
#print("End of Array Display")
#print()
#
#for s in range(0,2):
#    print("{} Hourglass".format(s+1))       
#    print(T[s+0][0],end = " ")  
#    print(T[s+0][1],end = " ")  
#    print(T[s+0][2],end = " ")  
#    print()
#    print(end='  ')       
#    print(T[s+1][1],end = " ")  
#    print()    
#    print(T[s+2][0],end = " ")  
#    print(T[s+2][1],end = " ")  
#    print(T[s+2][2],end = " ")  
#    print()
#
##column based
#
#for s in range(0,2):
#    print("{} Column Hourglass".format(s+1))       
#    print(T[0][s+0],end = " ")  
#    print(T[1][s+0],end = " ")  
#    print(T[2][s+0],end = " ")  
#    print()
#    print(end='  ')       
#    print(T[1][s+1],end = " ")  
#    print()    
#    print(T[0][s+2],end = " ")  
#    print(T[1][s+2],end = " ")  
#    print(T[2][s+2],end = " ")  
#    print()

#automate It
k=[[1,2,3],[1,2,3]]
for s in range(0,2):
    print("{} Hourglass".format(s+1))       
    k[s+0][0]=T[s+0][0]  
    k[s+0][1]=T[s+0][1]  
    k[s+0][2]=T[s+0][2]  
    k[s+1][1]=T[s+1][1]  
    k[s+2][0]=T[s+2][0]  
    k[s+2][1]=T[s+2][1]  
    k[s+2][2]=T[s+2][2]  

























#print(T[0])
#print(type(T))
#print(T[1][2])
#