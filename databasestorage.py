import os
def hapus_output():
    os.system('cls' if os.name == 'nt' else 'clear')

#Fungsi untuk membuka file txt
def buka_list():
    musik = []
    try:
        with open('musicDatabase.txt', 'r') as file:
            for line in file:
                nama_musik, genre, artis, album, tahun = line.strip().split(',')
                musik.append({
                    'nama_musik' : nama_musik,
                    'genre' : genre,
                    'artis' : artis,
                    'album' : album,
                    'tahun' : int(tahun)
                })
    except FileNotFoundError:
        pass
    return musik

# Fungsi untuk menyimpan data
def menyimpan_data(musik):
    with open('musicDatabase.txt', 'w') as file:
        for data in musik:
            file.write(f"{data['nama_musik']},{data['genre']},{data['artis']},{data['album']},{data['tahun']}\n")