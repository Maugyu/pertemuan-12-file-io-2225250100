with open("data/nilai.txt", "r", encoding="utf-8") as file:
    for nomor, baris in enumerate(file, start=1):
        baris = baris.strip()

        if not baris:
            continue

        try:
            nim, teks_nilai = baris.split(",")
            nilai = float(teks_nilai)
            print(f"NIM: {nim}, Nilai: {nilai:g}")

        except ValueError:
            print(f"Baris {nomor} tidak valid: {baris}")