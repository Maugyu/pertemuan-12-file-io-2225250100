def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    bagian = baris.split(",")

                    if len(bagian) != 2:
                        raise ValueError

                    nim = bagian[0].strip()
                    nilai = float(bagian[1].strip())

                    if not nim:
                        raise ValueError

                    data.append((nim, nilai))

                except ValueError:
                    print(
                        f"Baris {nomor} dilewati: {baris}"
                    )

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")

    return data


def tulis_rekap(nama_file, data):
    if not data:
        print("Tidak ada data valid untuk direkap.")
        return

    nilai = [item[1] for item in data]

    jumlah_data = len(nilai)
    rata_rata = sum(nilai) / jumlah_data
    minimum = min(nilai)
    maksimum = max(nilai)

    jumlah_lulus = sum(
        1 for angka in nilai if angka >= 60
    )

    with open(nama_file, "w", encoding="utf-8") as file:
        file.write("REKAP NILAI MAHASISWA\n")
        file.write("=====================\n")
        file.write(f"Jumlah data valid: {jumlah_data}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {minimum:.2f}\n")
        file.write(f"Nilai maksimum: {maksimum:.2f}\n")
        file.write(f"Jumlah lulus: {jumlah_lulus}\n")

    print("Rekap berhasil disimpan.")
    print(f"Jumlah data valid: {jumlah_data}")
    print(f"Rata-rata: {rata_rata:.2f}")
    print(f"Nilai minimum: {minimum:.2f}")
    print(f"Nilai maksimum: {maksimum:.2f}")
    print(f"Jumlah lulus: {jumlah_lulus}")


if __name__ == "__main__":
    input_file = "data/nilai.txt"
    output_file = "data/hasil_rekap.txt"

    data = baca_data(input_file)

    if data:
        tulis_rekap(output_file, data)