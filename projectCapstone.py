# Fungsi untuk mendapatkan stok barang awal
def get_stock():
  daftarBarang = [
    ['Kamera',      20, 10000],
    ['Printer',     15, 15000],
    ['Vacuum',      25, 20000],
    ['Handphone',   10, 30000],
    ['Laptop',      10, 10000],
  ]
  return daftarBarang

# Fungsi untuk menampilkan daftar barang dalam format tabel
def tampilkan_daftar_barang(daftarBarang):
  print('Stock Barang\n')
  print('-' * 49)
  print('| Kode\t| Nama Barang\t\t| Stock\t| Harga\t|')
  print('-' * 49)
  for i in range(len(daftarBarang)):
      print('| {}\t| {}  \t\t| {}\t| {} |'.format(i, daftarBarang[i][0], daftarBarang[i][1], daftarBarang[i][2]))
      print('-' * 49)


# Fungsi untuk menambahkan barang baru ke stok
def tambah_barang():
  nama = input('Masukkan Nama Barang : ')
  stock = int(input('Masukkan Stock Barang : '))
  harga = int(input('Masukkan Harga Barang : '))
  list = [nama, stock, harga]
  return list

# Fungsi untuk menghapus barang dari stok
def hapus_barang(daftarBarang):
  kode = int(input('Masukkan kode barang yang ingin dihapus : '))
  return kode

# Fungsi untuk melakukan transaksi pembelian
def beli_barang(daftarBarang):
  cart = []
  while True:
    kode = int(input('Masukkan kode barang : '))
    quantity = int(input('Masukkan jumlah barang : '))
    if quantity > daftarBarang[kode][1]:
      print('Stock tidak cukup, stock {} sisa {}'.format(daftarBarang[kode][0], daftarBarang[kode][1]))
    else:
      cart.append([daftarBarang[kode][0], quantity, daftarBarang[kode][2], kode])
    print('Isi Cart :')
    print('Nama\t| Qty\t| Harga')
    for item in cart:
      print('{}\t| {}\t| {}'.format(item[0], item[1], item[2]))
    checker = input('Tambah barang lain? (yes/no) = ')
    if checker == 'no':
      break
    else:
      tampilkan_daftar_barang(daftarBarang)
  print('\nDaftar Belanja :')
  print('Nama\t| Qty\t| Harga\t| Total Harga')
  totalHarga = 0
  for item in cart:
    print('{}\t| {}\t| {}\t| {}'.format(item[0], item[1], item[2], item[1] * item[2]))
    totalHarga += item[1] * item[2]
  if kalkulasi_harga(totalHarga):
    for item in cart:
      daftarBarang[item[3]][1] -= item[1]
    cart.clear()
  else:
    kalkulasi_harga(totalHarga)

# Fungsi untuk mengkalkulasi harga total dan mengelola pembayaran 
def kalkulasi_harga(totalHarga):
  print('\nTotal pembayaran = {}'.format(totalHarga))
  jmlUang = int(input('Masukkan jumlah uang : '))
  if jmlUang > totalHarga:
    kembali = jmlUang - totalHarga
    print('\nUang yang dikembalikan : {}'.format(kembali))
    return True
  elif jmlUang == totalHarga:
    print('\nPembelian Berhasil')
    return True
  else:
    kekurangan = totalHarga - jmlUang
    print('Uang tidak mencukupi sebesar {}'.format(kekurangan))

# Inisialisasi stok barang dan tampilan menu utama
daftarBarang = get_stock()
title = '''
=================== Electronic Store ===================
| Main Menu :                                          |
| 1. Tampilkan Stock Barang                            |
| 2. Tambah Stock Barang                               |
| 3. Hapus Barang                                      |
| 4. Beli Barang                                       |
| 5. Exit                                              |
========================================================                            
Masukkan Angka Menu yang ingin dijalankan : '''

# Fungsi utama untuk mengatur alur program
def main():
  pilihanMenu = input(title)
  if    pilihanMenu == '1':
        tampilkan_daftar_barang(daftarBarang)
  elif  pilihanMenu == '2':
        daftarBarang.append(tambah_barang())
        tampilkan_daftar_barang(daftarBarang)
  elif  pilihanMenu == '3':
        tampilkan_daftar_barang(daftarBarang)
        del daftarBarang[hapus_barang(daftarBarang)]
  elif  pilihanMenu == '4':
        tampilkan_daftar_barang(daftarBarang)
        beli_barang(daftarBarang)
  elif  pilihanMenu == '5':
        exit()
  main()

main()

