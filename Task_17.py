#Construct a one user defined function similar to inbuild range function

#Method 1

# def iterator(start,stop,step=1):
#     s=start
#     end=stop
#     while end > 0:
#         if step >= 2:
#             print((s + step)-1)
#             s=s+step
#             end = end - step
#         else:
#             print(s)
#             s=s+1
#             end=end-1
    
# iterator(0,50)

#Method 2

def my_numbers(n,step):
    num = step
    while num <= n:
        yield num -1
        num += step
a=my_numbers(20,1)
for i in a:
    print(i)






