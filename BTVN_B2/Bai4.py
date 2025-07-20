def tinh_so_chai_bia(n_xu):
    gia = 28
    chai_mua = n_xu // gia
    vo = chai_mua
    tong = chai_mua

    while vo >= 3:
        doi_duoc = vo // 3
        tong += doi_duoc
        vo = doi_duoc + (vo % 3)
    return f"Số chai bia có thể mua được là: {tong}"

# Test
print(tinh_so_chai_bia(28))  
