from cmath import pi
import math

# def area(r):
#     area = math.pi*pow(r,2)
#     return print("The area of the circle is: ",area)   
# area(5)

def findArea(r):
    pi = 3.14
    return pi*(r*r)

print("Area is %.6f"% findArea(5))