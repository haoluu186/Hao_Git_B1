#Cho 1 dãy số tự nhiên, viết chương trình sắp xếp dãy số này theo thứ tự giảm dần.

def my_sort(ds):
    for i in range(0,len(ds)):
        for j in range(i+1 ,len(ds)):
            if ds[i] < ds[j]:
                a = ds[i]
                ds[i] = ds[j]
                ds[j] = a

    return ds

ds_sn = [7,3,5,8,2]
print(my_sort(ds_sn))


user_list = [10,100,14,4,3]
print(user_list)
user_list.sort(reverse=True)
print(user_list)
