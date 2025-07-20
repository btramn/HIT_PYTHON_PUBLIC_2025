def dem_va_tong_chu_so(n):
    n = str(n)
    so_chu_so = len(n)
    tong = sum(int(ch) for ch in n)
    return f"Số chữ số: {so_chu_so} Tổng chữ số: {tong}"

# Test
print(dem_va_tong_chu_so(54))  
