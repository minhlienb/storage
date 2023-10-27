# Biểu thức lambda
#list comprehension
# syntax for 
# bài tập lab 1 cơ bản 
# hàm tìm ucln

# Cài đặt
    # Chỉ cài khi bị thiểu pip
# curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
# python get-pip.py

# pip install package==2.28.1

# for Python 3
# pip3 install package==2.28.1
# python3 -m pip install requests==2.28.1


# pip install pandas
# pip install matplotlib
# pip install numpy
# pip install openpyxl xlrd

# xóa gói, gỡ gói
# pip uninstall package_name



# Kiểm tra điều kiện đầu vào
# x = int(input("Nhập số cần tính giai thừa: "))
# def fact(x):
#     if x == 0:
#         return 1
#     return x * fact(x - 1)
# print (fact(x))



# x = 1
# def _d(x:int):
#     if x == 2:
#         return "Đúng"
#     return "Sai"
# print(_d(x))



# current_year = datetime.date.today().year
# current_month = datetime.date.today().month
# current_day = datetime.date.today().day
# datetime.strptime(date, "%d/%m/%Y")
    # def DocTuFile(self, tenFile):
    #     with open(tenFile, 'r', encoding='utf-8') as f:
    #         for hang in f:
    #             dl = hang.split('*')
    #             ms = int(dl[0])
    #             ht = dl[1]
    #             ns = datetime.strptime(dl[2], "%d/%m/%Y")
    #             sv = SinhVien(ms, ht, ns)
    #             self.themSinhVien(sv)

## căn lề
    #   print(f"{row[0]:<{9}}{row[1]:<{30}}{classes[int(row[2]) - 1]:<{10}}") # row[2]) -1 vì index mảng bắt đầu bằng 0





# lab 4 lab 04
# lab 6, lab 06 matplotlib bieu do


# Biểu đồ đường
# import matplotlib.pyplot as plt 

# def Show_Bieu_Do(namw):
#   thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
#   #========================================
#   def Xuat_bieu_do_theo_nam(year):
#     doanh_thu_sql = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     # for row in values_Of_Select(f"select * from HoaDon where YEAR(NgayMua) = {year}"):
#     #   thang_cua_hd = int(str(row[3]).split('-')[1]) #lấy tháng và bỏ số 0 ở đầu tháng có 1 chữ số bằng cách ép kiểu int
#     #   #  ['2022', '09', '19']
#     #   doanh_thu_sql[thang_cua_hd - 1] =  doanh_thu_sql[thang_cua_hd - 1] + int(row[4])
#     # print("Tháng có doanh thu cao nhất là tháng ", doanh_thu_sql.index(max(doanh_thu_sql)) + 1) #Tìm tháng có doanh thu cao nhất hiển thị vào terminal

#     # Vẽ biểu đồ
#     plt.figure(figsize=(10, 6))
#     plt.bar(thang, doanh_thu_sql, color='#1C6EEC')
#     plt.xlabel('Tháng')
#     plt.ylabel('Doanh thu (VND)')
#     plt.title(f'Biểu đồ thể hiện doanh thu năm {year}')
#     plt.xticks(rotation=45)
#     plt.tight_layout()

#     # Hiển thị biểu đồ
#     plt.show()
#   Xuat_bieu_do_theo_nam(namw)

# Show_Bieu_Do("2023")


# Biểu đồ tròn
# import matplotlib.pyplot as plt

# # Dữ liệu cho biểu đồ tròn (tổng các giá trị phải là 100%)
# labels = ['Táo', 'Kiwi', 'Chanh', 'Bưởi']
# sizes = [11, 52, 12, 25]  # Tổng các giá trị phải là 100%

# # Màu sắc cho từng phần trong biểu đồ tròn
# colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']

# # Tạo biểu đồ tròn
# plt.figure(figsize=(10, 5))
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)

# # Tiêu đề của biểu đồ
# plt.title("Biểu đồ tròn đơn giản")

# # Hiển thị biểu đồ
# plt.show()



# import pandas as pd

