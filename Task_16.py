#Input: [1234, 567, 89, 10]
#output: [10, 18, 17, 1]

#Method 1

# def sum(n):
#     result = []
#     for i in n:
#         temp = i
#         total = 0
#         while temp > 0:
#             digit = temp % 10
#             total += digit
#             temp = temp // 10
#         result.append(total)
#     return result
# num = list(map(int,input("Enter a Number").split(",")))
# print(sum(num))

#Method 2
def sum(n):
    result = []
    for i in n:
        total = 0
        for j in str(i):
            total +=int(j)
        result.append(total)
    return result
num = list(map(int,input("Enter a Number").split(",")))
print(sum(num))
