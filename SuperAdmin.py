from base.base import base
from Mahasiswa import Mahasiswa
from Dosen import Dosen


class SuperAdmin(base):
    def __init__(self, user_nim, name, email, password):
        super().__init__(user_nim, name, email, password)
        self.user_nim = user_nim
        self.user_password = password
        self.Mahasiswa_schedule = []

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
        
    def class_schedule(self, Mahasiswa):
        self.Mahasiswa_schedule.append(Mahasiswa)
    
    