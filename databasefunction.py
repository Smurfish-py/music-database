from databasestorage import hapus_output
#Fungsi untuk menambahkan data baru
def tambahkan_data(list_musik):
    def user_input():
        user_music_name = input("Masukkan judul lagu : ")
        user_genre = input("Masukkan jenis genre : ")
        user_artist = input("Masukkan nama artis : ")
        user_album = input("Masukkan nama album (Jika single maka masukkan saja Single pada bagian input) : ")
        user_year = input("Masukkan tahun rilis (Harus berupa angka): ")
        hapus_output()
        print(f""">>> PERHATIAN!
Nama Musik  : {user_music_name}
Jenis Genre : {user_genre}
Nama Artis  : {user_artist}
Nama Album  : {user_album}
Tahun Rilis : {user_year}""")
        def confirmationfunc():
            confirmation = int(input("\nNOTIFIKASI : Apakah data diatas sudah sesuai [1]Ya / [2]Tidak? "))
            if confirmation == 1:
                list_baru = {
                    'nama_musik' : user_music_name,
                    'genre' : user_genre,
                    'artis' : user_artist,
                    'album' : user_album,
                    'tahun' : user_year,
                }
                list_musik.append(list_baru)
            elif confirmation == 2:
                hapus_output()
                print("NOTIFIKASI : Anda memilih opsi tidak\n")
                user_input()
            else:
                hapus_output()
                print("NOTIFIKASI : Harap masukkan input yang valid!\n")
                confirmationfunc()
        confirmationfunc()
    user_input()

#Fungsi untuk simple user interface
def ui():
    print("""
                                                            █▀█▄▄▄▄     ██▄
                                                            █▀▄▄▄▄█     █▀▀█
                                                         ▄▄▄█     █  ▄▄▄█
                                                        ██▀▄█ ▄██▀█ ███▀█
                                                         ▀▀▀  ▀█▄█▀ ▀█▄█▀
          
                                        █▀▄▀█ █ █ █▀ █ █▀▀   █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄▄ ▄▀█ █▀ █▀▀
                                        █ ▀ █ █▄█ ▄█ █ █▄▄   █▄▀ █▀█  █  █▀█ █▄█ █▀█ ▄█ ██▄

                                                            Kelompok :
                                                1. Charolline Gisella Hetharia [03]
                                                2. Filipus Oey [08]
                                                3. Muhamad Rifqi Kurniawan [16]
                                                4. Muhammad Nabil Abyaz Fauzi [19]
                                                5. Naura Putri Ghisella [21]
                                                    
                                                            Pilihan :
                                                [1] Tambahkan data           
                                                [2] Tampilkan data               
                                                [3] Ubah data          
                                                [4] Hapus data            
                                                [Enter] Keluar / Hentikan program

""")

#Fungsi untuk header tabel
def buat_header():
    table = ['NO', 'JUDUL LAGU', 'GENRE', 'ARTIS', 'ALBUM', 'TAHUN']
    print("Berikut adalah data yang tersimpan di database")
    print(f"+{'='*121}+")
    print('| {:02}. | {:<21} | {:<21} | {:<31} | {:<22} | {:<6} |'.format(*table))
    print(f"+{'='*121}+")

#Fungsi untuk memanggil data
def panggil_data(list_musik):
    if not list_musik:
        print("Tidak ada data!")
        return
    number = 1
    for listdata in list_musik:
        print('| {:02}. | {:<21} | {:<21} | {:<31} | {:<22} | {:<6} |'.format(number, listdata['nama_musik'], listdata['genre'], listdata['artis'], listdata['album'], listdata['tahun']))
        number += 1
        print(f"+{'—'*121}+")

