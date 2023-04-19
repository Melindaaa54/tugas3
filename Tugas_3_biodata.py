# Membuat kamus berisi biodata mahasiswa dan nilai matakuliah
mahasiswa = {
    "Melinda": {
        "nim": "TI19220009",
        "alamat": "batu menek",
        "prodi": "teknik Informatika",
        "semester": 2,
        "ipk": 3.5,
        "nilai_matakuliah": {
            "Pemrograman Dasar": 80,
            "Kalkulus": 85,
            "Matematika diskrit": 75
        }
    },
    "Laela": {
        "nim": "TI19220011",
        "alamat": "jelantik",
        "prodi": "teknik Informatika",
        "semester": 2,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "Kalkulus": 90,
            "Algoritma dan pemograman": 87,
            "Struktur Data": 92
        }
    },
    "nora": {
        "nim": "TI19220017",
        "alamat": "ganti",
        "prodi": "teknik Informatika",
        "semester": 2,
        "ipk": 3.6,
        "nilai_matakuliah": {
            "Algoritma dan pemrograman": 85,
            "Kalkukus": 80,
            "Struktur Data": 90
        }
    },
    "Juli muslim ihsan": {
        "nim": "TI19220021",
        "alamat": "batukliang",
        "prodi": "Teknik Informatika",
        "semester": 2,
        "ipk": 3.7,
        "nilai_matakuliah": {
            "Matematika diskrit": 88,
            "Kalkulus ": 85,
            "Struktur Data": 92
        }
    },
    "Hasan": {
        "nim": "TI19220023",
        "alamat": "tenganan",
        "prodi": "Teknik Informatika",
        "semester": 2,
        "ipk": 3.9,
        "nilai_matakuliah": {
            "Matematika diskrit": 95,
            "Kalkulus": 92,
            "Struktur Data": 93
        }
    }
}

# Menampilkan biodata mahasiswa dan nilai akumulasi tiga matakuliah
for nama, data in mahasiswa.items()
    print("Biodata Mahasiswa")
    print("Nama          :", nama)
    print("NIM           :", data["nim"])
    print("Alamat        :", data["alamat"])
    print("Program Studi :", data["prodi"])
    print("Semester      :", data["semester"])
    print("IPK           :", data["ipk"])
    print("Nilai Akumulasi Matakuliah:")
    total_nilai = 0
    for matakuliah, nilai in data["nilai_matakuliah"].items():
        print("-", matakuliah, ":", nilai)
        total_nilai += nilai
    print("Total Nilai:", total_nilai)
    print("")
