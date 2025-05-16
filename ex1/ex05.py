so_gio_lam=float(input("Nhap so gio lam "))
luong_gio=float(input("Nhap so luong theo gio "))
gio_tieu_chuan=44
gio_lam_them=max(0, so_gio_lam-gio_tieu_chuan)
thu_nhap=gio_tieu_chuan*luong_gio+gio_lam_them*luong_gio*1.5
print(f"So tien thu nhap cua nhan vien {thu_nhap}")