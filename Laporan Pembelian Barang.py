nama_suplier = input('Masukkan nama suplier:')
jumlah_barang = int(input('Masukkan jumlah barang:'))
harga_barang_1_pcs = int(input('Masukkan harga barang per pcs:'))

print('=======Laporan Pembelian Barang=======')
print('nama suplier:', nama_suplier)
print('jumlah barang:', jumlah_barang)
print('Harga barang per pcs:', harga_barang_1_pcs)
Total_harga = jumlah_barang*harga_barang_1_pcs
print(f'Total harga: {Total_harga:,}')