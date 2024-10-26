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
        self.next(self.receive_grades)

    @step
    def receive_grades(self):
        """Langkah menerima nilai"""
        print("Menerima nilai akhir dan mengevaluasi kinerja...")
        self.next(self.end)

    @step
    def end(self):
        """Langkah akhir"""
        print("Proses selesai dengan sukses!")

if __name__ == '__main__':
    kuliah_informatika()
