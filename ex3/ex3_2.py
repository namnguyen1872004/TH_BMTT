def dao_nguoc(lst):
    return lst[::-1]
input_list=input("Nhap danh sach cac so ")
numbers=list(map(int, input_list.split(',')))
list_dao_nguoc=dao_nguoc(numbers)
print("List sau khi dao nguoc ",list_dao_nguoc)