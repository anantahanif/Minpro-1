print ("Nama    :Ananta Hanif Fidzya Pratama")
print ("Kelas   :Sistem Informasi A'25")
print ("NIM     :2509116023")
print ("Tugas   :Mini Project 1")


inventaris = [
    ["krimer", 10, "pcs"],
    ["skm", 60, "kaleng"],
    ["susu uht", 20, "dus"],
    ["kopi", 25, "pack"],
    ["evaporasi", 10, "dus" ],
    ["es batu", 50, "pack"]
]

while True:
    print("=== Inventaris Stok Gudang ===")
    print("1. Lihat Stok ")
    print("2. Tambah Stok")
    print("3. Ubah Stok")
    print("4. Hapus Stok")
    print("5. Keluar")
    menu = input("Pilih menu (1-5): ")

    if menu == "1":
        print("Daftar Stok Opname Bahan:")
        for i, item in enumerate(inventaris):
            print(i+1 , item[0] ,"- stok:", item[1] , item[2])
    elif menu == "2":
        nama = input("Nama Stok Bahan: ").lower()
        stok = int(input("Jumlah stok bahan?: "))
        jenis = input("Jenis stok bahan?: ")
        inventaris.append([nama, stok, jenis])
        print("Stok berhasil ditambahkan.")
    elif menu == "3":
        for i, item in enumerate(inventaris):
            print(i+1 , item[0] ,"- stok:", item[1] , item[2])
        idx = int(input("Pilih bahan stok yang mau diubah: ")) - 1
        if 0 <= idx < len(inventaris):
            nama_baru = input("Nama bahan yang mau di ubah?: ").lower()
            stok_baru = int(input("Berapa stok bahan?: "))
            jenis_baru = input("Jenis kemasannya?: ")
            inventaris[idx][0] = nama_baru
            inventaris[idx][1] = stok_baru
            inventaris[idx][2] = jenis_baru
            print("Stok berhasil diubah.")
        else:
            print("Nomor tidak valid.")
    elif menu == "4":
        for i, item in enumerate(inventaris):
            print(i+1 , item[0] ,"- stok:", item[1] , item[2])
        idx = int(input("Pilih bahan stok yang mau dihapus: ")) - 1
        if 0 <= idx < len(inventaris):
            inventaris.pop(idx)
            print("stok berhasil dihapus.")
        else:
            print("Nomor tidak valid.")
    elif menu == "5":
        print("Keluar dari program.")
        break
    else:
        print("Menu tidak ditemukan.")