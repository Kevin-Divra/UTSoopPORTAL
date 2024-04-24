from base.base import base
from Mahasiswa import Mahasiswa
from Dosen import Dosen


class SuperAdmin(base):
    def __init__(self, user_nim, name, email, password, list_book):
        super().__init__(user_nim, name, email, password)
        self.user_nim = user_nim
        self.user_password = password
        self.Mahasiswa_schedule = []
        self.add_book = []
        self.available_book = list_book

    def login(self, nim, password):
        if nim == self.user_nim and password == self.user_password:
            return True
        else:
            return False
    
        
    def create_user_account(self, user_type, *args):
        if user_type == "Mahasiswa":
            return Mahasiswa(*args)
        elif user_type == "Dosen":
            return Dosen(*args)
        elif user_type == "SuperAdmin":
            return SuperAdmin(*args)
    
    def Mahasiswa_billing(self, mahasiswa, billing):
        if isinstance(mahasiswa,  Mahasiswa):
            print(f"Tagihan sebesar {billing} berhasil diinputkan untuk {mahasiswa.get_name()}.")
        else:
            print("Gagal menginputkan tagihan. Objek yang diberikan bukan merupakan instance dari kelas Mahasiswa.")
    
    def proses_pembayaran(self, mahasiswa, billing):
        print(f"Admin memproses pembayaran dari mahasiswa {mahasiswa.get_name()} sebesar {billing}. Pembayaran berhasil diproses.")

    
    def upload_book(self, returnedBook):
        self.available_book.append(returnedBook)
        # self.add_book.append(library)
    
    def available(self):
        print("the books we have in our library ar as follows:")
        print("===============================================")
        for book in self.available_book:
            print(book)
    
    def lend_book(self, request):
        if request in self.available_book:
            print("The book you requested has now been borrowed")
            self.available_book.remove(request)
        else:
            print("sorry the book you have requested is currently not in library")
    
