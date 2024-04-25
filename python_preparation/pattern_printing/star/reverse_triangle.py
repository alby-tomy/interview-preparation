# def reverse_tri_ptrn(n):
#     for i in range(n,0,-1):
#         for j in range(i):
#             print("*",end=' ')
#         print()
        
# reverse_tri_ptrn(5)

def print_inverted_triangle(rows):
    for i in range(rows, 0, -1):
        print('*' * i)

print_inverted_triangle(5)
