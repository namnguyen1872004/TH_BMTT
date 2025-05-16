def tao_taple(lst):
    return tuple(lst)
input_list=input("Nh1,-2,3,4,5,-6,7,8,-9ap danh sach cac so ")
numbers=list(map(int, input_list.split(',')))
my_taple=tao_taple(numbers)
print("List: ",numbers)
print("Tumple tu List ", my_taple)
