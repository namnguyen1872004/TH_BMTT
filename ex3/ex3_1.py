def tinh_tong_chan(lst):
    tong=0
    for num in lst:
        if num%2==0:
            tong+=num
    return tong

input_list=input("Nhap danh sach cac so ")
numbers=list(map(int, input_list.split(',')))
tong_chan=tinh_tong_chan(numbers)
print("tong cac so chan ",tong_chan)