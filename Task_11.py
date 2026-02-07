#Write a program about remove the mid of element in given array.

#Method 1

# class Remove:
#     @staticmethod
#     def remove(n):
#         m = len(n)
#         if m % 2 == 0:
#             del n[(m//2)-1 : (m//2)+1]
           
#         else:
#             n.pop(m // 2)
        
#         return n
    
# n = list(map(int, input("Enter a number : ").split(",")))
# print(Remove.remove(n))


#Method 2

def array_handling(a):
    n=0
    if len(a)%2==0:
        for _ in range(1,len(a),2):      
            n+=1
        m=n-1
        del a[m:n+1]
    else:
        for _ in range(1,len(a),2):      
            n+=1
        del a[n]
    return a

n = list(map(int, input("Enter a number : ").split(","))) 
print(array_handling(n))




# for j in range(len(a)):
#     if j == n:
#         print(a[j])
#         n =-1
#     mid = j
# print(mid)

# a=[1,2,3,4,5]
# mid = len(a)//2
# a.pop(mid)
# print(a)