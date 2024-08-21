name = "srikar mama"
for i in range(1000):
    print(name)


    from functools import cmp_to_key

def compare_numbers(n1, n2):
    # Custom comparator to decide the order based on concatenation
    if n1 + n2 > n2 + n1:
        return -1
    else:
        return 1

def create_largest_number(number_list):
    # Convert all numbers to strings for concatenation
    number_list = list(map(str, number_list))
    
    # Sort the list using the custom comparator
    number_list.sort(key=cmp_to_key(compare_numbers))
    
    # Join all the numbers to form the largest number
    largest_number = ''.join(number_list)
    
    return int(largest_number)

number_list = [23, 45, 67]
largest_number = create_largest_number(number_list)
print(largest_number)
#lex_auth_012693819159732224162

def check_palindrome(word):
    
 return word == word[::-1]
status=check_palindrome("mala")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")