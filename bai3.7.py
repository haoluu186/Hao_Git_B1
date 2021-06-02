#Cho trước chuỗi ký tự s bất kỳ, hãy thay thế các ký tự trong chuỗi s là chữ số thành
# ký tự $, và in ra chuỗi s mới.
import re
original_str = "213imic1technology456"
s1 = ""
#Cách 1: dùng regex để tìm số và thay thế
p = "[0-9]"
for i in range(0,len(original_str)):
    if re.search(p,original_str[i]) != None:
        s1 += '$'
    else:
        s1 += original_str[i]
print(s1)

#Cách 2: dùng hàm isdigit() để tìm số
s2 = ""
for i in range(0,len(original_str)):
    if original_str[i].isdigit():
        s2 += '$'
    else:
        s2 += original_str[i]
print(s2)
