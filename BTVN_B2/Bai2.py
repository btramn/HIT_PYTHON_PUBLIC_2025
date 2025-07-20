def tinh_thue_va_luong_rong(luong):
    if luong >= 15000000:
        thue = 0.3 * luong
    elif luong >= 7000000:
        thue = 0.2 * luong
    else:
        thue = 0.1 * luong
    luong_rong = luong - thue
    return f"Thuế: {int(thue)} Thu nhập: {int(luong_rong)}"

#Test
print(tinh_thue_va_luong_rong(5000000))  
