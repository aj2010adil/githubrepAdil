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
arr = [[1,2,3,4     ] ,
       [5,6,7,8     ], 
       [9,10,11,12  ],
       [13,14,15,16]]

def hourglass(arr):
    k=[]
    no=0
    for s in range(len(arr)-2):
        for d in range( len(arr)-2):
            no=no+1
            #print("row={} and col={}  and {} Hourglass".format(s,d,no))             
            k.append([[arr[s][d],arr[s][d+1],arr[s][d+2]],[0,arr[s+1][d+1],0],[arr[s+2][d],arr[s+2][d]+1,arr[s+2][d+2]]])      
            
    return k
def printHourglass(arr):
    no=0
    for k in range(len(arr)):
        no=no+1
        print()
        print("hourglass no {}".format(no))
        for j in range(len(arr[k])-1):
            print(hourglass(arr)[k][j])      
        
    
    
def hourglasssum(arr):
    sum = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            #print(arr[i][j], end=" ")
            sum.append(arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2])
    print(max(sum))


printHourglass(arr)
