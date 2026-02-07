# a = input("Enter a Number :")
# result = 0
# second_half = 0
# for i in a:
#     result +=int(i)
# if len(str(result)) > 1:
#       for j in str(result):
#             second_half += int(j)    

#       if second_half == 1:
#         print(f"{second_half} is a Magic Number")
     
#       else:
#         print(f" {second_half} is not Magic Number")
# elif result == 1:
#     print(f"{result} is a Magic Number")    
# else:
#     print(f"{result}is not Magic Number")



# a = input("Enter a number :")
# temp = abs(int(a))
# n = len(str(temp))
# result = 0
# while n != 0 and result < 9:
#     digit = (temp % 10)
#     print(digit)
#     result = result + digit
#     print(result)
#     temp = (temp // 10)   
#     n = n-1

# if len(str(result)) > 1:
#     # n = len(str(result))
#     second_half = len(str(result))
#     print(second_half)
#     second_result = 0
#     while second_half != 0:
#         second_result = second_result + int(result) % 10
#         result = result // 10
#         second_half = second_half - 1
#     if int(second_result) == 1:
#         print(f"{second_result} is magic number")
#     else:
#         print(f"{second_result} is not magic number")
# elif result == 1:
#     print(f"{result} is magic number")

# else:
#     print(f"{result} is not magic number")





# def magic_number(a):
#     temp = abs(int(a))
#     while temp > 9 :
#         result = 0
#         while temp != 0:
#             digit = temp % 10
#             result = result + digit
#             temp = temp // 10
#         temp = result
#     return temp

# a=input("Enter a Number :")
# temp = magic_number(a)
# if temp == 1:
#     print(f"{temp} is a Magic Number")
# else:
#     print(f"{temp} is not a Magic Number")





# def armstrong(n):
#     temp = int(n)
#     power = len(n)
#     result = 0
#     while temp > 0:
#         digit = temp % 10
#         result = result + (digit ** power)
#         temp = temp // 10
#     return result

# n = input("Enter a Number :")
# result = armstrong(n)
# if result == int(n):
#     print("It is a Armstrong Number")
# else:
#     print("Not Armstrong Number")


# num = int(input("Enter a number: "))
# power = len(str(num))

# def armstrong_sum(n):
#     if n == 0:
#         return 0
#     return (n % 10) ** power + armstrong_sum(n // 10)

# if armstrong_sum(num) == num:
#     print("Armstrong Number")
# else:
#     print("Not an Armstrong Number")

num = int(input("Enter a number: "))

def sum_of_digits(num):
    if num == 0:
        return 0
     
    return (num % 10) + int(sum_of_digits(num // 10))

def length(a):
    if len(str(a)) > 1:
        return sum_of_digits(a)
    else:
        return a
first = sum_of_digits(num)
second = length(first)

if second==1:
   
    print("Magic Number")
else:
    print("Not Magic Number")



