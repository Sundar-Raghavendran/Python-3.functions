import math 

#### learning - functions           ######
#### Code author: Hari Sundararajan ######

def Area_Trapezoid(a_side,b_side,height):
    area = (a_side+b_side)/2 * height
    return area

a = float(input("Length of the top leg?"))
b = float(input("Length of the bottom leg?"))
h = float(input("What's the height?"))

area = Area_Trapezoid(a,b,h)
print("The area of the trapezoid is: ",area, "units")

#### learning Lists                 ######
#### Code author: Hari Sundararajan ######

Cities = ["Naperville", "Plano", "Madras"]
print(Cities)

for city in Cities:
    print(city)