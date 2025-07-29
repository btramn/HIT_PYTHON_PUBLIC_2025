
# 1. Nhập vào một list
N = 8
list1 = [3, 7, 2, 2, 5, 7, 9, 2]
print(list1)

# 2. Nhập một số X từ bàn phím, kiểm tra số lần X xuất hiện trong list.
X = 2
print(f"Số lần {X} xuất hiện:", list1.count(X))

# 3. Thay thế phần tử từ vị trí 2 -> 7
list1[2:8] = [8, 5, 4, 0, 1, 3]
print("List sau thay thế:", list1)

# 4. Tìm max và min
print("Giá trị lớn nhất:", max(list1))
print("Giá trị nhỏ nhất:", min(list1))

# 5. Chèn Y vào đầu
Y = 6
list1.insert(0, Y)
print("List sau khi chèn Y:", list1)

# 6. Kiểm tra sắp xếp
if list1 == sorted(list1):
    print("TĂNG")
elif list1 == sorted(list1, reverse=True):
    print("GIẢM")
else:
    print("NO")
