from metaflow import FlowSpec, step

class KuliahInformatika(FlowSpec):
    """Alur yang mensimulasikan perjalanan kuliah."""

    @step
    def start(self):
        """Titik awal"""
        print("Membayar biaya kuliah...")
        self.next(self.register)

    @step
    def register(self):
        """Langkah pendaftaran"""
        print("Mendaftar untuk kelas...")
        self.next(self.attend_classes)

    @step
    def attend_classes(self):
        """Langkah menghadiri kelas"""
        print("Menghadiri kelas...")
        self.total_attend = 14
        self.presence = 14  # Simulasi kehadiran penuh
        print(f"Kehadiran: {self.presence} dari {self.total_attend}")
        if self.presence >= 0.75 * self.total_attend:
            print("Memenuhi persyaratan kehadiran")
            self.next(self.receive_grades)
        else:
            print("Tidak memenuhi persyaratan kehadiran")
            self.next(self.end)

    @step
    def receive_grades(self):
        """Langkah menerima nilai"""
        self.midterm_grade = 80  # Nilai UTS
        self.final_grade = 90  # Nilai UAS
        print(f"Nilai UTS: {self.midterm_grade}, Nilai UAS: {self.final_grade}")
        self.next(self.calculate_final_score)

    @step
    def calculate_final_score(self):
        """Menghitung nilai akhir"""
        self.final_score = (self.midterm_grade + self.final_grade) / 2
        print(f"Nilai akhir: {self.final_score}")
        self.next(self.end)

    @step
    def end(self):
        """Langkah akhir"""
        print("Proses selesai!")

if __name__ == '__main__':
    KuliahInformatika()
