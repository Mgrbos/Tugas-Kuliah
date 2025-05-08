def soal1():
    umur = int(input('masukan umur anak:'))
    if umur < 7:
        print('anak tidak bisa diterima di SD.')
    else:
        print('anak bisa masuk SD')

def soal2():
    nilai = int(input('masukan nilai (1-100):'))
    if 85 <= nilai <= 100:
        print('nilai: A')
    elif 70 <= nilai <= 85:
        print('nilai: B')
    elif 55 <= nilai <= 70:
        print('nilai: C')
    else:
        print('nilai: D')

def soal3():
    # FOR
    print('perulangan FOR:')
    for i in range(1,6):
        print(f'iterasi {i}')
        
    #while
    print('\nPerulangan WHILE:')
    i = 1
    while i <= 5:
        print(f'iterasi {i}')
        i += 1

def soal4():
    # a. Ibu membeli 6 jenis sayuran
    sayuran = ['Bayam','Kangkung','Tomat','Sawi','KOl','Timun']
    print('a.Sayuran yang dibeli ibu:',sayuran)


    #b.Dalam perjalanan ibu tambahkan Wortel dan Terong
    sayuran.append('Terong')
    sayuran.append('Wortel')
    print('b.setelah ditambahkan Terong dan Wortel:',sayuran)


    #c. Ibu mengganti sayuran yang pertama dengan Brokoli
    sayuran[0] = 'Brokoli'
    print('c.Setelah mengganti sayuran pertama dengan brokoli:',sayuran)


    #d.Dalam perjalanan ibu kehilangan sayuran ke-5 (indeks ke-4)
    sayuran.pop(4)
    print('d.Setelah kehilangan sayuran ke-5:',sayuran)


    #e.Cetak sayuran nomor 2 dan 3
    print('e.sayuran nomor 2 dan 3 adalah:',sayuran[1:3])

    #f.tampilkan semua daftar nama dengan perulangan 
    print('f.Daftar sayuran dengan FOR loop:')
    for item in sayuran:
        print(item)
    
    print('f.Daftar sayuran dengan WHILE loop:')
    i = 0
    while i < len(sayuran):
        print(sayuran[i])
        i+=1

    #g.Tampilkan panjang list 
    print('g.jumlah total sayuran sekarang:',len(sayuran))

# untuk memanggil soal dalam def contoh: soal()
# soal1()
# soal2()
# soal3()
# soal4()
