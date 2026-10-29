# Pertemuan 12 - File I/O dan Error Handling

Nama: Maulyditha Revania Aprilliyanti  
NIM: 2225250100  
Kelas: 3A

## Tujuan

Mempelajari cara membaca, menulis, memvalidasi, mengolah, dan menyimpan data menggunakan file pada Python.

## Struktur Folder

```text
pertemuan-12-file-io/
├── .gitignore
├── README.md
├── KUIS_FORMATIF.txt
├── data/
│   ├── catatan.txt
│   └── nilai.txt
├── latihan/
│   ├── latihan_1_menulis_file.py
│   ├── latihan_2_membaca_file.py
│   ├── latihan_3_append_file.py
│   ├── latihan_4_proses_baris.py
│   ├── latihan_5_file_tidak_ditemukan.py
│   └── latihan_6_value_error.py
└── tugas/
    └── rekap_nilai_file.py
```

## Format File Input

File nilai.txt menggunakan format NIM,nilai.

Contoh:

```text
A001,85
A002,78
A003,92
```

Baris kosong akan dilewati. Baris dengan format atau nilai yang tidak valid akan dilaporkan dan dilewati agar data lainnya tetap dapat diproses.

## Cara Menjalankan Program

Jalankan perintah berikut melalui terminal VS Code dari folder utama proyek.

```bash
python latihan/latihan_1_menulis_file.py
python latihan/latihan_2_membaca_file.py
python latihan/latihan_3_append_file.py
python latihan/latihan_4_proses_baris.py
python latihan/latihan_5_file_tidak_ditemukan.py
python latihan/latihan_6_value_error.py
python tugas/rekap_nilai_file.py
```

## Error yang Ditangani

1. FileNotFoundError: menangani file yang tidak ditemukan.
2. ValueError: menangani nilai atau format data yang tidak valid.

## Test Case

1. Semua baris valid: seluruh data diproses dan statistik dihitung.
2. File input hilang: program menampilkan pesan kesalahan.
3. Nilai invalid: baris yang tidak valid dilewati.
4. Baris kosong: baris kosong dilewati.
5. Nilai 60: dihitung sebagai lulus.

## Hasil Pengujian

Data contoh terdiri atas enam baris, dengan satu baris yang memiliki nilai tidak valid.

Hasil yang diharapkan:
- Jumlah data valid: 5
- Rata-rata: 83.40
- Minimum: 74.00
- Maksimum: 92.00
- Jumlah lulus: 5

## Refleksi

Penanganan error diperlukan agar program tetap dapat memproses data yang valid meskipun terdapat baris yang salah. Penggunaan with juga membantu memastikan file ditutup secara otomatis setelah selesai digunakan.
