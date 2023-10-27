import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import *
import matplotlib.pyplot as plt
import datetime
from datetime import date
# from matplotlib.widgets import TextBox, Dropdown


mydb = mysql.connector.connect(
  host="localhost",
  user="lien",
  password="1234",
  #database="QLSinhVien"
  #database="QLBaiBao"
  database="QLQuanAo"
)

mycursor = mydb.cursor()
#=================================================================
# Các hàm dùng cho mysql
def ExecuteMultipleVal(strr:str, v):
  try:
    mycursor.executemany(strr, v)
    mydb.commit()
    print(mycursor.rowcount, "row was effected.")
    return True
  except mysql.connector.Error as err:
    print("Đã có lỗi xảy ra: {}".format(err))

def Execute(strr:str): # dùng để tạo ra bất kỳ thay đổi nào trên bảng
  mycursor.execute(strr)
  mydb.commit()
  print(mycursor.rowcount, "row was effected.")

def runSelect(strr:str): # dùng để hiển thị kết quả của dòng query
  mycursor.execute(strr)
  records = mycursor.fetchall()
  for row in records:
    print(row)
  print(mycursor.rowcount, "row was effected.")

def values_Of_Select(strr:str): #hàm này cho phép trả về dữ liệu các dòng của một câu query select
  result = []
  mycursor.execute(strr)
  records = mycursor.fetchall()
  for row in records:
    result.append(row)
  return result

def get_all_class():
  try:
    mycursor.execute("""select * from Lop""")
    records = mycursor.fetchall()

    for row in records:
      print("*"*50)
      print("Ma Lop", row[0])
      print("Ten Lop", row[1])

  except mysql.connector.Error as err:
    print("Đã có lỗi xảy ra: {}".format(err))

#Quản lý quần áo
#Insert vào bảng quần áo
sqlInsertMatHang = """INSERT INTO QuanAo (TenMatHang, GiaMatHang, LoaiQuanAo) VALUES (%s,%s,%s)"""
cacMatHang = [
    ("Áo Thun T-Shirt Nam","120000","1"),
    ("Áo Khoác Bomber Nam","365000","1"),
    ("Quần Jeans Nam", "250000","2"),
    ("Áo Sơ Mi Nữ", "180000","1"),
    ("Áo Polo Nam", "150000","1"),
    ("Áo Len Nữ", "220000","1"),
    ("Quần Kaki Nam", "190000","2"),
    ("Áo Hoodie Nữ", "280000","1"),
    ("Áo Thun Crop Top Nữ", "120000","1"),
    ("Áo Polo Nam", "170000","1"),
    ("Quần Jogger Nam", "200000","2"),
    ("Quần Legging Nữ", "150000","2"),
    ("Quần Khaki Nữ", "180000","2"),
    ("Quần Short Nam", "120000","2"),
    ("Quần Jean Nữ", "250000","2"),
    ("Váy Đầm Bodycon Nữ", "320000","2"),
]


sqlInsertHoaDonCoDinh = """INSERT INTO HoaDon (TenHoaDon, MaCacMatHang, NgayMua, TongGiaTriDonHang) VALUES (%s,%s,%s,%s)""" #Nhập cố định
sqlInsertHoaDon = """INSERT INTO HoaDon (TenHoaDon, MaCacMatHang, NgayMua, TongGiaTriDonHang) VALUES (%s, %s, %s, %s""" #Lấy ngày hôm nay
    # ("Áo Thun T-Shirt Nam, Quần Jogger Nam, Quần Short Nam","1;11;14", "2022-09-19","2;1;1","440000"),

