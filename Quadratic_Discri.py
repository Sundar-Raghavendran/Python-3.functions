#### function   : calculate the roots of a quadratic equation     ####
#### Authors    : Sundar raghavendran & Hari Sundararajan         ####
#### Date       : Feb-10-2019                                     #### 

import math 

def calculate_discriminant(a,b,c): 
    return round(((math.pow(b,2)) - (4*a*c)), 2)

coeff_a = float(input("enter the value of coefficient a : "))
coeff_b = float(input("enter the value of coefficient b : "))
coeff_c = float(input("enter the value of coefficient c : ")) 

disc = calculate_discriminant(coeff_a,coeff_b,coeff_c)
print("The equation is : (",coeff_a,"x^2) + (",coeff_b,"x) + (",coeff_c,") = 0")
print("The discriminant for the above equation is :", disc)

if disc > 0:
    print("There are two roots for this equation")
    root1 = (-(coeff_b) + math.sqrt(disc))/(2*coeff_a)
    root2 = (-(coeff_b) - math.sqrt(disc))/(2*coeff_a)
    print("The roots are : ",root1," and ", root2)

elif disc == 0:
        print("There is one root for this equation.")
        root = -(coeff_b)/(2*coeff_a)
        print("the root is: ",root)

else:
    print("There are no roots for this equation.")   