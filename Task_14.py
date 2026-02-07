#Bubble sort (ascending order)

#Method 1
# def bubble(a):
#     for i in range(len(a)):
#         for j in range(i,len(a)):
#             if a[i]>a[j]:
#                 a[j],a[i]=a[i],a[j]
#     return a
# n = list(map(int, input("Enter a number : ").split(","))) 
# print(bubble(n))

#Method 2
def bubble(a,length):
    if length == 1:
        return a
    for i in range(length-1):
        if a[i] > a[i+1]:
            a[i],a[i+1] = a[i+1],a[i]
    return bubble(a,length-1)

n = list(map(int, input("Enter a number : ").split(","))) 

nums = len(n)
c=bubble(n,nums)
print(c)