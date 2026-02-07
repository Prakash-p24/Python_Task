#Write a function about Traverse a matrix in a spiral format.
#input:
#matrix = [[1,   2,   3,   4,  5,   6], [7,   8,   9,  10,  11,  12],  [13,  14,  15, 16,  17,  18]]
#output:
#[1,2,3,4,5,6,12,18,17,16,15,14,13,7,8,9,10,11]


# def traverse():
#     R = 3
#     matrix = [list(map(int, input("Enter a number : ").split())) for _ in range(R)]
#     spiral_matrix=[]
#     for i in matrix:


#     return matrix
# print(traverse())


#Method 1

# def spirallyTraverse(mat):
#     m, n = len(mat), len(mat[0])
#     print(m,n)

#     res = []
#     top, bottom, left, right = 0, m - 1, 0, n - 1


#     while top <= bottom and left <= right:


#         for i in range(left, right + 1):
#             res.append(mat[top][i])
#         top += 1
#         print(res,"1")


#         for i in range(top, bottom + 1):
#             res.append(mat[i][right])
#         right -= 1
#         print(res,"2")


#         if top <= bottom:
#             for i in range(right, left - 1, -1):
#                 res.append(mat[bottom][i])
#             bottom -= 1
#         print(res,"3")

#         if left <= right:
#             for i in range(bottom, top - 1, -1):
#                 res.append(mat[i][left])
#             left += 1
#         print(res,"4")

#     return res


# R = int(input("Enter a row:"))
# matrix = [list(map(int, input("Enter a number : ").split())) for _ in range(R)]
# res = spirallyTraverse(matrix)
# print(" ".join(map(str, res)))


#Method 2

#input:
#matrix = [[1,   2,   3,   4,  5,   6], [7,   8,   9,  10,  11,  12],  [13,  14,  15, 16,  17,  18]]
#output:
#[1,2,3,4,5,6,12,18,17,16,15,14,13,7,8,9,10,11]

# def spirallyTraverse(matrix):
#     result = []
#     while matrix:
#         result +=matrix.pop(0)
#         matrix = list(zip(*matrix))[::-1]
#     return result
# R = int(input("Enter a row:"))
# matrix = [list(map(int, input("Enter a number : ").split(","))) for _ in range(R)]
# print(spirallyTraverse(matrix))


#Method 3

#input:
#matrix = [[1,   2,   3,   4,  5,   6], [7,   8,   9,  10,  11,  12],  [13,  14,  15, 16,  17,  18]]
#output:
#[1,2,3,4,5,6,12,18,17,16,15,14,13,7,8,9,10,11]

def spiral_traverse_recursive(matrix):
    result = []
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    def recursive_helper(top, bottom, left, right):
        if top > bottom or left > right:
            return

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1


        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1


        recursive_helper(top, bottom, left, right)

    recursive_helper(0, rows - 1, 0, cols - 1)
    return result

R = int(input("Enter a row:"))
matrix = [list(map(int, input("Enter a number : ").split(","))) for _ in range(R)]
print(matrix)
# print(spiral_traverse_recursive(matrix))




