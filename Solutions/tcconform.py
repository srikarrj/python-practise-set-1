ticket_status="Confirmed"
luggage_weight=32
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=0
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared")
    elif(luggage_weight<=(weight_limit+10)):
        extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")



ticket_status="confirmed"
luggage_weight=45
weight_limit= 40
extra_luggage_charge = 10
if(ticket_status=="confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared")
    elif(luggage_weight<=(weight_limit+10)):
        extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")


    passenger_name="Chan"
passport_status="valid"
if(passport_status=="valid"):
 print("Airport security cleared")
else:
 print("Invalid passport")
ticket_status="Confirmed"
luggage_weight=42
weight_limit=30  #Weight limit for the airline
extra_luggage_charge=500
if(ticket_status=="Confirmed"):
    if(luggage_weight>0 and luggage_weight<=weight_limit):
        print("Check-in cleared")
    elif(luggage_weight<=(weight_limit+10)):
        extra_luggage_charge=300*(luggage_weight-weight_limit)
    else:
        extra_luggage_charge=500*(luggage_weight-weight_limit)
    if(extra_luggage_charge>0):
        print("Extra luggage charge is Rs.", extra_luggage_charge)
        print("Please make the payment to clear check-in")
else:
    print("Sorry, ticket is not confirmed")