# # Đường dẫn đến file Excel (thay đổi đường dẫn tới file của bạn)
# excel_file_path = 'D:\\file.xlsx'

# # Đọc file Excel vào DataFrame
# data = pd.read_excel(excel_file_path, header=None)  # Không có header

# # Lấy tên sinh viên từ cột theo index hoặc theo tên cột
# # Đây là ví dụ lấy dữ liệu từ dòng đầu tiên và cột đầu tiên (index=0, column=0)
# ten_sinh_vien = data.at[0, 0]

# # In ra tên sinh viên
# print(ten_sinh_vien)

# Ma So	    Ho Ten	            Ngay Sinh
# 2116976	Bui Minh Lien	    19/09/2003
# 2110000	Hello bat ngo chua	27/10/2023

# import pandas as pd

# # Đường dẫn đến file Excel (thay đổi đường dẫn tới file của bạn)
# excel_file_path = 'D:\\file.xlsx'

# # Đọc file Excel vào DataFrame mà không sử dụng chỉ mục
# data = pd.read_excel(excel_file_path, header=None)

# # Lấy tên sinh viên từ dòng thứ 1 và cột thứ 2 của DataFrame (index=0, column=1)
# cot_2 = data.iloc[1:, 1]

# # In ra tất cả các giá trị từ cột thứ 2
# print(cot_2.iloc[0])







# lab 1, lab 01

# import math

# def Cau01(a, b):
#     sum = a + b
#     div = a/b   
#     mul = a**b
#     print("a + b = " + str(sum))
#     print("a/b = " + str(div))
#     print("a b = " + str(sum))


# def Cau02(a, b):
#     return a*b*2


# def is_prime(n):
#   for i in range(2,n):
#     if (n%i) == 0:
#       return False
#   return True

# def Cau03(start, end):
#    for i in range (start, end):
#       if is_prime == True: print(i)
#       else: 
#          continue



# def is_fibonacci(n):
#   if not isinstance(n, int) or n < 0:
#     return False

#   # Khởi tạo hai số Fibonacci đầu tiên.
#   a, b = 0, 1

#   # Lặp qua dãy số Fibonacci cho đến khi gặp n.
#   while b <= n:
#     a, b = b, a + b

#   # Nếu n bằng một trong hai số Fibonacci đầu tiên, thì nó là số Fibonacci.
#   if n == a or n == b:
#     return True

#   return False
    
# def tinh_Tong_Can_Bac_Hai(n):
#   sum = 0
#   for i in range(1, n):
#     sum += math.sqrt(i)
#   return sum

# def giai_phuong_trinh_bac_2(a,b,c):
#   delta = b**2 - 4*a*c
#   if delta < 0:
#     return "Phương trình vô nghiệm"
#   elif delta == 0:
#     return f"Phương trình có nghiệm kép = {-(b / (2 * a))}"
#   else:
#     x1 = (-(b) + math.sqrt(delta))/(2*a)
#     x2 = (-(b) - math.sqrt(delta))/(2*a)
#     return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
    
# def Cau09_Tinh_N_GT(n):
#     result = 1
#     for i in range(1,n + 1):
#         result *= i
#     return result

# def draw_custom_triangle(height):
#     for i in range(1, height + 1):
#         if i == 1 or i == height:
#             print('* ' * i)
#         else:
#             print('*  ' + ' ' * (2 * (i - 2)) + '*')

# def giay_qua_gio(seconds):
#    return f"{seconds // 3600}:{seconds %3600 // 60}:{seconds %3600 % 60}"

# def so_le_khong_chia_het_cho_5(list):
#   out = []
#   for item in list:
#     if not(item % 5 == 0) and item % 2 != 0:
#       out.append(item)
#   return out

# def so_le_khong_chia_het_cho_5(list):
#    for item in list:
#     if not(item % 5 == 0) and item % 2 != 0:
#       print(item)

# def Xuat_fib(list):
#   out = []
#   for item in list:
#     if is_fibonacci(item):
#       out.append(item)
#   return out

