# Tugas 6 - Coding: Python Modules, File I/O, & OOP Sederhana

import numpy as np
import pandas as pd
import os

# Set seed agar output konsisten
np.random.seed(42)


# BAGIAN 1 – NumPy: Data & Statistik

nilai_array = np.array([85, 72, 91, 60, 78, 55, 88, 74, 65, 95, 50, 83])

rata_rata = np.mean(nilai_array)
median = np.median(nilai_array)
std_dev = np.std(nilai_array)
nilai_min = np.min(nilai_array)
nilai_max = np.max(nilai_array)


# BAGIAN 2 – Pandas: DataFrame

data = {
    "nama": ["A","B","C","D","E","F","G","H","I","J","K","L"],
    "nim": [
        "2021001","2021002","2021003","2021004",
        "2021005","2021006","2021007","2021008",
        "2021009","2021010","2021011","2021012",
    ],
    "nilai": nilai_array.tolist(),
}

df = pd.DataFrame(data)

df["status"] = df["nilai"].apply(lambda v: "LULUS" if v >= 70 else "TIDAK LULUS")


# BAGIAN 3 – File I/O

OUTPUT_FILE = "ringkasan_tugas6.txt"

jumlah_lulus = (df["status"] == "LULUS").sum()
jumlah_tidak_lulus = (df["status"] == "TIDAK LULUS").sum()

ringkasan_numpy = f"RINGKASAN\nJumlah Data   : {len(nilai_array)}\nRata-rata     : {rata_rata:.2f}\nMedian        : {median:.2f}\nStd Deviasi   : {std_dev:.2f}\nNilai Minimum : {nilai_min}\nNilai Maximum : {nilai_max}\n"

ringkasan_df = f"RINGKASAN DATAFRAME\nJumlah Baris        : {len(df)}\nJumlah LULUS        : {jumlah_lulus}\nJumlah TIDAK LULUS  : {jumlah_tidak_lulus}\nPersentase Lulus    : {jumlah_lulus / len(df) * 100:.1f}%\n"

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(ringkasan_numpy)
    f.write(ringkasan_df)


# BAGIAN 4 – OOP

class GradeBook:
    """Kelas sederhana untuk merangkum dan menganalisis nilai mahasiswa."""

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def average(self) -> float:
        return float(self.df["nilai"].mean())

    def pass_rate(self, threshold: float = 70.0) -> float:
        lulus = (self.df["nilai"] >= threshold).sum()
        return round(lulus / len(self.df) * 100, 2)

    def save_summary(self, path: str) -> None:
        ringkasan_oop = f"RINGKASAN OOP – GradeBook\nJumlah Data       : {len(self.df)}\nRata-rata Nilai   : {self.average():.2f}\nPersentase Lulus  : {self.pass_rate():.2f}%\nPersentase Tidak  : {100 - self.pass_rate():.2f}%\n\nDetail per Mahasiswa:\n{self.df[['nama', 'nim', 'nilai', 'status']].to_string(index=False)}\n"

        with open(path, "a", encoding="utf-8") as f:
            f.write(ringkasan_oop)

        print(f"[GradeBook] Ringkasan berhasil disimpan ke '{path}'")

    def __str__(self) -> str:
        return f"GradeBook(jumlah_data={len(self.df)}, rata_rata={self.average():.2f})"


# DEMO

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("=== NUMPY ===")
    print("=" * 50)
    print(f"Array Nilai   : {nilai_array}")
    print(f"Rata-rata     : {rata_rata:.2f}")
    print(f"Median        : {median:.2f}")
    print(f"Std Deviasi   : {std_dev:.2f}")
    print(f"Nilai Min     : {nilai_min}")
    print(f"Nilai Max     : {nilai_max}")

    print("\n" + "=" * 50)
    print("=== PANDAS ===")
    print("=" * 50)
    print(df.head())
    print(f"\nTotal Baris        : {len(df)}")
    print(f"Jumlah LULUS       : {jumlah_lulus}")
    print(f"Jumlah TIDAK LULUS : {jumlah_tidak_lulus}")

    print("\n" + "=" * 50)
    print("=== OOP: GRADEBOOK ===")
    print("=" * 50)

    gb = GradeBook(df)

    print(f"\nRepresentasi Objek : {gb}")
    print(f"Rata-rata Nilai    : {gb.average():.2f}")
    print(f"Persentase Lulus   : {gb.pass_rate():.2f}%")

    gb.save_summary(OUTPUT_FILE)

    print(f"\nFile ringkasan tersimpan : '{os.path.abspath(OUTPUT_FILE)}'")
    print("\n" + "=" * 50)