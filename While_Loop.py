# 1. Find the greatest common divisior(GCD) of two numbers using the Euclidean ALgorithm:

a = 56
b = 98

while b != 0:
    a, b = b, a%b
    
    print(f"GCD is {a}")
    
    
# 2.  Reverse a Given Integer:

n = 12345
reversed_num = 0

while n > 0:
    remainder = n % 10
    reversed_num = reversed_num * 10 + remainder
    n //= 10
    
    print(f"Reversed Number Is {reversed_num}")    
    
    
# 3. Print the Fibonacci Sequence Until a Number Greater than 100 is found:

a, b = 0,1

while a <= 100:
    print(a)
    a, b = b, a + b    
    
    
    
# 4. Sum Of Digits Of a Number 

n = 1234
sum_digits = 0

while n > 0:
    sum_digits += n % 10
    n //= 10
    
    print(f"Sum Of Digits Is {sum_digits}")
    
    
# 5. Check Is a Number Is a Palindrome :

n = 121
original_n = n 
reversed_num = 0

while n > 0:
    reversed_num = reversed_num * 10 + n % 10
    n //= 10
    
    if original_n == reversed_num:
        print(f"{original_n} is a palindrome..")
        
    else:
        print(f"{original_n}Is Not a Plaindrome...")    
        
        
# 6. Simulate a guessing game where the user has to guess a number between 1 and 10

import random
secret_number = random.randint(1,10)
guess = None

while guess != secret_number:
    guess = int(input("Guess The Number (Between 1 And 10 ): "))
    if guess < secret_number:
        print("Too Low!")
    elif guess > secret_number:
        print("Too High!")
    else:
        print("Correct! You've Guessed It..")        
        
        
# 7. Find the Number Of Digits In an Integer:

n = 12345
count = 0

while n > 0:
    n //= 10
    count += 1
    
    print(f"Number Of Digits is {count}")        
    
    
    
# 8. Convert a Decimal Number To Binary:

n = 25
binary_representation = ""

while n > 0:
    binary_representation = str(n % 2) + binary_representation
    n //= 2
    
    print(f"Binary Representation Is{binary_representation}")     
    
    
# 9. Find the First Number In the Collatz Sequence to Reach 1 For a Given Starting Number:

n = 13

while n != 1:
    print(n)
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
        
        print(n)        
        
        
# 10. Check if a Number Is Prime

n = 29
i = 2
is_prime = True

while i <= n // 2:
    if n % i == 0:
        is_prime = False
        break
    i += 1
    
    if is_prime:
        print(f"{n} is a prime number..")
    else:
        print(f"{n} is not a prime number..")            