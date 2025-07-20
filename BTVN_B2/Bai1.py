def so_ngay_trong_thang(thang, nam):
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif thang in [4, 6, 9, 11]:
        return 30
    elif thang == 2:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            return 29
        else:
            return 28
        
#Test 
print(so_ngay_trong_thang(10, 2020))  
print(so_ngay_trong_thang(2, 2024))   
print(so_ngay_trong_thang(2, 2025))   
print(so_ngay_trong_thang(11, 1921))  