cacHoaDon = [
    ("Áo Thun T-Shirt Nam, Quần Jogger Nam, Quần Short Nam","1;11;14", "2021-09-19","440000"),
    ("Áo Khoác Bomber Nam, Quần Jeans Nam, Quần Legging Nữ", "2;5;6", "2022-10-03", "680000"),
    ("Áo Sơ Mi Nữ, Áo Len Nữ, Quần Đùi Nam", "3;7;13", "2022-11-15", "530000"),
    ("Áo Polo Nam, Áo Hoodie Nữ, Quần Khaki Nữ", "4;8;9", "2022-12-08", "590000"),
    ("Áo Thun Crop Top Nữ, Quần Baggy Nữ, Quần Tây Nam", "10;12;15", "2023-01-21", "630000"),
    ("Áo Thun T-Shirt Nam, Quần Short Nam, Quần Linen Nam", "1;14;8", "2023-02-09", "470000"),
    ("Áo Thun Crop Top Nữ, Quần Culottes Nữ, Quần Kaki Nam", "10;7;13", "2023-03-05", "600000"),
    ("Áo Polo Nam, Áo Hoodie Nữ, Quần Baggy Nữ", "4;8;12", "2023-04-12", "710000"),
    ("Áo Sơ Mi Nữ, Áo Len Nữ, Quần Jean Nữ", "3;6;5", "2023-05-18", "620000"),
    ("Áo Khoác Bomber Nam, Quần Jogger Nam, Quần Short Nam", "2;1;14", "2023-06-23", "670000"),
    ("Áo Thun T-Shirt Nam, Áo Polo Nam, Quần Linen Nam", "1;4;8", "2023-07-30", "530000"),
    ("Áo Thun Crop Top Nữ, Quần Culottes Nữ, Quần Kaki Nam", "10;7;13", "2023-08-05", "600000"),
    ("Áo Polo Nam, Áo Hoodie Nữ, Quần Baggy Nữ", "4;8;12", "2023-09-12", "710000"),
    ("Áo Sơ Mi Nữ, Áo Len Nữ, Quần Jean Nữ", "3;6;5", "2023-10-18", "620000"),
    ("Áo Khoác Bomber Nam, Quần Jogger Nam, Quần Short Nam", "2;1;14", "2023-04-23", "670000")
]

hda = [
   ("Áo Thun T-Shirt Nam, Quần Jogger Nam, Quần Short Nam","1;11;14", "2022-09-19","440000"),
    ("Áo Khoác Bomber Nam, Quần Jeans Nam, Quần Legging Nữ", "2;5;6", "2022-10-03", "680000"),
    ("Áo Sơ Mi Nữ, Áo Len Nữ, Quần Đùi Nam", "3;7;13", "2022-11-15", "530000"),
    ("Áo Polo Nam, Áo Hoodie Nữ, Quần Khaki Nữ", "4;8;9", "2022-12-08", "590000"),
    ("Áo Thun Crop Top Nữ, Quần Baggy Nữ, Quần Tây Nam", "10;12;15", "2022-01-21", "630000"),
    ("Áo Thun T-Shirt Nam, Quần Short Nam, Quần Linen Nam", "1;14;8", "2022-02-09", "470000"),
    ("Áo Thun Crop Top Nữ, Quần Culottes Nữ, Quần Kaki Nam", "10;7;13", "2022-03-05", "600000"),
    ("Áo Polo Nam, Áo Hoodie Nữ, Quần Baggy Nữ", "4;8;12", "2022-04-12", "710000"),
    ("Áo Sơ Mi Nữ, Áo Len Nữ, Quần Jean Nữ", "3;6;5", "2022-05-18", "620000"),
    ("Áo Khoác Bomber Nam, Quần Jogger Nam, Quần Short Nam", "2;1;14", "2023-06-23", "670000"),
]
# ExecuteMultipleVal(sqlInsertHoaDonCoDinh, hda)



# Tạo bảng cho db quần áo
# Execute("""CREATE TABLE HoaDon (
#     MaHoaDon INT AUTO_INCREMENT PRIMARY KEY,
#     TenHoaDon VARCHAR(255),
#     MaCacMatHang VARCHAR(255),
#     NgayMua DATE,
#     TongGiaTriDonHang INT)""")

# Execute("""CREATE TABLE QuanAo (
#     MaQuanAo INT AUTO_INCREMENT PRIMARY KEY,
#     TenMatHang VARCHAR(255) NOT NULL,
#     GiaMatHang INT NOT NULL,
#     LoaiQuanAo VARCHAR(5) NOT NULL
# )""")

#==========================================================
# THỰC THI LỆNH SQL TẠI ĐÂY





