from databasefunction import ui, buat_header, tambahkan_data, panggil_data, hapus_data, ubah_data,panggil_data_list
from databasestorage import buka_list, menyimpan_data, hapus_output

list_data = buka_list()

def main():
    ui()
    user_input = input("\nMasukkan input anda : ")
    hapus_output()
    if user_input == '1':
        print("NOTIFIKASI : Anda memilih menambahkan data (Gunakan ';' sebagai pemisah. Contoh => EDM; Pop Rock)\n")
        tambahkan_data(list_data)
        menyimpan_data(list_data)
        hapus_output()
        print("NOTIFIKASI : Data baru telah ditambahkan!\n")
        main()
    elif user_input == '2':
        print("NOTIFIKASI : Anda memilih untuk menampilkan data\n")
        print("""\nJenis data yang ingin anda tampilkan :
[1] Tabel
[2] List\n""")
        user_subinput = int(input("Input anda : "))
        if user_subinput == 1:
            hapus_output()
            buat_header()
            panggil_data(list_data)
            print('='*123)
            input("\nTekan tombol Enter untuk kembali ke menu...")
            hapus_output()
            main()
        elif user_subinput == 2:
            hapus_output()
            print(f"""
{'='*40}
              LIST MUSIK""")
            print("="*40)
            panggil_data_list(list_data)
            print("="*40)
            input("\nTekan tombol Enter untuk kembali ke menu...")
            hapus_output()
            main()


    elif user_input == '3':
        print("NOTIFIKASI : Anda memilih untuk mengubah data (Gunakan ';' sebagai pemisah. Contoh => EDM; Pop Rock)\n")
        ubah_data(list_data)
        menyimpan_data(list_data)
        main()
    elif user_input == '4':
        print("NOTIFIKASI : Anda memilih untuk menghapus data\n")
        hapus_data(list_data)
        menyimpan_data(list_data)
        main()
    elif user_input == '':
        hapus_output()
        print("Program telah dihentikan!\nUntuk menjalankan kembali program, gunakan perintah 'python maincontent.py'.")
    else:
        print("NOTIFIKASI : Harap masukkan input yang sesuai dengan pilihan yang tersedia!\n")
        main()
main()