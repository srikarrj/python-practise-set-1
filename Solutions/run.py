airline="AirIndia"
luggage_weight=28
AI_weight_limit=30
EM_weight_limit=35
if(airline=="AirIndia"):
    if(luggage_weight<=AI_weight_limit):
        print("Check-in cleared")
    else:
        print("Remove some luggage and come back")
elif(airline=="Emirates"):
    if(luggage_weight<=EM_weight_limit):
        print("Check in cleared")
    else:
        print("Remove some luggage and come back")
else:
    print("Invalid airline")


no_of_landings=356
no_of_takeoffs=245
initial_no_of_flights=100
current_no_of_flights=initial_no_of_flights+no_of_landings-no_of_takeoffs
print("Current number of flights:",current_no_of_flights)
