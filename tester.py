from SuperAdmin import SuperAdmin
from Mahasiswa import Mahasiswa
from admisi import admisi
from Dosen import Dosen
import sys

def main():
    admin = SuperAdmin("422023023", "kevin", "kevin@gmail.com", "uts", ["The Last Battle", "The Screwtape", "The Great Divorce"])


    nim_input = input("Masukkan NIM: ")
    password_input = input("Masukkan Password: ")

    print("\n")

    if admin.login(nim_input, password_input):
        print("Login Berhasil")

        print("\n")
            


        mahasiswa = admin.create_user_account("Mahasiswa", "422023023", "Kevin", "Kvin@example.com", "password123")
        dosen = admin.create_user_account("Dosen" "422023023", "John Doe", "john@example.com", "password123") 
        dosen = Dosen("422023023", "John Doe", "john@example.com", "password123")

        mahasiswa.view_schedule()

        print("\n")

        dosen.tambah_nilai(mahasiswa, "Pemrograman Web Lanjutan", 85)
        dosen.tambah_nilai(mahasiswa, "Analisa dan Perancangan Proses Bisnis", 90)
        dosen.tambah_nilai(mahasiswa, "Analisa & Perencanaan SI", 78)
        dosen.tambah_nilai(mahasiswa, "Manajemen SI", 85)
        dosen.tambah_nilai(mahasiswa, "Pemrograman Berorientasi Objek", 90)

        print("\n")

        mahasiswa.view_grade()

        print("\n")
        
        for user in [admin]:
            if user:
                admin.Mahasiswa_billing(mahasiswa, 500000)
        
        mahasiswa.upload_bukti_pembayaran(admin, 500000)

        print("\n")

        mahasiswa.upload_soft_skill("Leadership")
        mahasiswa.upload_soft_skill("Communication")
        mahasiswa.upload_soft_skill("Teamwork")

        print("\n")

        print("Daftar soft skill yang diunggah:")
        for skill in mahasiswa.soft_skills:
            print(skill)

        print("\n")

        mahasiswa.absen("Pemrograman Web Lanjutan", "2024-04-05")
        mahasiswa.absen("Analisa dan Perancangan Proses Bisnis", "2024-04-02")
        mahasiswa.absen("Analisa & Perencanaan SI", "2024-04-03")
        mahasiswa.absen("Manajemen SI", "2024-04-03")
        mahasiswa.absen("Pemrograman Berorientasi Objek", "2024-04-04")

        print("\n")

        print("Data absensi:")
        for course, dates in mahasiswa.attendance.items():
            print(f"Mata kuliah: {course}")
            print("Tanggal absen:", ", ".join(dates))
            print()
        
        print("\n")


        print("E-library")

        done = False
        while not done:
            print("""===========LIBRARY MENU============
            1. Display all available books
            2. Request a book
            3. Return a book
            4. Exit
           """)
            choice = int(input("Enter Choice: "))
            if choice == 1:
                admin.available()
            elif choice == 2:
                book_requested = input("Enter the name of the book you want to request: ")
                admin.lend_book(book_requested)
            elif choice == 3:
                book_returned = input("Enter the name of the book you want to return: ")
                admin.upload_book(book_returned)
            elif choice == 4:
                sys.exit()
            else:
                print("Invalid choice. Please try again.")

    else:
        print("Login Gagal")

if __name__ == "__main__":
    main()


