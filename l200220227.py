from metaflow import FlowSpec, step

class kuliah_informatika(FlowSpec):
    """Alur yang mensimulasikan perjalanan kuliah."""

    def __init__(self):
        super().__init__()
        self.midterm_grade = None
        self.final_grade = None
        self.final_score = None

    @step
    def start(self):
        """Titik awal"""
        print("Membayar biaya kuliah yang mencakup seluruh semester "
              "untuk memastikan pengalaman kuliah yang lancar...")
        self.next(self.register)

    @step
    def register(self):
        """Langkah pendaftaran"""
        print("Mendaftar untuk kelas...")
        self.next(self.attend_classes)

    @step
    def attend_classes(self):
        """Langkah menghadiri kelas"""
        print("Menghadiri kelas dan berpartisipasi dalam berbagai kegiatan...")
        self.total_attend = 14
        self.presence = 0

        for i in range(1, self.total_attend + 1):
            attend = True  # Simulasi kehadiran
            if attend:
                self.presence += 1
            print(f"Hari {i}: {'Hadir' if attend else 'Tidak hadir'}")
        self.min_attend = int(0.75 * self.total_attend)
        if self.presence >= self.min_attend:
            print("Memenuhi persyaratan kehadiran")
        else:
            print("Tidak memenuhi persyaratan kehadiran")
            self.next(self.end)
        self.next(self.receive_grades)

    @step
    def receive_grades(self):
        """Langkah menerima nilai UTS dan UAS"""
        self.midterm_grade = 80  # Nilai UTS
        self.final_grade = 90  # Nilai UAS
        print(f"Nilai UTS: {self.midterm_grade}")
        print(f"Nilai UAS: {self.final_grade}")
        self.next(self.calculate_final_score)

    @step
    def calculate_final_score(self):
        """Menghitung nilai akhir berdasarkan UTS dan UAS"""
        self.final_score = (self.midterm_grade + self.final_grade) / 2
        print(f"Nilai akhir: {self.final_score}")
        self.next(self.end)

    @step
    def end(self):
        """Langkah akhir"""
        print("Proses selesai dengan sukses!")

if __name__ == '__main__':
    kuliah_informatika()
