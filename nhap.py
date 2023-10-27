class SinhVien:
    def __init__(self, maso, hoten):
        self.maso = maso
        self.hoten= hoten
    def __str__(self):
        return f'sinh viên có mã số: {self.maso} họ tên: {self.hoten}'

class DanhSachSinhVien:
    def __init__(self):
        self.ds = []
    
    def them_sinh_vien(self, sv: SinhVien):
        self.ds.append(sv)

    def XuatAll(self):
        for sv in self.ds:
            print(sv)

danhsach = DanhSachSinhVien()
sv1 = SinhVien('2116976', 'Bùi Minh Liên')
sv2 = SinhVien('2116900', 'Trần Đoàn Trúc Như')
sv3 = SinhVien('2116901', 'Nguyễn Thị Trà My')

danhsach.them_sinh_vien(sv1)
danhsach.them_sinh_vien(sv2)
danhsach.them_sinh_vien(sv3)

danhsach.XuatAll()