def panggil_data_list(list_musik):
    if not list_musik:
        print("Tidak ada data!")
        return
    for listdata in list_musik:
        print('''Judul Lagu  : {:<21}
Genre       : {:<21}
Artis       : {:<31}
Album       : {:<22}
Tahun Rilis : {:<6}'''.format(listdata['nama_musik'], listdata['genre'], listdata['artis'], listdata['album'], listdata['tahun']))
        print("-"*40)

#Fungsi untuk menghapus data
def hapus_data(list_musik):
    if not list_musik:
        hapus_output()
        print("NOTIFIKASI : Tidak ada data yang bisa dihapus!")
        return
    buat_header()
    panggil_data(list_musik)
    print('='*123)
    user_num = int(input("Masukkan nomor data yang ingin anda hapus datanya : "))
    hapus_output()
    user_choice = int(input("""
[1] YA
[2] TIDAK (Kembali ke menu utama)
NOTIFIKASI : Apakah anda yakin untuk menghapus data?"""))
    if user_choice == 1:
        list_musik.pop(user_num -1)
        hapus_output()
        print("NOTIFIKASI : Data telah dihapus!\n")
    elif user_choice == 2:
        hapus_output()
        print("NOTIFIKASI : Data tidak jadi dihapus")
    else:
        hapus_output()
        print("Masukkan input yang sesuai!")

