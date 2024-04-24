from base.base import base 

class Mahasiswa(base):
    def __init__(self, user_nim, name, email, password):
        super().__init__(user_nim, name, email, password)
        self.soft_skills = []
        self.attendance = {}
        self.grades = {}
        self.book = []
        self.schedules = {
            "Senin ": ["Libur"],
            "Selasa 08:00 - 10:30": ["Analisa dan Perancangan Proses Bisnis"],
            "Rabu 09:00 - 15:10": ["Analisa & Perencanaan SI", "Manajemen SI"],
            "Kamis 08:00 - 11:20": ["Pemrograman Berorientasi Objek"],
            "Jumat 08:00 - 13:15": ["Pemrograman Web Lanjutan"]
        }
    
    def view_grade(self):
        print("Daftar Nilai:")
        for course, nilai in self.grades.items():
            print(f"Mata kuliah: {course}, Nilai: {nilai}")

    def upload_soft_skill(self, soft_skill):
        self.soft_skills.append(soft_skill)
        print(f"Soft skill '{soft_skill}' berhasil diunggah.")

    def view_schedule(self):
        if not self.schedules:
            print("Anda belum terdaftar pada kursus manapun.")
        else:
            print("Jadwal mata kuliah:")
            for hari, mata_kuliah in self.schedules.items():
                print(f"{hari}: {', '.join(mata_kuliah)}")
    
    def lihat_tagihan(self):
        print(f"Total tagihan Anda adalah: {self.billing}")

    def upload_bukti_pembayaran(self, admin, billing):
        admin.proses_pembayaran(self, billing)

    def absen(self, course, date):
        if course in self.attendance:
            self.attendance[course].append(date)
        else:
            self.attendance[course] = [date]
        print(f"Absensi untuk mata kuliah '{course}' pada tanggal {date} berhasil dicatat.")

    def request(self):
        print("Enter the name of the book")
        self.book = input()
        return self.book
    
    def return_book(self):
        print("Enter the name of the book you'd likr to return")
        self.book = input()
        return self.book


    def get_name(self):
        return self.name