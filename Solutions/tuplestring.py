#Creating a string
pancard_number="AABGT6715H"

#Length of the string
print("Length of the PAN card number:", len(pancard_number))

#Concatenating two strings
name1 ="PAN "
name2="card"
name=name1+name2
print(name)

print("Iterating the string using range()")
for index in range(0,len(pancard_number)):
    print(pancard_number[index])
    
print("Iterating the string using keyword in")
for value in pancard_number:
    print(value)

print("Searching for a character in string")
if "H" in pancard_number:
    print("Character present")
else:
    print("Character is not present")

#Slicing a string
print("The numbers in the PAN card number:", pancard_number[5:9])
print("Last but one 3 characters in the PAN card:",pancard_number[-4:-1])

def generate_ticket(airline, source, destination, no_of_passengers):
    ticket_number_list = []
    
    # Extract the first three characters of source and destination
    src_code = source[:3]
    dest_code = destination[:3]
    
    # Generate ticket numbers
    for i in range(101, 101 + no_of_passengers):
        ticket = f"{airline}:{src_code}:{dest_code}:{i}"
        ticket_number_list.append(ticket)
    
    # Return the last five tickets, or all if less than 5
    return ticket_number_list[-5:]

# Test cases
print(generate_ticket("AI", "Bangalore", "London", 7))
print(generate_ticket("BA", "Australia", "France", 2))
