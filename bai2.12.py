#Dãy số a được gọi là dãy con của b nếu từ b xóa đi một vài phần tử sẽ thu được a.
#Cho trước 2 dãy số nguyên a,b. Hãy kiểm tra xem a có là dãy con của b hay không?

ds_a = [1,5]
ds_b = [1,2,5,7]

for so in ds_b:
    if so not in ds_a:
        ds_b.remove(so) #xóa tất cả những phần tử có ở ds_b nhưng không có ở ds_a

ds_a.sort()
ds_b.sort()
if ds_a == ds_b:
    print(ds_a, "la con cua", ds_b)
else:
    print(ds_a, "không la con cua", ds_b)
