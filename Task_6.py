# Write a function that accepts a string with some “#” in it. Move all the hashes to the front of the string and return the modified string.

# def modify_string(a):
#   
#     hash_symbol = ""
#     for i in a:
#         if i == "#":
#             hash_symbol += i

#     b=a.split("#")
#     b.insert(0,hash_symbol)
#     c="".join(b)
#     return c

# a = input("Enter a sentence :")
# print(modify_string(a))


#Method 2

# def modify_string(a):
#     hash_symbol = a.count("#")
#     result = "#"*hash_symbol + a.replace("#","")
#     return result
# a = input("Enter a sentence :")
# print(modify_string(a))


#Method 3

# def modify_string(a):
#     hash_symbol = [x for x in a if x=="#"]
#     char = [x for x in a if x!="#"]
#     return "".join(hash_symbol+char)
 
# a = input("Enter a sentence :")
# print(modify_string(a))

#Method 4

def modify_string(a):
    b=list(a) 
    pos = 0
    for i in range(len(b)):
        if b[i] =="#":
            b[pos],b[i]=b[i],b[pos]
            pos +=1
    # result = b,key=lambda x: x != "#"
    result = "".join(b)
    return result

a = input("Enter a sentence :")
print(modify_string(a))

 