#=================================================================================
#giao diện tkinter
#=======================================================================
#Cửa sổ hóa đơn:
def khoi_tao_Cua_so_hoa_don():
    winHoadon = tk.Toplevel(root)
    winHoadon.title("Xem danh sách hóa đơn")
    winHoadon.geometry("1200x600")

    search_boxhd = tk.Entry(winHoadon, width=30, textvariable=var)
    search_boxhd.pack()

    columns = ("Mã hóa đơn", "Tên", "Mã các đơn hàng", "Ngày mua","Tổng thanh toán")
    global treev
    treev = ttk.Treeview(winHoadon, columns=columns, show="headings")
    for col in columns:
        treev.heading(col, text=col)
        treev.column(col, width=200)
    treev.pack()
    XuatDanhSachHoaDon()

def XuatDanhSachHoaDon():
    sql = "SELECT * FROM HoaDon"
    try:
        for row in values_Of_Select(sql):
            treev.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))
    except mysql.connector.Error as err:
        print("" + err)

def Tim_Kiem_Mat_HangHD(strr:str):
    # Xoá dữ liệu hiện tại trong treeview
    for row in treev.get_children():
        treev.delete(row)
    sql = f"SELECT * FROM HoaDon Where TenMatHang like '%{strr}%'"
    try:
        for row in values_Of_Select(sql):
            treev.insert("", "end", values=(row[0], row[1], row[2], row[3],row[4]))
    except mysql.connector.Error as err:
        print("" + err)

#=================================================================
#cửa sổ chính
def XuatMatHang():
    sql = "SELECT * FROM QuanAo"
    try:
        for row in values_Of_Select(sql):
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
    except mysql.connector.Error as err:
        print("" + err)

# def XuatMatHangOnChange():
#     sql = f"SELECT * FROM QuanAo"
#     try:
#         for row in values_Of_Select(sql):
#             tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
#     except mysql.connector.Error as err:
#         print("" + err)

#Xử lý tìm kiếm nếu search_box thay đổi
def Tim_Kiem_Mat_Hang(content:str, _table:str):
    # Xoá dữ liệu hiện tại trong treeview
    for row in tree.get_children():
        tree.delete(row)
    sql = f"SELECT * FROM {_table} Where TenMatHang like '%{content}%'"
    try:
        for row in values_Of_Select(sql):
            tree.insert("", "end", values=(row[0], row[1], row[2], row[3]))
    except mysql.connector.Error as err:
        print("" + err)





#Xử lý nút add to Cart
def Add_To_Cart():
    curItems = tree.selection()
    for item in curItems:
      m = tree.item(item)['values'][0]
      t = tree.item(item)['values'][1]
      g = tree.item(item)['values'][2]
      newCart.insert("", END, values=(m,t,g))

def Them_vao_hoa_don():
  values = []
  tenHD = ""
  macacdonhang = ""
  tongGiaTriDonHang = 0
  ngay_hien_tai = str(date.today())

  for row in newCart.get_children():
    # tple = ()
    
    macacdonhang += f"""{newCart.item(row)['values'][0]};"""
    tenHD += f"""{newCart.item(row)['values'][1]},"""
    tongGiaTriDonHang += newCart.item(row)['values'][2]
    # print(tree.item(row)['values'][1])
  tple = (tenHD, macacdonhang, ngay_hien_tai, tongGiaTriDonHang)
  values.append(tple)
  print(str(values))
  if ExecuteMultipleVal(sqlInsertHoaDonCoDinh, values):
     print('Đơn hàng đã được thêm vào Bảng hóa đơn')






# def Them_vao_hoa_don():
#   values = []
#   for row in newCart.get_children():
#     tongGiaTriDonHang = 0
#     # tple = ()
#     tenHD = ""
#     macacdonhang = ""
#     macacdonhang += f"""{tree.item(row)['values'][0]}"""
#     tenHD += f"""{tree.item(row)['values'][1]},"""
#     tongGiaTriDonHang += tree.item(row)['values'][2]
#     # print(tree.item(row)['values'][1])
#     tple = (tenHD, macacdonhang, tongGiaTriDonHang)
#     print(tple)
#     values.append(tple)
#   print(values)
#   # ExecuteMultipleVal(sqlInsertHoaDon, values)



