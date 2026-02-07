
#Method 1

def perfect_square(n):
    if (n**0.5)**2 == n:
        return "perfect square"
    else:
        return "No"
a=int(input("Enter a number :"))
print(perfect_square(a))


#Method 2
def perfect_square(n):
  
    odd = 1
    while n > 0:
        n -= odd
        odd += 2
    if n == 0:
        return True

# x = int(input("Enter a number :"))
# if perfect_square(x):
#     print("Perfect Square")
# else:
#     print("No")
