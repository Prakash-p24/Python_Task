# Write a function to print a factorial numbers for a given input range


#Method 1
# a = input("Enter a Number :")
# num = int(a)
# fact = 1
# for i in range(1,num+1):
#     fact = fact * i
# print(fact)

#Method 1
def factorial(n):
    result = 1
    for i in range(1,n+1):
       result = result * i
    return result

b = int(input("Enter a Number :"))
print(factorial(b))


#Method 2
def factorial_two(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_two(n-1)

a = int(input("Enter a Number :"))
print(factorial_two(a))