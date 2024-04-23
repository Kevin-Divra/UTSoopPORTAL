from base.base import base
from Mahasiswa import Mahasiswa

class admisi(base):
    def __init__(self, user_nim, name, email, password):
        super().__init__(user_nim, name, email, password)

    def Mahasiswa_billing(self, mahasiswa, billing):
        if isinstance(mahasiswa,  Mahasiswa):
            print(f"Tagihan sebesar {billing} berhasil diinputkan untuk {mahasiswa.get_name()}.")
        else:
            print("Gagal menginputkan tagihan. Objek yang diberikan bukan merupakan instance dari kelas Mahasiswa.")