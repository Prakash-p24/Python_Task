# Write a function to print a list of prime numbers for a given input range

def check_prime(n):
    primes = []
    for i in range(2,n):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            primes+=[i]
    return primes

a = int(input("Enter a Number :"))
# print(check_prime(a))   

# Prime number check using while loop

# Function to check if a number is prime
# def is_prime(num):
#     primes = []
#     if num <= 1:
#         return False
    
#     divisor = 2
#     while divisor * divisor >= num:  
#         if num % divisor == 0:
#             return False  
#         divisor += 1
#     primes.append(num)
#     # return primes

# a = input("Enter a Number :")
# n = int(a)
# for i in range(2,n+1):
#     is_prime(i)



# def check_prime_two(n):
#     primes = [i for i in range(2,n) for j in range(2,int(i*0.5)+1) if j % i !=0]
#     return primes
# a = input("Enter a Number :")
# print(check_prime_two(int(a)))

# using While Loop
# Number = int(input(" Please Enter any Num: "))
# count = 0
# i = 2

# while(i <= Number//2):
#     if(Number % i == 0):
#         count = count + 1
#         break
#     i = i + 1

# if (count == 0 and Number != 1):
#     print(" %d is a Prime" %Number)
# else:
#     print(" %d is not" %Number)
# primes = []
# def is_prime(num):
    
#     divisor = 2
    
#     # while True:  
#     n = 2
#     while n != 10:
#         if num % n != 0:
#             primes.append(num)
#         else:
#             n += 1
        
#     #     if num % divisor == 0:
#     #         return False  
#     #     divisor += 1
#     # primes.append(num)
        

#     # primes.append(num)
#     # return primes

# a = input("Enter a Number :")
# n = int(a)
# for i in range(2,n+1):
#     is_prime(i)

# print(primes)
      

# Check divisors up to sqrt(n)
# primes = []
# def prime_two(n):  
#     num = n
#     while num != 0:
#         for i in range(2,int(num**0.5) + 1):
#             if num % i == 0:
#                 num = 0
#                 break
#         else:
#             primes.append(num)
#             break
   
# a = input("Enter a Number :")
# n = int(a)
# for i in range(2,n+1):
#     prime_two(i)
# print(primes)

primes = []
def prime_two(n):   
    i = 2
    while i * i <= n: 
        if n % i == 0:
            return 
        i += 1
    
    primes.append(n)  
a = int(input("Enter a Number :"))
for i in range(2,a+1):
    prime_two(i)
print(primes)

