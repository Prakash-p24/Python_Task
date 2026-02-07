#Method 1

# def odd_even(n):
#     odd = [i for i in range(1,n+1) if i % 2 !=0]
#     even = [i for i in range(1,n+1) if i % 2 ==0]
#     # for i in range(1,n+1):
#     #     if i % 2 ==0:
#     #         even.append(i)
#     #     else:
#     #         odd.append(i)
#     print("Odd numbers :",odd)
#     print("Even numbers :",even)

# n = int(input("Enter a number :"))
# odd_even(n)


#Method 2

# def odd_even_two(n):
#     odd = [i for i in range(1,n+1) if (i // 2) *2 != i]
#     even = [i for i in range(1,n+1) if (i // 2) *2 == i]
#     # for i in range(1,n+1):
#     #     if (i // 2) * 2 == i:
#     #         even.append(i)
#     #     else :
#     #         odd.append(i)
#     print("Odd numbers :",odd)
#     print("Even numbers :",even)

# n = int(input("Enter a number :"))
# odd_even_two(n)


#Method 3

def odd_even_three(n):
    even = []
    odd = []
    for i in range(2,n+1,2):
        even.append(i)
    for j in range(1,n+1,2):
        odd.append(j)

    print("Odd numbers :",odd)
    print("Even numbers :",even)

n = int(input("Enter a number :"))
odd_even_three(n)

