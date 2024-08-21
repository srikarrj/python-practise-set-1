boarding_call="Good Evening, this is the final call to AI passengers for the flight AI 466 which is planned to take off at 8.40A.M."

if(boarding_call.startswith("Good Evening")):
    print(boarding_call.replace("Good Evening","Good Morning"))

if(boarding_call.find("AI"))>=0:
    print("Welcome to Air India.")

if(boarding_call.endswith("A.M.")):
    print("Passengers are requested to have their breakfast.")

a=boarding_call.split(" ")
for i in a:
    if(i.isdigit()):
        print("Flight Number is specified to the passengers.")

print("Total number of times flight service name is specified in the boarding call:",boarding_call.count("AI"))


message="Thank you all..Have a nice journey!"

print(message.upper())

print(message.lower())



row1 = (101,"Dallas",3.5)
row2 = (102,"Atlanta",5.6)
row3 = (103,"Tokyo",9.8)
table = [row1,row2,row3]
print(table[0])
print(table[1])
print(table[2])
                    
pancard_list=["AABGT6715H", "UFFAC4352T", "IFSBD9163K", "JOOEC1225H","RWXAFE187B"] 



print(pancard_list[3][6], end=" ")

print(pancard_list[4][3:])

message="welcome to Mysore"
word=message[-7:]
if(word=="mysore"):
    print("got it")
else:
    message=message[3:14]
    print(message)


    song="JINGLE Bells jingle Bells Jingle All The Way"
song.upper()
song_words=song.split()
count=0
for word in song_words:
    if(word.startswith("jingle")):
        count=count+1
print(count)


def count_names(name_list):
    count1 = 0
    count2 = 0
    
    for name in name_list:
        # Check for "_at" pattern: the name should have exactly one character followed by "at"
        if len(name) == 3 and name[1:] == "at":
            count1 += 1
        
        # Check for "%at%" pattern: the name should contain "at" anywhere
        if "at" in name:
            count2 += 1
    
    # Use the provided print statements
    print("_at -> ", count1)
    print("%at% -> ", count2)

# Provide different names in the list and test your program
name_list = ["Hat", "Cat", "rabbit", "matter"]
count_names(name_list)

 
 