# def find_max_prime(list):
#   out = []
#   for item in list:
#     if is_prime(item):
#       out.append(item)
#   return max(out) #nếu không có số nguyên tố thì sao

# def find_max_prime_2(list):
#   out = filter(is_prime, list) 
#   return max(out) #nếu không có số nguyên tố thì sao




# ''''''''
# def find_min_fib(list):
#   out = []
#   for item in list:
#     if is_fibonacci(item):
#       out.append(item)
#   return min(out)


# def find_min_fib_2(list):
#   out = filter(is_fibonacci, list)
#   return min(out)

# ''''''''
# def tinh_trung_binh_so_le(list):
#   out = []
#   for item in list:
#     if item % 2 == 1:
#       out.append(item)
#   return sum(out) / len(out)


# def tinh_tich_so_le_khong_chia_het_cho_3(list):
#   out = []
#   for item in list:
#     if (item % 2 == 1) and not(item % 3 == 3):
#       out.append(item)
#   result = 1
#   for x in out:
#     result *= x
#   return result 

# def doi_cho_x_y(list, pos1, pos2):
#   x = list.pop(pos1)  
#   y = list.pop(pos2-1)
#   list.insert(pos1, y)
#   list.insert(pos2 , x)
#   return list

# def dao_mang(list):
#   list.reverse() 

# def xuat_cac_so_lon_thu_nhi(list):
#   sortedList = list
#   sortedList.sort()
#   return sortedList[-2]

# def dem_so_lan_xuat_hien(list, n):
#   out = []
#   for x in list:
#     if x == n:
#       out.append(x)
#   return len(out)



# def tinhTong(list):
#   return sum(list)
  











# tkinter
# import tkinter as tk

# # Tạo cửa sổ chính
# root = tk.Tk()
# root.title("Grid Example")

# # Tạo các nhãn và ô nhập liệu
# label1 = tk.Label(root, text="Nhãn 1:")
# label1.grid(row=0, column=0, padx=10, pady=10)  # Đặt nhãn 1 tại hàng 0, cột 0 với padding

# entry1 = tk.Entry(root)
# entry1.grid(row=0, column=1, padx=10, pady=10)  # Đặt ô nhập liệu tương ứng với nhãn 1

# label2 = tk.Label(root, text="Nhãn 2:")
# label2.grid(row=1, column=0, padx=10, pady=10)  # Đặt nhãn 2 tại hàng 1, cột 0 với padding

# entry2 = tk.Entry(root)
# entry2.grid(row=1, column=1, padx=10, pady=10)  # Đặt ô nhập liệu tương ứng với nhãn 2

# # Hàm xử lý sự kiện khi nhấn nút
# def on_button_click():
#     value1 = entry1.get()
#     value2 = entry2.get()
#     print("Giá trị từ ô nhập liệu 1:", value1)
#     print("Giá trị từ ô nhập liệu 2:", value2)

# # Tạo nút và gắn hàm xử lý sự kiện
# button = tk.Button(root, text="Hiển thị giá trị", command=on_button_click)
# button.grid(row=2, columnspan=2, pady=10)  # Đặt nút tại hàng 2, cột 0 và kết hợp 2 cột

# # Bắt đầu vòng lặp chính của ứng dụng
# root.mainloop()

# ghi excel, xuất excel
# import pandas as pd

# # Tạo DataFrame mẫu
# data = {
#     'Name': ['Alice', 'Bob', 'Charlie'],
#     'Age': [25, 30, 35],
#     'City': ['New York', 'London', 'Paris']
# }
# df = pd.DataFrame(data)

# # Ghi DataFrame vào file Excel
# df.to_excel('output.xlsx', index=False)  # Tham số index=False loại bỏ cột index khi ghi vào tệp tin Excel
# print("Dữ liệu đã được ghi vào file Excel.")


# pandas
# import pandas as pd
# pd.Series(calories)


# import pandas as pd

# # Reading the CSV file into a DataFrame
# data = pd.read_csv('file.csv')

# # Printing all data from the DataFrame
# print(data)




