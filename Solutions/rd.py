print("________________________________________________________________________")
print("BREAD BASKET")
print("Looking for a healthy breakfast, this is the place for you!!")
print("________________________________________________________________________")
print("Raisin Toast$2.50")
print("French Toast$2.80")
print("Mushroom Toast$3.00")
print("Pancake$4.00")
print("Pancake with Ice-cream$7.50")
print("Chef's speciality$10.00")
print("__________________________________________________________________________")

num1=100
num2=200
num3=6
if(5>=num3):
    if(num1>100 or num2>150):
        print("1")
elif(num1>=100 and num2>150):
    print("2")
else:
    print("3")
 


if((num1/num2==5) and (num1+num2)>5):
    print("1")
elif((num1-num2)<=1 or (num1%num2)==0):
    print("2")
else:
    print("3")






for number in range(1,5):
    print ("The current number is ",number)

print("---------------------------")

for number in range(1,7,2):
    print ("The current number is ",number)

print("---------------------------")

for number in range(5,0,-1):
    print ("The current number is ",number)


number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    for baggage_count in range(1,number_of_baggage+1):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared") 


number_of_passengers=5
number_of_baggage=2
security_check=True
for passenger_count in range(1, number_of_passengers+1):
    baggage_count =1
    while (baggage_count<=number_of_baggage):
        if(security_check==True):
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage cleared")
        else:
            print("Security check of passenger:", passenger_count, "-- baggage:", baggage_count,"baggage not cleared")
        baggage_count+=1



#Assume A – Adult passenger, C- Child, FC – Flight Captain, FA – Flight Attendant, SP – Suspicious passenger. 
for passenger in "A","A", "FC", "C", "FA", "SP", "A", "A":
 if(passenger=="FC" or passenger=="FA"):
  print("No check required")
  continue
if(passenger=="SP"):
   print("Declare emergency in the airport")
   
if(passenger=="A" or passenger=="C"):
 print("Proceed with normal security check")
print("Check the person")
print("Check for cabin baggage")