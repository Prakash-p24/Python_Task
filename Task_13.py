
#Method 1

# try:
#     num = int(input("Enter a Number :"))
# except Exception as e:
#     print("Error is",e)
# else:
#     def integer_handling(num):
#         result = ""
#         n = str(num)
#         for i in n[::-1]:
#             result += i
#         return result

# print(integer_handling(num))

# #Method 2
# def integer_handling(num,i):  
#     if i == 0: 
#         return num[i]   
#     return num[i]+ integer_handling(num,i-1)
# num = int(input("Enter a Number :"))
# n = str(num)
# a = integer_handling(n,len(n)-1) 
# print(a) 


#Method 3
def integer_handling(n):
    temp = n
    while temp > 0:
        digit = temp % 10
        temp = temp // 10
        print(digit,end="")

n = int(input("Enter a Number :"))
integer_handling(n)

