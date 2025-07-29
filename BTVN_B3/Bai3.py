# 1
s1 = "python"
s2 = "HIT"

# 2
print("s1 đảo ngược:", s1[::-1])

# 3
a = 2
b = 6
if 1 <= a < b <= len(s2):
    s2_mới = s2[:a] + s2[a:b+1][::-1] + s2[b+1:]
    print("s2 đảo ngược:", s2_mới)
else:
    print("a, b không hợp lệ")

# 4
s3 = ''.join([s1[i] for i in range(len(s1)) if i % 2 != 0])
print("s3:", s3)

# 5
s4 = ''.join(s1[i] + s2[i] if i < len(s2) else s1[i] for i in range(len(s1))) + s2[len(s1):]
print("s4:", s4)
