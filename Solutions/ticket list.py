#list can store homogeneous data
list_of_airlines=["AI","EM","BA"]
print("List of airlines:",list_of_airlines)

#list can  store heterogeneous data
sample_list=["Mark",5,"Jack",9, "Chan",5]
print("Sample List:",sample_list)

#Length of the list
print("Number of elements in the list:",len(sample_list))

#Random read
print("Element at 2nd index position:", sample_list[2])

#Random write
sample_list[2]="James"

#Random read
print("Element at 2nd index position after random write:",sample_list[2])


#Adding an element to list
sample_list.append("James")
print("After adding element to list:",sample_list)

#Combining two lists
new_list=["Henry","Tim"]
sample_list+=new_list

#Adds Henry and Tim to the existing sample_list
print("After combining two lists - 1st way:",sample_list)

#Another way to combine two lists
sample_list=sample_list+new_list

#Adds Henry and Tim to the new sample_list
print("After combining two lists - 2nd way:",sample_list)




#This is a list of lists
#Stores airline and number of flights operated by them
airline_details=[["Air india",8], ["Emirates",10],["Bharath",7]]

#To get the details of Emirates (EM) airline
#Prints a list
print(airline_details[1])

#To get the number of flights operated by British Airways (BA)
#[2][1] refers to 2nd list and 1st value, inside airline_details
#Remember counting is 0 based
print(airline_details[2][1])

#To display the details of all airlines
print("Airline details as a list:")
for airline in airline_details:
    print(airline)

#To display the number of flights operated by each airline
print("No. of flights operated by each airline:")
for airline in airline_details:
        print(airline[1])    


mark_list=[78,90,90,95,83,95]

mark_pos=mark_list.index(90)
print("Index position of mark 90:", mark_pos)

mark_list.append(54)
print("After adding new marks:",mark_list)

mark_list.insert(2, 98)
print("After inserting 98 at the 2nd index position:",mark_list)

mark_list.pop(1)
print("After removing the marks at the 1st index position:",mark_list)

mark_list.remove(95)
print("After removing the first occurence of 95 from the list:",mark_list)

mark_list.sort()
print("After sorting the marks in the given list:",mark_list)

mark_list.reverse()
print("After reversing the marks in the given list:",mark_list)

num_list = [100.5,30.465,-1.22,20.15]
num_list.insert(1, -100.5)
num_list.pop(0)
num_list.sort()
print(num_list[0])
 
'''Given a list of integer values. Write a python program to check whether it contains same number in adjacent position. Display the count of such adjacent occurrences

Sample Input

Expected Output

[1,1,5,100,-20,-20,6,0,0]

3

[10,20,30,40,30,20]

0

[1,2,2,3,4,4,4,10]

3



[1,1,5,100,-20,-20,6,0,0]

3

[10,20,30,40,30,20]

0

[1,2,2,3,4,4,4,10]

3
'''


def get_count(num_list):
    count = 0
    
    # Iterate through the list, comparing each element with the next one
    for i in range(len(num_list) - 1):
        if num_list[i] == num_list[i + 1]:
            count += 1

    return count

# Provide different values in list and test your program
num_list = [1, 1, 5, 100, -20, -20, 6, 0, 0]
print(get_count(num_list))  # Expected output: 3

num_list = [10, 20, 30, 40, 30, 20]
print(get_count(num_list))  # Expected output: 0

num_list = [1, 2, 2, 3, 4, 4, 4, 10]
print(get_count(num_list))  # Expected output: 3
