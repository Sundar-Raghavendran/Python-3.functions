####################################################
# program to demo use of functions in python       #
# author     : Sundar Raghavendran                 #
# function to calculate bmi,given height & weight  #
# date       : 2-4-2019                            #
# version    : v1.0                                #
####################################################  

import  math

def calculate_bmi(name,height_m,weight_kg):
    bmi = round(weight_kg/(pow(height_m,2)), 2)
    return bmi
  
name      = input("what's your name?")
weight_kg = float(input("what's your weight in Kgs?"))
height_m  = float(input("what's your height in meters?"))

print("Hello ", name,". How are you ?. The BMI calculator will advise shortly ")
your_bmi = calculate_bmi(name,height_m,weight_kg)
print(name + "'s bmi is : ", your_bmi)

if your_bmi >= 25:
    print(name + " is overweight")
    desired_weight = 25 * pow(height_m,2) 
    # bcoz bmi=weight/height-squared, 
    # weight = bmi*height-squared
    print("you need to reduce ", round(weight_kg-desired_weight,2) , "kgs to get good bmi score")
else:
    print(name + " is not overweight")
    boosted_weight = 25 * pow(height_m,2)
    print("you could go upto ", round(boosted_weight-weight_kg,2), "kgs and still be in good bmi score")