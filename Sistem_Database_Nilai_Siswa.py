import math

dict_siswa = {
    'nama': ['Budi', 'Siti', 'Andi', 'Rina', 'Dodi'],
    'matematika': [85, 90, 78, 92, 70],
    'bahasa_indonesia': [88, 85, 80, 95, 75],
    'bahasa_inggris': [80, 88, 75, 90, 72],
    'ipa': [90, 87, 82, 88, 68]
}


def hitung_rata(index):
    scores = [
        dict_siswa['matematika'][index],
        dict_siswa['bahasa_indonesia'][index],
        dict_siswa['bahasa_inggris'][index],
        dict_siswa['ipa'][index]
    ]
    return sum(scores) / len(scores)


def daftar_siswa():
    print(f"\n{'Index':<6} | {'Nama':<12} | {'Matematika':<11} | {'B. Indonesia':<13} | {'B. Inggris':<11} | {'IPA':<5} | {'Rata-rata'}")
    print('-' * 85)
    for i in range(len(dict_siswa['nama'])):
        rata = hitung_rata(i)
        print(f"{i:<6} | {dict_siswa['nama'][i]:<12} | {dict_siswa['matematika'][i]:<11} | {dict_siswa['bahasa_indonesia'][i]:<13} | {dict_siswa['bahasa_inggris'][i]:<11} | {dict_siswa['ipa'][i]:<5} | {rata:.2f}")
    print()


def menu():
    return int(input('''\n============================
  Sistem Database Nilai Siswa
============================
Menu:
1. Tampilkan Data Siswa
2. Tambah Data Siswa
3. Update Nilai Siswa
4. Hapus Data Siswa
5. Exit

Pilihan: '''))


while True:
    pilihan = menu()

    if pilihan == 1:
        daftar_siswa()

    elif pilihan == 2:
        daftar_siswa()
        while True:
            while True:
                nama_baru = input('Nama siswa: ').title()
                if nama_baru in dict_siswa['nama']:
                    print(f'Data siswa "{nama_baru}" sudah ada dalam tabel! Silahkan masukkan nama lain.\n')
                else:
                    break
            mtk = int(input('Nilai Matematika (0-100): '))
            bind = int(input('Nilai Bahasa Indonesia (0-100): '))
            bing = int(input('Nilai Bahasa Inggris (0-100): '))
            ipa = int(input('Nilai IPA (0-100): '))

            dict_siswa['nama'].append(nama_baru)
            dict_siswa['matematika'].append(mtk)
            dict_siswa['bahasa_indonesia'].append(bind)
            dict_siswa['bahasa_inggris'].append(bing)
            dict_siswa['ipa'].append(ipa)

            print(f'\nData siswa "{nama_baru}" berhasil ditambahkan!')
            daftar_siswa()

            lagi = int(input('Apakah ingin menambah data siswa lagi?\n1. Ya (masukkan 1)\n2. Tidak (masukkan 2)\nPilihan: '))
            if lagi == 2:
                break

    elif pilihan == 3:
        daftar_siswa()
        while True:
            idx = int(input('Masukkan index siswa yang ingin diupdate: '))
            if 0 <= idx < len(dict_siswa['nama']):
                print(f'\nUpdate nilai untuk: {dict_siswa["nama"][idx]}')
                print('(Tekan Enter untuk melewati / tidak mengubah nilai)\n')

                input_mtk = input(f'Nilai Matematika saat ini [{dict_siswa["matematika"][idx]}]: ')
                input_bind = input(f'Nilai B. Indonesia saat ini [{dict_siswa["bahasa_indonesia"][idx]}]: ')
                input_bing = input(f'Nilai B. Inggris saat ini [{dict_siswa["bahasa_inggris"][idx]}]: ')
                input_ipa = input(f'Nilai IPA saat ini [{dict_siswa["ipa"][idx]}]: ')

                if input_mtk:
                    dict_siswa['matematika'][idx] = int(input_mtk)
                if input_bind:
                    dict_siswa['bahasa_indonesia'][idx] = int(input_bind)
                if input_bing:
                    dict_siswa['bahasa_inggris'][idx] = int(input_bing)
                if input_ipa:
                    dict_siswa['ipa'][idx] = int(input_ipa)

                print(f'\nNilai siswa "{dict_siswa["nama"][idx]}" berhasil diupdate!')
                daftar_siswa()

                lagi = int(input('Apakah ingin mengupdate data siswa lagi?\n1. Ya (masukkan 1)\n2. Tidak (masukkan 2)\nPilihan: '))
                if lagi == 2:
                    break
            else:
                print('Index tidak valid!')

    elif pilihan == 4:
        daftar_siswa()
        while True:
            hapus = int(input('Masukkan index siswa yang ingin dihapus: '))
            if 0 <= hapus < len(dict_siswa['nama']):
                nama_hapus = dict_siswa['nama'][hapus]
                for key in dict_siswa:
                    dict_siswa[key].pop(hapus)
                print(f'Data siswa "{nama_hapus}" berhasil dihapus!')
                daftar_siswa()

                lagi = int(input('Apakah ingin menghapus data siswa lagi?\n1. Ya (masukkan 1)\n2. Tidak (masukkan 2)\nPilihan: '))
                if lagi == 2:
                    break
            else:
                print('Index tidak valid!')

    elif pilihan == 5:
        print('Terima kasih, sampai jumpa!')
        break

    else:
        print('Pilihan tidak valid! Masukkan angka 1-5.')
