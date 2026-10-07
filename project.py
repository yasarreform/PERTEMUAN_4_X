def cek_status(nilai):
    if nilai >= 75:
        return "LULUS"
    return "TIDAK LULUS"


def tampilkan_siswa(siswa):
    print("Nama  :", siswa["nama"])
    print("Kelas :", siswa["kelas"])
    print("Nilai :", siswa["nilai"])
    print("Status:", cek_status(siswa["nilai"]))


data_siswa = []

print("==============================")
print("     TDC STUDENT DATABASE")
print("==============================")

while True:
    print()
    print("1. Input data siswa")
    print("2. Update nilai siswa")
    print("3. Hapus data siswa")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    match pilihan:
        case "1":
            jumlah = int(input("Jumlah siswa yang akan diinput: "))
            for i in range(jumlah):
                print()
                print("Siswa ke-", i + 1)
                nama = input("Nama  : ")
                kelas = input("Kelas : ")
                nilai = int(input("Nilai : "))

                siswa = {
                    "nama": nama,
                    "kelas": kelas,
                    "nilai": nilai
                }
                data_siswa.append(siswa)

            print("Data berhasil ditambahkan")

        case "2":
            cari = input("Nama siswa yang akan diupdate: ").lower()
            ditemukan = False

            for siswa in data_siswa:
                if siswa["nama"].lower() == cari:
                    nilai_baru = int(input("Nilai baru: "))
                    siswa["nilai"] = nilai_baru
                    print("Data berhasil diupdate")
                    tampilkan_siswa(siswa)
                    ditemukan = True
                    break

            if not ditemukan:
                print("Nama siswa tidak ditemukan")

        case "3":
            cari = input("Nama siswa yang akan dihapus: ").lower()
            ditemukan = False

            for siswa in data_siswa:
                if siswa["nama"].lower() == cari:
                    data_siswa.remove(siswa)
                    print("Data berhasil dihapus")
                    ditemukan = True
                    break

            if not ditemukan:
                print("Nama siswa tidak ditemukan")

        case "4":
            print("Program selesai")
            break

        case _:
            print("Pilihan tidak tersedia")

    if pilihan != "4":
        kembali = input("Kembali ke menu? (1 = Ya, 2 = Selesai): ")
        if kembali != "1":
            print("Program selesai")
            break

