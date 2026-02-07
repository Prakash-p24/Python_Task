#Write a code to get the count of vowels in given string

#Method 1
# class vowel_char:   
#     @staticmethod  
#     def count_vowel(s):
#         vowels = "aeiouAEIOU"
#         count = 0
#         for ch in s:
#             if ch in vowels:
#                 count +=1
#         return count

# word = input("Enter a sentence :") 
# print(vowel_char.count_vowel(word))

#Method 2

def count_vowel(s):
    values = [65,69,73,79,85,97,101,105,111,117]
    count = 0
    for ch in s:
        if ord(ch) in values:
            count += 1

    return count
word = input("Enter a sentence :") 
print(count_vowel(word))

