# 1
# 2 2
# 3 3 3
# 4 4 4 4

def print_triangle_pattern(n):
    for i in range(n):
        for j in range(i):
            print(i, end=" ")
        print()


print_triangle_pattern(5)
