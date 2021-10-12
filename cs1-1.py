# Author: SMR (AMDG) 10/12/21
x_value_1=int(input("What is the x value of the first point? "))
y_value_1=int(input("What is the y value of the first point? "))
x_value_2=int(input("What is the x value of the second point? "))
y_value_2=int(input("What is the y value of the second point?"))
distance= (((x_value_2-x_value_1)**2)+((y_value_2-y_value_1)**2))**(1/2)
print("The distance between the two points is",distance)

