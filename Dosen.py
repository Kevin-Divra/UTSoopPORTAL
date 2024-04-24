from base.base import base
from Mahasiswa import Mahasiswa

class Dosen(base):
    def __init__(self, user_nim, name, email, password):
        super().__init__(user_nim, name, email, password)
    
    def tambah_nilai(self, mahasiswa, course, nilai):
        if isinstance(mahasiswa, Mahasiswa):
            mahasiswa.grades[course] = nilai
            print(f"Nilai untuk mahasiswa {mahasiswa.get_name()} pada mata kuliah '{course}' berhasil ditambahkan.")
        else:
            print("Gagal menambahkan nilai. Objek yang diberikan bukan merupakan instance dari kelas Mahasiswa.")
