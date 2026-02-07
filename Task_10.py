
#Method 1
#C:\\Users\\Mitrahsoft35\\Downloads\\

try:
    with open ("C:\\Users\\Mitrahsoft35\\Downloads\\UI_design4.txt") as f:
        a=f.readlines()
        print(a)
except Exception as e:
    print("Error is :",e)

else:
    rev = " "
    for i in a:
        word = i[::-1]
        rev = rev + "\n"+ word 
    print(rev)


#Method 2
# try:
#     with open ("C:\\Users\\Mitrahsoft35\\Downloads\\UI_design4.txt") as f:
#         a=f.readlines()
#         print(a)
       
# except Exception as e:
#     print("Error is :",e)

# else:
#     def file_handling(a,i):
#         m = i
#         if len(a) == m:
#             pass
#         else:
#           word=a[i]
#           print(word[::-1])
#           file_handling(a,i+1)
# file_handling(a,0)
