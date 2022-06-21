print("\t~~~~~~~~~~~~ Selamat Datang di Jasa Ekspedisi TIMETRAVELER ~~~~~~~~~~~\n")

total  = 0
provinsi = []
barang = []
harga = []

while True:
    print("""\t______________________________________________________________________
    \t\tDaftar Biaya & Pelayanan Ekspedisi Barang TIMETRAVELER
\t======================================================================
\t\tkode\t|\tProvinsi\t|\t     Biaya
\t----------------------------------------------------------------------
\t\t10245\t| Jawa Timur \t\t| 10000/kg
\t\t20367\t| Jawa Barat \t\t| 25000/kg
\t\t30212\t| Jawa Tengah \t\t| 15000/kg
\t\t40398\t| Sumatera \t\t| 9000/kg
\t\t50657\t| Sulawesi \t\t| 10000/kg  
\t\t68474\t| Bali \t\t\t| 24000/kg
\t\t70890\t| Kalimantan \t\t| 15000/kg
\t\t80982\t| Luar Negeri \t\t| 100000/kg
\t======================================================================                       
\t\tJenis Layanan \t|\t             Biaya
\t----------------------------------------------------------------------
\t\t1. Reguler \t|\t+5000
\t\t2. Express \t|\t+10000
\t\t3. Kilat \t|\t+15000
\t======================================================================

    """)
   
# Input Informasi Barang
    print("\n-------------------- Masukan Alamat --------------------")
    Asal_kota     = input("Kota : ")
    Asal_Kec      = input("Kecamatan : ")
    Asal_Prov     = input("Provinsi : ")
    Jenis_Barang  = input("Masuk jenis barang : ")
    Berat_Barang  = int(input("Masukan berat barang(kg) : "))
    Jenis_Layanan = input("Masukan jenis layanan? (reguler/exspress/kilat) : ")
    
# Cetak Resi
    if Asal_Prov == 'Jawa Timur':
        print("No. Resi : TITRALE10245")
        print("==================================================\n")
    elif Asal_Prov == 'Jawa Barat':
        print("No. Resi : TITRALER20367")
        print("==================================================\n")
    elif Asal_Prov == 'Jawa Tengah':
        print("No. Resi : TITRALER30212")
        print("=======================================================\n")
    elif Asal_Prov == 'Sumatera':
        print("No. Resi : TITRALER40398")
        print("=======================================================\n")
    elif Asal_Prov == 'Sulawesi':
        print("No. Resi : TITRALER50657")
        print("=======================================================\n")
    elif Asal_Prov == 'Bali':
        print("No. Resi : TITRALER68474")
        print("=======================================================\n")
    elif Asal_Prov == 'Kalimantan':
        print("No. Resi : TITRALER70890")
        print("=======================================================\n")
    else:
        print("No. Resi : TITRALER80982")
        print("=======================================================\n")
        
# Pembayaran
    if Asal_Prov == 'Jawa Timur':
        harga.append(8000)
        total += 8000
    elif Asal_Prov == 'Jawa Barat':
        harga.append(21000)
        total += 21000
    elif Asal_Prov == 'Jawa Tengah':
        harga.append(15000)
        total += 15000
    elif Asal_Prov == 'Sumatera':
        harga.append(31000)
        total += 31000
    elif Asal_Prov == 'Sulawesi':
        harga.append(35000)
        total += 35000
    elif Asal_Prov == 'Bali':
        harga.append(18000)
        total += 18000
    elif Asal_Prov == 'Kalimantan':
        harga.append(25000)
        total += 25000
    else:
        harga.append(3000000)
        total += 3000000

    Kartu_Member = input('Apakah anda memiliki Kartu Member (y/t) : ')
    if Kartu_Member == 'y' or Kartu_Member == 'Y':
        input('Masukkan kode (8 digit) : ')
        print("\n-------------------Data Pemesanan-----------------")
        if Jenis_Layanan == 'reguler':
            print("Biaya Kirim Rp.", Berat_Barang*total+5000)
            print("Diskon member = -5000",)
            print("Total Biaya Kirim = Rp.", Berat_Barang*total)
            print('Estimasi Pengiriman = 3-4 hari')
        elif Jenis_Layanan == 'express':
            print("Biaya Kirim Rp.", Berat_Barang*total+10000)
            print("Diskon member = -10000",)
            print("Total Biaya Kirim = Rp.", Berat_Barang*total)
            print('Estimasi Pengiriman = 2-3 hari')
        elif Jenis_Layanan == 'kilat':
            print("Biaya Kirim Rp.", Berat_Barang*total+15000)
            print("Diskon member = -15000",)
            print("Total Biaya Kirim = Rp.", Berat_Barang*total)
            print('Estimasi Pengiriman = 1-2 hari')
            print("---------------------------------------------------")
        else:
            print('Layanan Tidak tersedia')
    elif Kartu_Member == 't' or Kartu_Member == 'T':
        print("\n-------------------Data Pemesanan-----------------")
        if Jenis_Layanan == 'reguler':
            print("Total Biaya Kirim = Rp.", Berat_Barang*total+5000)
            print('Estimasi Pengiriman = 3-4 hari')
        elif Jenis_Layanan == 'express':
            print("Total Biaya Kirim = Rp.", Berat_Barang*total+10000)
            print('Estimasi Pengiriman = 3-2 hari')
        elif Jenis_Layanan == 'kilat':
            print("Total Biaya Kirim = Rp.", Berat_Barang*total+15000)
            print('Estimasi Pengiriman = 2-1 hari')
            print("---------------------------------------------------")
        else:
            print('Layanan Tidak Tersedia')
    Proteksi = input("Tambah proteksi barang dengan gratis (y/t): ")
    if Proteksi == 'y' or Proteksi == 'Y':
        print("\n>>>>>>>>>>PAKET ANDA AKAN KAMI PROSES<<<<<<<<<<") 
    elif Proteksi == 't' or Proteksi == 'T':
        print("\n>>>>>>>>>>PAKET ANDA AKAN KAMI PROSES<<<<<<<<<<")
        
    lanjut = input('Lanjut Pengiriman Barang Lain (y/t) : ')
    if lanjut == 't' or lanjut == 'T':
        print("\n\n\t\t**********************************************************")
        print("\t\t>>>>>>>>>> TERIMA KASIH SUDAH MEMPERCAYAI KAMI <<<<<<<<<<<")
        print("\t\t**********************************************************")
        break