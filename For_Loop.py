# # 1. Print Ther First 10 Natural Numbers using For Loop
# n = 11
# for i in range(1,n):
#     print(i)


    
# # 2. Python Program to Print All The Even Numbers Within the given Range.

# given_range = 10

# for i in range(given_range):
#     if i%2==0:
#         print(i)      
        
        
# # 3. Python Program to Calculate the Sum of All Numbers from 1 to a given number.
    
#     given_number = 10 
#     sum = 0
    
#     for i in range(1,given_number+1):
#         sum+=i
        
#         print(sum)
        

# # 4. Python Program to Calculate the sum of all the odd numbers within the given range..

# given_range = 10

# sum = 0

# for i in range(given_range):
#     if i%2!=0:
#         sum+=i
        
#     print(sum)            
    
    
# # 5. Python Program To Print a Multiplication Table Of a Given Number 

# given_number = 5

# for i in range(11):
#     print(given_number,"X",i,"=",5*i)    
    
    
# 6. Python Program To Display Numbers From a List Using a For Loop

# list = [1,2,4,6,88,125]
# for i in list:
#     print(i)
    
    
# 7. Python Program To Count The Total Number Of Digits In a Number.

# given_number = 129475 
# given_number = str(given_number)
# count = 0

# for i in given_number:
#     count += 1
    
# print(count)    


# 8. Python Program To Check If The Given String Is a Palindrome..

# given_string = "madam"
# reverse_string=""

# for i in given_string:
#     reverse_string = i + reverse_string
    
#     if(given_string == reverse_string):
#         print("The String",given_string,"Is a Palindorme.")
        
#     else:
#         print("The String",given_string,"Is Not a Palindrome.")
        
        
# 9. Python Program That Accepts a Word From The User and Reverse it.

# given_string = input()
# reverse_string=""

# for i in given_string:
#     reverse_string = i + reverse_string
    
#     print(reverse_string)        
    
    
# 10. Python Program To Check Is a Given Number Is An Armstrong NUmber


# given_number = 153
# given_number = str(given_number)
# string_length = len(given_number)

# sum = 0

# for i in given_number:
#     sum+=int(i)**string_length
    
# if sum == int(given_number):
#     print("The Given Number",given_number,"Is An Armstrong Number.")
    
# else:
#     print("The Given Number",given_number,"Is Not An Armstrong Number.")        
    
    
    
# 11. Python Program To Count The Number Of Even And Odd Numbers From a Series Of Numbers.

# num_list = [1,3,5,6,99,134,55]

# for i in num_list:
#     if i%2==0:
#         print(i,"Is An Even Number.")
        
#     else:
#         print(i,"Is An Odd Number...")        
        
        
        
# 12. Python program to display all numbers within a range except the prime numbers.

import math

def is_not_prime(n):
    flag = False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            flag = True
        return flag
    
    range_starts = 10
    
    range_ends = 30 
    print("Non-Prime Numbers Between",range_starts,"and",range_ends,"are:") 
    
    for number in filter(is_not_prime,range(range_starts,range_ends)):
        print(number)
        
        
        
# nums = [25,30,55,40,45]

# nums[0:5:-1]
# []        