

class grades:
    def __init__(self, course_name, mahasiswa):
        self.course_name = course_name
        self.grades = []
    
    def upload_grade(self, mahasiswa, grade):
        if mahasiswa in self.grades:
            print("Nilai untuk mahasiswa ini sudah diunggah sebelumnya.")
        else:
            self.grades[mahasiswa] = grade
            print("Nilai berhasil diunggah.")

    def view_grades(self, mahasiswa):
        if mahasiswa in self.grades:
            print("Grades: ")
            return self.grades[mahasiswa]
        else: 
            return "Nilai Mahasiswa ini Belum di Unggah"
    