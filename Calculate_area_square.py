####################################################
# program to demo use of functions in python       #
# author     : Hari Sundararajan                   #
# function to calculate Square Root                #
# date       : 2-5-2019                            #
# version    : v1.0                                #
#################################################### 

import math

def calculate_SqRoot(side):
    area = math.sqrt(side)
    return round(area,2)

s = float(input("enter a perfect square to compute the Sq root :  "))
print("Sq Root is: ",calculate_SqRoot(s))