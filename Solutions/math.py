import math
num1=234.01
num2=6
num3=-27.01

print("The smallest integer greater than or equal to num1,",num1,":",math.ceil(num1))
print("The largest integer smaller than or equal to num1,",num1,":",math.floor(num1))
print("The factorial of num2,",num2,":", math.factorial(num2))
print("The absolute value of num3",num3,":",math.fabs(num3))
import time
import datetime

#To get current GM time
print("Current GM time:",time.gmtime())
#This returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

#To get current local time
print("Current local time:",time.localtime())
#This also returns a time structure containing 9 values - year, month,day, hour, minute, sec, day of week, day of year and daylight savings.

#To extract today's date in a specified string format
print("Today's date using time module",time.strftime("%m-%m/%Y"))

#Python additionally allows use of  datetime module
#Prints today's date
print("Today's date using datetime module:", datetime.date.today())

#To extract today's date in a specified string format
print("Today's date (dd/mm/yyyy) using datetime module:", datetime.date.today().strftime("%d/%m/%Y"))


#To convert a date in string format to datetime value
print("Today's date (dd/mm/yyyy):", datetime.datetime.strptime("17/04/1","%y/%d/%m"))