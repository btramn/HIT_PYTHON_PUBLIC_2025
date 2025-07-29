# 1
k = 12
a = [1, 3, 5, 7, 2, 4, 6, 8, 9, 0, 11, 13]
n = 3
m = 4

# 2
if n * m > k:
    print("NO")
else:
    matrix = [a[i*m:(i+1)*m] for i in range(n)]
    print("Ma trận thu được:")
    for row in matrix:
        print(row)