#Fungsi untuk mengubah data
def ubah_data(list_musik):
    if not list_musik:
        hapus_output()
        print("NOTIFIKASI : Tidak ada data yang bisa diubah!")
        return
    buat_header()
    panggil_data(list_musik)
    print('='*123)
    user_num = int(input("Masukkan nomor data yang ingin anda ubah datanya : "))
    ubah_data_musik = list_musik[user_num - 1]
    def change_data_choices():
        print("""
    Apa yang ingin anda ubah ?
    [1] Judul Lagu
    [2] Jenis Genre
    [3] Nama Artis
    [4] Nama Album
    [5] Tahun Rilis
    [6] Seluruh Data
            """)
        user_num_choices = int(input("Masukkan angkanya saja : "))
        if user_num_choices == 1:
            def ubahDataMusik():
                ubah_data_musik['nama_musik'] = input("Masukkan judul lagu baru : ")
                hapus_output()
                print(f"PERHATIAN! Judul lagu akan diubah menjadi : {ubah_data_musik['nama_musik']}")
                def confirmationname():
                    confirmationdata = int(input("Apakah data yang anda ubah sudah benar ([1]Ya / [2]Tidak)? "))
                    if confirmationdata == 1:
                        return
                    elif confirmationdata == 2:
                        hapus_output()
                        print("NOTIFIKASI : Anda memilih opsi tidak\n")
                        ubahDataMusik()
                    else:
                        hapus_output()
                        print("NOTIFIKASI : Harap masukkan input yang valid!\n")
                        confirmationname()
                confirmationname()
            ubahDataMusik()
        elif user_num_choices == 2:
            def ubahDataGenre():
                ubah_data_musik['genre'] = input("Masukkan jenis genre baru : ")
                hapus_output()
                print(f"PERHATIAN! Jenis genre akan diubah menjadi : {ubah_data_musik['genre']}")
                def confirmationgenre():
                    confirmationdata = int(input("Apakah data yang anda ubah sudah benar ([1]Ya / [2]Tidak)? "))
                    if confirmationdata == 1:
                        return
                    elif confirmationdata == 2:
                        hapus_output()
                        print("NOTIFIKASI : Anda memilih opsi tidak\n")
                        ubahDataGenre()
                    else:
                        hapus_output()
                        print("NOTIFIKASI : Harap masukkan input yang valid!\n")
                        confirmationgenre()
                confirmationgenre()
            ubahDataGenre()
        elif user_num_choices == 3:
            def ubahDataArtis():
                ubah_data_musik['artis'] = input("Masukkan nama artis baru : ")
                hapus_output()
                print(f"PERHATIAN! Nama artis akan diubah menjadi : {ubah_data_musik['artis']}")
                def confirmationartis():
                    confirmationdata = int(input("Apakah data yang anda ubah sudah benar ([1]Ya / [2]Tidak)? "))
                    if confirmationdata == 1:
                        return
                    elif confirmationdata == 1:
                        hapus_output()
                        print("NOTIFIKASI : Anda memilih opsi tidak\n")
                        ubahDataArtis()
                    else:
                        hapus_output()
                        print("NOTIFIKASI : Harap masukkan input yang valid!\n")
                        confirmationartis()
                confirmationartis()
            ubahDataArtis()
        elif user_num_choices == 4:
            def ubahDataAlbum():
                ubah_data_musik['album'] = input("Masukkan nama album baru : ")
                hapus_output()
                print(f"PERHATIAN! Nama album akan diubah menjadi : {ubah_data_musik['album']}")
                def confirmationalbum():
                    confirmationdata = int(input("Apakah data yang anda ubah sudah benar ([1]Ya / [2]Tidak)? "))
                    if confirmationdata == 1:
                        return
                    elif confirmationdata == 1:
                        hapus_output()
                        print("NOTIFIKASI : Anda memilih opsi tidak\n")
                        ubahDataAlbum()
                    else:
                        hapus_output()
                        print("NOTIFIKASI : Harap masukkan input yang valid!\n")
                        confirmationalbum()
                confirmationalbum()
            ubahDataAlbum()
        elif user_num_choices == 5:
            def ubahDataTahun():
                ubah_data_musik['tahun'] = int(input("Masukkan tahun rilis baru (Harus berupa angka): "))
                hapus_output()
                print(print(f"PERHATIAN! Tahun rilis akan diubah menjadi : {ubah_data_musik['tahun']}"))
                def confirmationtahun():
                    confirmationdata = int(input("Apakah data yang anda ubah sudah benar ([1]Ya / [2]Tidak)? "))
                    if confirmationdata == 1:
                        return
                    elif confirmationdata == 1:
                        hapus_output()
                        print("NOTIFIKASI : Anda memilih opsi tidak\n")
                        ubahDataTahun()
                    else:
                        hapus_output()
                        print("NOTIFIKASI : Harap masukkan input yang valid!\n")
                        confirmationtahun()
                confirmationtahun()
            ubahDataTahun()
        elif user_num_choices == 6:
            def ubahDataSemua():
                ubah_data_musik['nama_musik'] = input("Masukkan judul lagu baru : ")
                ubah_data_musik['genre'] = input("Masukkan jenis genre baru : ")
                ubah_data_musik['artis'] = input("Masukkan nama artis baru : ")
                ubah_data_musik['album'] = input("Masukkan nama album baru : ")
                ubah_data_musik['tahun'] = int(input("Masukkan tahun rilis baru (Harus berupa angka): "))
                hapus_output()
                print(f""">>> PERHATIAN!
Judul lagu akan diubah menjadi  : {ubah_data_musik['nama_musik']}
Jenis genre akan diubah menjadi : {ubah_data_musik['genre']}
Nama artis akan diubah menjadi  : {ubah_data_musik['artis']}
Nama album akan diubah menjadi  : {ubah_data_musik['album']}
Tahun rilis akan diubah menjadi : {ubah_data_musik['tahun']}\n""")
                def confirmationsemua():
                    confirmationdata = int(input("Apakah data yang anda ubah sudah benar ([1]Ya / [2]Tidak)? "))
                    if confirmationdata == 1:
                        return
                    elif confirmationdata == 1:
                        hapus_output()
                        print("NOTIFIKASI : Anda memilih opsi tidak\n")
                        ubahDataSemua()
                    else:
                        hapus_output()
                        print("NOTIFIKASI : Harap masukkan input yang valid!\n")
                        confirmationsemua()
                confirmationsemua()
            ubahDataSemua()
    change_data_choices()
    hapus_output()
    print("NOTIFIKASI : Data telah diubah!\n")