# Author: SMR (AMDG) 10/12/21
p=int(input("Enter Your Initial Investment Amount "))
r=int(input("Enter your annual interest rate a a percent "))
t=int(input("Enter the number of years that the money is in the account "))
future_investment=p*(1+((r/100)/12))**(t*12)
print("Your future value of the investment will be", future_investment)
