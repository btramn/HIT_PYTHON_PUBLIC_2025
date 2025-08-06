A = {"SV01", "SV02", "SV03", "SV05"}
B = {"SV03", "SV04", "SV06"}

print("Bàn 1:", A)
print("Bàn 2:", B)

hai_ban = A.intersection(B)
print("Sinh viên đăng ký cả 2 bàn:", hai_ban)

both = A.union(B)
print("Danh sách tổng hợp sinh viên:", both)

A = A.difference(B)
print("Sinh viên chỉ đăng ký tại bàn 1:", A)

