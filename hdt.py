# ##file Danh sach sinh vien

# from SinhVien import SinhVien
# from SinhVienChinhQuy import SinhVienChinhQuy
# from SinhVienPhiChinhQuy import SinhVienPhiChinhQuy
# import datetime

# class DanhSachSV:
#     def __init__(self) -> None:
#         self.dssv = []
        
#     def themSinhVien(self, sv: SinhVien):
#         self.dssv.append(sv)
        
#     def xuat(self):
#         for sv in self.dssv:
#             print(sv)
            
#     def timSVTheoMSSV(self, mssv: int):
#         return [sv for sv in self.dssv if sv.mssv == mssv]

#     def timVTSVTheoMSSV(self, mssv: int):
#         for i in range(len(self.dssv)):
#             if self.dssv[i].mssv == mssv:
#                 return i
#             else:
#                 return -1
    
#     def xoaSVTheoMSSV(self, maSo: int) -> bool:
#         vt = self.timVTSVTheoMSSV(maSo)
#         if vt != -1:
#             del self.dssv[vt]
#             return True
#         else:
#             return False
        
#     def timSVTheoTen(self, hoTen: str):
#         return [sv for sv in self.dssv if sv.hoTen == hoTen]
    
#     def timSVSinhTruocNgay(self, ngay: datetime):
#         return [sv for sv in self.dssv if sv.ngaySinh - ngay < 0]
    
#     def DocTuFile(self, tenFile):
#         with open(tenFile, 'r', encoding='utf-8') as f:
#             for hang in f:
#                 dl = hang.split('*')
#                 ms = int(dl[0])
#                 ht = dl[1]
#                 ns = datetime.strptime(dl[2], "%d/%m/%Y")
#                 sv = SinhVien(ms, ht, ns)
#                 self.themSinhVien(sv)
    
#     def SapXepTangTheoTen(self):
#         return self.dssv.sort(key = lambda x: x.__hoTen, reverse=False)
    
#     def SapXepGiamTheoTen(self):
#         return self.dssv.sort(key = lambda x: x.__hoTen, reverse=True)
    
#     def TimSinhVienTheoLoai(self, loai: str):
#         if loai == "chinhquy":
#             return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy)]
#         else:
#             return [sv for sv in self.dssv if isinstance(sv, SinhVienPhiChinhQuy)]
        
#     def TimSinhVien_DiemRL(self, diemRL):
#         # for sv in self.dssv:
#         #     if isinstance(sv, SinhVienChinhQuy) and sv.diemRL > diemRL:
#         #         print(sv)
#         return [sv for sv in self.dssv if isinstance(sv, SinhVienChinhQuy) and sv.diemRL > diemRL]
    
#     # def TimSinhVienTheo_ThoiGian(self, daySV: datetime):
#     #     # daySV = datetime.datetime.strptime(daySV, "%d/%m/%y")
#     #     for sv in self.dssv:
#     #         if isinstance (sv, SinhVienPhiChinhQuy):
#     #             if sv.__ngaySinh.year < daySV.datetime.year:
#     #                 print(sv)
#     #             elif sv.__ngaySinh.year == daySV.datetime.year:
#     #                 if sv.__ngaySinh.month < daySV.datetime.month:
#     #                     print(sv)
#     #                 elif sv.__ngaySinh.month == daySV.datetime.month:
#     #                     if sv.__ngaySinh.day < daySV.datetime.month:
#     #                         print(sv)
                    

# ds = DanhSachSV()
# # ds.DocTuFile('DSSV.txt')
# svcq1 = SinhVienChinhQuy(2111982, "Trương Công Định", datetime.datetime(2000, 8, 18), 79)
# svcq2 = SinhVienChinhQuy(2111983, "Đặng Thị Tuyết Mai", datetime.datetime(2001, 9, 11), 81)
# svpcq1 = SinhVienPhiChinhQuy(2110282, "Nguyễn Hải Đăng", datetime.datetime(1999, 8, 14), "Cao Đẳng", 5)
# sv1 = SinhVien(2116976, "Bùi Minh Liên", datetime.datetime(2003, 2, 15))
# ds.themSinhVien(sv1)
# ds.themSinhVien(svcq1)
# ds.themSinhVien(svcq2)
# ds.themSinhVien(svpcq1)
# ds.xuat()
# loai = str(input("Nhập loại muốn tìm = "))
# kq = ds.TimSinhVienTheoLoai(loai)
# for i in kq:
#     print(i)
# diemRL = int(input("Nhập điểm RL: "))
# kq2 = ds.TimSinhVien_DiemRL(diemRL)
# for a in kq2:
#     print(i)
    
# d1 = str(input("Nhập thời gian muốn tìm (day / month/ year): "))
# daySV = datetime.datetime.strptime(d1, "%d/%m/%y")
# ds.TimSinhVienTheo_ThoiGian(daySV)


# ## file sinhvien
# from datetime import datetime

# class SinhVien:
#     truong = "Đại học Đà Lạt"
#     def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime) -> None:
#         self.__maSo = maSo
#         self.__hoTen = hoTen
#         self.__ngaySinh = ngaySinh
        
#     @property
#     def maSo(self):
#         return self.__maSo
    
#     @maSo.setter
#     def maSo(self, maSo):
#         if self.laMaSoHopLe(maSo):
#             self.__maSo = maSo
            
#     @staticmethod
#     def laMaSoHopLe(maSo: int):
#         return len(str(maSo)) == 7
    
#     def __str__(self) -> str:
#         return f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}"
    
#     def xuat(self):
#         print(f"{self.__maSo}\t{self.__hoTen}\t{self.__ngaySinh}")
        



# #### file sinhvienchinhquy
# from datetime import datetime
# from  SinhVien import SinhVien
# import datetime

# class SinhVienChinhQuy(SinhVien):
#     def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, diemRL: int) -> None:
#         super().__init__(maSo, hoTen, ngaySinh) 
#         self.diemRL = diemRL
        
#     def __str__(self) -> str:
#         return super().__str__() + f"\t {self.diemRL}"


# ###file sinhvienphychinhquy
# from datetime import datetime
# from SinhVien import SinhVien
# import datetime

# class SinhVienPhiChinhQuy(SinhVien):
#     def __init__(self, maSo: int, hoTen: str, ngaySinh: datetime, trinhdo: str, tgdt: int) -> None:
#         super().__init__(maSo, hoTen, ngaySinh)
#         self.trinhdo = trinhdo
#         self.tgdt = tgdt
        
#     def __str__(self) -> str:
#         return super().__str__() + f"\t{self.trinhdo}\t{self.tgdt}"