# Tạo cửa sổ chính
root = tk.Tk()
root.title("Quản lý Hàng hóa - Hóa đơn - 2116976 - Bùi Minh Liên")
root.geometry("1280x720")

# Tạo và thiết lập các widget





def callback(var):
   content= var.get()
   Tim_Kiem_Mat_Hang(content, "QuanAo")
#Create an variable to store the user-input
var = StringVar()
var.trace("w", lambda name, index,mode, var=var: callback(var))

Label(text="Tìm kiếm").pack()

search_box = tk.Entry(root, width=30, textvariable=var)
search_box.pack()


# Tạo treeview
columns = ("Mã Hàng", "Tên", "Giá", "Loại")
tree = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=250)
tree.pack()
XuatMatHang()
#=============================
#tree.insert("", "end", values=(maQuanAo, ten, gia, loai))
#nút thêm vào cart
btnThem = tk.Button(root, text="Thêm vào giỏ", command=Add_To_Cart)
btnThem.pack()

btn_XemHD = tk.Button(root, text="Xem Hóa Đơn", command=khoi_tao_Cua_so_hoa_don)
btn_XemHD.pack()




#==============================================================R
# thống kê
def Show_Bieu_Do(namw):
  thang = ['Tháng 1', 'Tháng 2', 'Tháng 3', 'Tháng 4', 'Tháng 5', 'Tháng 6', 'Tháng 7', 'Tháng 8', 'Tháng 9', 'Tháng 10', 'Tháng 11', 'Tháng 12']
  #========================================
  def Xuat_bieu_do_theo_nam(year):
    doanh_thu_sql = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for row in values_Of_Select(f"select * from HoaDon where YEAR(NgayMua) = {year}"):
      thang_cua_hd = int(str(row[3]).split('-')[1]) #lấy tháng và bỏ số 0 ở đầu tháng có 1 chữ số bằng cách ép kiểu int
      #  ['2022', '09', '19']
      doanh_thu_sql[thang_cua_hd - 1] =  doanh_thu_sql[thang_cua_hd - 1] + int(row[4])
    print("Tháng có doanh thu cao nhất là tháng ", doanh_thu_sql.index(max(doanh_thu_sql)) + 1) #Tìm tháng có doanh thu cao nhất hiển thị vào terminal

    # Vẽ biểu đồ
    plt.figure(figsize=(10, 6))
    plt.bar(thang, doanh_thu_sql, color='#1C6EEC')
    plt.xlabel('Tháng')
    plt.ylabel('Doanh thu (VND)')
    plt.title(f'Biểu đồ thể hiện doanh thu năm {year}')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Hiển thị biểu đồ
    plt.show()
  Xuat_bieu_do_theo_nam(namw)

Label(text="Xem thống kê").pack()

def on_field_change(index, value, op):
    namThongKe = cbNam.get()
    print(namThongKe)
    Show_Bieu_Do(namThongKe)
v = StringVar()
v.trace('w',on_field_change)

cbNam = ttk.Combobox(root, textvar=v)
cbNam.pack()
cbNam['values'] = ( '2023',  
                    '2022', 
                    '2021', 
                    '2020')
# Khởi chạy ứng dụng

#NEW CART
#=============================================================================================
#functions
def Xoa_Trong_Gio():
  x = newCart.selection()
  for record in x:
    newCart.delete(record)
#========================================================
label = tk.Label(root, text="Cart:")
label.pack()
columns = ["Mã hàng", "Tên", "Giá"]
newCart = ttk.Treeview(root, columns=columns, show="headings")
for col in columns:
    newCart.heading(col, text=col)
    newCart.column(col, width=150)
    if col == "Tên":
      newCart.column(col, width=350)
      
newCart.pack()
btn_delete_inside_cart = Button(text="Xóa trong giỏ", command=Xoa_Trong_Gio)
btn_delete_inside_cart.pack()
btn_thanh_toan = Button(text="Thanh toán", command=Them_vao_hoa_don)
btn_thanh_toan.pack()

root.mainloop()



#Just writting some comment 