teks = input("Masukkan nilai: ")

try:
    nilai = float(teks)
    print(f"Nilai = {nilai:g}")

except ValueError:
    print("Input harus berupa angka.")