#Write a code for the given str is print palindrome or not


#Method 1

# def palindrome_one(a):
#     palindrome = ""
#     for i in a:
#         palindrome = i + palindrome
#     if palindrome == a:
#         return "The given sentence is palindrome"
#     else:
#         return "The given sentence is not palindrome"

# a = input("Enter a Sentence :")
# print(palindrome_one(a))


#Method 2

# def palindrome_two(a):

#     palindrome = False
#     for i in range(len(a)):
#         if a[i] != a[len(a)-i-1]:
#             break
#         else:
#             palindrome = True
#     if palindrome:
#         return "The given sentence is palindrome"
#     else:
#         return "The given sentence is not palindrome"

# a = input("Enter a Sentence :")
# print(palindrome_two(a))

def is_palindrome(s):
    if len(s) < 2:
        return True
    
    if s[0] != s[-1]:
        return False

    return is_palindrome(s[1:-1])

a = input("Enter a Sentence :")
if is_palindrome(a):
    print("The given sentence is palindrome")
else:
    print("The given sentence is not palindrome")

#Method 3

# def palindrome_three(a):
#     start = 0
#     end = len(a)-1
#     while end > start:
#         if a[start] != a[end]:
#             return "The given sentence is not palindrome"
#         start +=1
#         end -=1
#     else:
#         return "The given sentence is palindrome"


# a = input("Enter a Sentence :")
# print(palindrome_three(a))


