# Given a string with multiple characters that are repeated consecutively, reduce the size of the string using mathematical logic. Replace consecutive repeated characters with the character followed by the count of repetitions.

# input = "aabbbbeeeeffggg"
# output = "a2b4e4f2g3"


# Method 1

# def string_handling(a):
#     dict = {}
#     for i in a:
#         if i in dict:
#             dict[i]+=1
#         else:
#             dict[i]=1
#     return dict
# a=input("Enter a sentence :")
# b=string_handling(a)
# res =[key + str(values) for key,values in b.items()]
# final = "".join(res)
# print(final)


# Method 2

# def string_handling(a):
    
#     char = ""
#     for ch in a:
#         if ch in char:
#             pass
#         else:
#             char+=str((ch+str(a.count(ch))))
#             print(char)
#     return(char)
        
            
# a=input("Enter a sentence :")
# print(string_handling(a))

# Method 2

def string_handling(a):
    string = []
    
    length = len(a)
    while length != 0:
        for ch in a:
            if str((ch+str(a.count(ch)))) in string:
              pass
            else:
              string.append(str((ch+str(a.count(ch)))))

        length =0
    result = "".join(string)
    return result
        
a=input("Enter a sentence :")
print(string_handling(a))


# Method 3

# def string_handling(s,result):
    
#     if s =="":
#       return result
#     ch = s[0]
#     if ch in result:
#        result[ch]+=1
#     else:
#        result[ch]=1
#     return string_handling(s[1:],result)
# a=input("Enter a sentence :")
# res=string_handling(a,{})
# final=[key + str(values) for key,values in res.items()]
# output = "".join(final)
# print(output)
