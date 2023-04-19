# Membuat kamus berisi biodata mahasiswa dan nilai matakuliah
mahasiswa = {
    "Ari": {
        "nim": "SI19220015",
        "alamat": "Aik Bukak",
        "prodi": "Sistem Informasi",
        "semester": 2,
        "ipk": 3.5,
        "nilai_matakuliah": {
            "Pemrograman Dasar": 80,
            "Kalkulus": 85,
            "Fisika Dasar": 75
        }
    },
    "Reza Hardian": {
        "nim": "SI19220013",
        "alamat": "Braim",
        "prodi": "Sistem Informasi",
        "semester": 3,
        "ipk": 3.8,
        "nilai_matakuliah": {
            "Pemrograman Lanjut": 90,
            "Algoritma dan Struktur Data": 87,
            "Basis Data": 92
        }
    },
    "Hofiz Azizan": {
        "nim": "SI19220017",
        "alamat": "Bakan",
        "prodi": "Sistem Informasi",
        "semester": 2,
        "ipk": 3.6,
        "nilai_matakuliah": {
            "Jaringan Komputer": 85,
            "Sistem Digital": 80,
            "Manajemen Basis Data": 90
        }
    },
    "Hardian": {
        "nim": "SI19220021",
        "alamat": "Pegading",
        "prodi": "Teknik Informatika",
        "semester": 5,
        "ipk": 3.7,
        "nilai_matakuliah": {
            "Kimia Fisika": 88,
            "Rekayasa Proses Kimia": 85,
            "Termokimia": 92
        }
    },
    "Faruk": {
        "nim": "TI19220012",
        "alamat": "Peringga Rata",
        "prodi": "Teknik Informatika",
        "semester": 4,
        "ipk": 3.9,
        "nilai_matakuliah": {
            "Jaringan Komputer": 95,
            "Aljabar Linier": 92,
            "Konstruksi Beton": 93
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
