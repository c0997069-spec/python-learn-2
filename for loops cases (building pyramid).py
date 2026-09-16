#for loops cases (building pyramid)

SHOW_PROGRESS = True   # ubah ke False pas submit ke judge

n_kasus = int(input('Enter the number of test cases: '))
block = int(input('Enter the number of blocks: '))

for i in range(n_kasus):
    sisa = block
    height = 0
    for day in range(1, block + 1):      # day 1, 2, 3, ... jalan sendiri
        if sisa < day:
            if SHOW_PROGRESS:
                print(f'  day {day}: blok nggak cukup, berhenti')
            break
        sisa -= day
        height = day
        if SHOW_PROGRESS:
            print(f'  day {day}: pakai {day} blok, sisa {sisa}')
    print('The height of the pyramid:', height)

# penjelasannya:
#Baris 1 — SHOW_PROGRESS = True: Saklar lampu. Variabel boolean (isinya cuma True/False). Dia nggak ikut menghitung apa pun; dia cuma ngatur "tampilkan progres harian atau nggak". Buat belajar: True. Buat submit ke judge: False.
#Baris 3 — n_kasus = int(input(...)): Dua lapis. input(...) nampilin teks ke layar dan nunggu ketikan lo — hasilnya teks (string). int(...) mengonversi teks itu jadi angka. Angka itu disimpan di n_kasus: berapa banyak kasus uji yang bakal diproses.
#Baris 5 — for i in range(n_kasus):: Loop terluar = "meja pendaftaran kasus". range(n_kasus) nghasilin urutan 0, 1, 2, ... sampai n_kasus−1, jadi badan loop jalan tepat sebanyak n_kasus kali. Variabel i cuma penghitung putaran — isinya nggak dipakai di badan loop, dan itu wajar.
#Baris 6 — block = int(input(...)): Baca jumlah blok untuk kasus putaran ini, konversi ke angka. Tiap putaran loop terluar minta input baru — makanya tiga kasus cukup satu kali play.
#Baris 7 — sisa = block: Bikin "dompet": salin jumlah blok jadi sisa blok yang tersedia. Disalin biar nilai asli block tetap utuh (dipakai buat batas range di baris 9).
#Baris 8 — height = 0: Catatan tinggi mulai dari nol — piramida belum dibangun sama sekali.
#Baris 9 — for day in range(1, block + 1):: Loop dalam = "kalender pembangunan". day berjalan 1, 2, 3, ... sampai block. Kenapa block + 1? Karena batas atas range itu eksklusif (nggak ikut), dan secara logika tinggi piramida nggak mungkin melebihi jumlah blok (tiap lantai minimal makan 1 blok) — jadi ini batas aman.
#Baris 10 — if sisa < day:: Gerbang cek-dulu-bayar-kemudian. Lantai yang dibangun hari ini bernomor day dan harganya day blok. Kalau dompet (sisa) lebih kecil dari harga → nggak mampu.
#Baris 11–12 — if SHOW_PROGRESS: print(f'...'): Kalau saklar nyala, cetak pesan berhenti. Perhatikan awalan f'...' — itu f-string: teks yang boleh menyelipkan nilai variabel di dalam kurung kurawal {day}. Tanpa huruf f, {day} bakal ketik apa adanya sebagai teks.
#Baris 13 — break: Rem darurat. Langsung keluar dari loop dalam (kalender berhenti). Baris 14–17 untuk hari ini dilewati — karena memang nggak mampu bayar, jangan pernah memotong dompet yang kosong.
#Baris 14 — sisa -= day: Bayar. Bentuk singkat dari sisa = sisa - day. Dompet berkurang sebesar harga lantai hari ini.
#Baris 15 — height = day: Catat tinggi. Lantai nomor day baru aja berhasil dibangun, jadi tinggi piramida saat ini = day. (Ini kenapa kita nggak perlu height += 1 — nomor hari dan nomor lantai dan tinggi itu angka yang sama.)
#Baris 16–17 — progres opsional: Kalau saklar nyala, lapor: hari ke berapa, bayar berapa, sisa berapa. Buat nonton mesinnya bekerja.
#Baris 18 — print('The height of the pyramid:', height): Setelah loop dalam selesai (kena break atau hari habis), laporkan tinggi final untuk kasus ini. Perhatikan indentasinya: sejajar dengan baris 6–8, artinya dia anggota loop terluar — dia jalan sekali per kasus, bukan sekali per hari. Koma di print otomatis menambah spasi sebelum angka.