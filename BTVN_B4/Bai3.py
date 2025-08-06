# Đầu vào mẫu
n, m = 5, 3
a = [1, 5, 3, 2, 6]
A = {1, 2, 3}
B = {4, 5, 6}

muc_do_hp = 0
for x in a:
    if x in A:
        muc_do_hp += 1
    elif x in B:
        muc_do_hp -= 1

print("Mức độ hạnh phúc:", muc_do_hp)
