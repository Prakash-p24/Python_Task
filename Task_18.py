#Input: [2,4,[3,5,[1,[9]]],0]
#Output: [2,4,3,5,1,9,0]
# a = [2,4,[3,5,[1,[9]]],0]
# result = []
# for i in str(a).split():
#     print(i)
#     # if isinstance(i,int):
#     #     result.append(i)
# print(result)

def flatten(a,result):
    for i in a:
        if type(i) == list:
            flatten(i,result)
        else:
            result.append(i)
    return result
print(flatten([2,4,[3,5,[1,[9]]],0],[]))

                      