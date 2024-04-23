from base.base import base 

class Mahasiswa(base):
    def __init__(self, user_nim, name, email, password):
        super().__init__(user_nim, name, email, password)
        self.schedules = []

    def view_schedule(self):
        if not self.schedules:
            print("Anda belum terdaftar pada kursus manapun.")
        else:
            print("Jadwal mata kuliah:")
            for course in self.schedules:
                print(f"{course.name}: {course.schedule}")

    def get_name(self):
        return self._name