def chia_het_cho_5(so_nhi_phan):
    so_thap_phan=int(so_nhi_phan,2)
    if so_thap_phan%5==0:
        return True
    else:
        return False
chuoi_so_nhi_phan=input("Nhap chuoi so nhi phan ")
chuoi_so_nhi_phan_list=chuoi_so_nhi_phan.split(',')
so_chia_het_cho_5=[so for so in chuoi_so_nhi_phan_list if chia_het_cho_5(so)]
if len(so_chia_het_cho_5)>0:
    ket_qua =','.join(so_chia_het_cho_5)
    print("So chia het cho 5 ",ket_qua)
else:
    print("Khong co so nhi phan nao chia het cho 5")
        
    