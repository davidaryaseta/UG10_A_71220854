print ('===== Selamat di Toko Andi Tersenyum,selamat belanja! =====')
a= int(input('Total belanja :Rp'))

#diskon
ss = int(a*(2/100))
sl = int(a*(5/100))
sst = int(a*(10/100))
print(a - sl)

if a < 100000 :
    print('Tidak ada diskon! Maka yang Anda bayarkan adalah : Rp.',a')
if a >= 100000 and total <=500000:
    print('biaya yang harus dibayar setelah diskon adalah :Rp.', a-ss')
elif total>= 500000 and a  <= 1000000 :
    print('biaya yang harus dibayar setelah diskon adalah : Rp.',a-sl)
elif a 
