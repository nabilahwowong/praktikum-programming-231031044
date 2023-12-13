print ('praktikum-3\n')
print('nama lengkap: nabilah ramadhani wowong')
print('nim         : 231031044')
print('prodi       : sistem informasi')

print ()
a = True 
b = False 

print ('\n=============NAND===============')
print ()
hasil =  not (a and a)
print (a, 'nand', a, 'adalah=', hasil)
hasil = not (a and b) 
print (a, 'nand', b, 'adalah=', hasil )
hasil = not  (b and a) 
print (b, 'nand', a, 'adalah=', hasil)
hasil = not (b and b) 
print (b, 'nand', b, 'adalah=', hasil )

print ('\n==================NOR=============')
print ()
hasil =  not (a or a)
print (a, 'nor', a, 'adalah=', hasil)
hasil = not (a or b) 
print (a, 'nor', b, 'adalah=', hasil )
hasil = not  (b or a) 
print (b, 'nor', a, 'adalah=', hasil)
hasil = not (b or b) 
print (b, 'nor', b, 'adalah=', hasil )

print ('\n==================NXOR=============')
print ()
hasil =  not (a ^ a)
print (a, 'nxor', a, 'adalah=', hasil)
hasil = not (a ^ b) 
print (a, 'nxor', b, 'adalah=', hasil )
hasil = not  (b ^ a) 
print (b, 'nxor', a, 'adalah=', hasil)
hasil = not (b ^ b) 
print (b, 'nxor', b, 'adalah=', hasil )

# ini operator membership 
print ('==================IN=================')
print ()
nama = ('nabilah')

test = 'na'
cek = test in nama 
print (test, 'ada di', nama,'adalah=', cek)

print ()
test = 'an'
cek = test in nama 
print (test, 'ada di', nama,'adalah=', cek)

print ()
test1 = 'a'
test2 = 'i' 
test3 = 'u' 
test4 = 'e'
test5 = 'o' 

print ()
cek = test1 in nama 
print (test1, 'ada di', nama,'adalah=', cek)
print ()
cek = test2 in nama 
print (test2, 'ada di', nama,'adalah=', cek)
print ()
cek = test3 in nama 
print (test3, 'ada di', nama,'adalah=', cek)
print ()
cek = test4 in nama 
print (test4, 'ada di', nama,'adalah=', cek)
print ()
cek = test5 in nama 
print (test5, 'ada di', nama,'adalah=', cek)

print ()
cek = not (test1 in nama) 
print (test1, 'tidak ada di', nama,'adalah=', cek)
print ()
cek = not (test2 in nama) 
print (test2, 'tidak ada di', nama,'adalah=', cek)
print ()
cek = not (test3 in nama) 
print (test3, 'tidak ada di', nama,'adalah=', cek)
print ()
cek = not (test4 in nama) 
print (test4, 'tidak ada di', nama,'adalah=', cek)
print ()
cek = not (test5 in nama) 
print (test5, 'tidak ada di', nama,'adalah=', cek)

# ini operator BITWISE 
print ('\n')
a = 29 #tanggal lahir 
b = 10 #bulan lahir 
a+= 60 
b+= 80 
print ()
print ('===============AND==============')
print ('nilai', a, 'biner adalah=', format(a,'08b'))
print ('nilai',b, 'biner adalah=', format(b,'08b'))
print ()
print ('----------------------AND')
c = a & b 
print ('nilai', a, '&', b, 'biner adalah=', format(c, '08b'))
print ()
print ('===============AND==============')
print ('nilai', a, 'biner adalah=', format(a,'10b'))
print ('nilai',b, 'biner adalah=', format(b,'10b'))
print ()
print ('----------------------AND')
c = a & b 
print ('nilai', a, '&', b, 'biner adalah=', format(c, '10b'))
print ('nilai', a, '&', b, 'biner adalah=', format(c, '10b'))

print ()
print ('===============AND==============')
print ('nilai', a, 'biner adalah=', format(a,'09b'))
print ('nilai',b, 'biner adalah=', format(b,'09b'))
print ()
print ('----------------------AND')
c = a & b 
print ('nilai', a, '&', b, 'biner adalah=', format(c, '09b'))

print ('\n==========OR===========')
print ('nilai', a, 'biner  adalah=', format (a, '09b'))
print ('nilai', b, 'biner adalah', format (b, '09b'))
c = a | b 
print ('nilai', a, 'nor', b, 'biner adalah=', format(c, '09b'))

print ('\n===========xor=========')
print ('nilai', a, 'biner adalah=', format (a, '09b'))
print ('nilai', b, 'biner adalah=', format (b, '09b'))
c = a ^ b 
print ('nilai', a, 'xor', b, 'biner adalah=', format (c, '09b'))

print ('\n============not=========')
c = ~a
print ('nilai', a, 'biner adalah=', format(c,'09b'))
print ('nilai not', a, 'biner adalah=', format(c,'09b'))
c = ~b 
print ('nilai', b, 'biner adalah=', format(c,'09b'))
print ('nilai not', b, 'biner adalah=', format(c,'09b'))

print ('\n=============left shift===========')
c = a << 2 
print ('nilai', a, 'biner adalah=', format(a,'09b'))
print ('nilai', a, '<< 2 biner adalah=', format(a,'09b'))
print ()
c = b << 2 
print ('nilai', b, 'biner adalah=', format(a,'09b'))
print ('nilai', b, '<< 2 biner adalah=', format(a,'09b'))

print ()
print ('\n=============right shift===========')
c = a >> 2 
print ('nilai', a, 'biner adalah=', format(a,'09b'))
print ('nilai', a, '>> 2 biner adalah=', format(a,'09b'))
print ()
c = b >> 2 
print ('nilai', b, 'biner adalah=', format(a,'09b'))
print ('nilai', b, '>> 2 biner adalah=', format(a,'09b'))

print ()
print ('===============NOT AND==============')
print ('nilai', a, 'biner adalah=', format(a,'09b'))
print ('nilai',b, 'biner adalah=', format(b,'09b'))
print ()
c = ~(a & b )
print ('nilai', a, 'nand', b, 'biner adalah=', format(c, '09b'))

print ('\n==========NOT OR===========')
print ('nilai', a, 'biner  adalah=', format (a, '09b'))
print ('nilai', b, 'biner adalah', format (b, '09b'))
c = ~ (a | b )
print ('nilai', a, 'nor', b, 'biner adalah=', format(c, '09b'))

print ('\n=========== NOT XOR=========')
print ('nilai', a, 'biner adalah=', format (a, '09b'))
print ('nilai', b, 'biner adalah=', format (b, '09b'))
c = ~(a ^ b) 
print ('nilai', a, 'nxor', b, 'biner adalah=', format (c, '09b'))

print ('\n=============NOT left shift===========')
c = ~ (a << 2)
print ('nilai', a, 'biner adalah=', format(a,'09b'))
print ('nilai', a, 'not','<< 2 biner adalah=', format(a,'09b'))
print ()
c = ~ (b << 2) 
print ('nilai', b, 'biner adalah=', format(a,'09b'))
print ('nilai', b, 'not', '<< 2 biner adalah=', format(a,'09b'))

print ('\n=============NOT right shift===========')
c = ~ (a >> 2) 
print ('nilai', a, 'biner adalah=', format(a,'09b'))
print ('nilai', a, 'not', '>> 2 biner adalah=', format(a,'09b'))
print ()
c = ~(b >> 2) 
print ('nilai', b, 'biner adalah=', format(a,'09b'))
print ('nilai', b, 'not','>> 2 biner adalah=', format(a,'09b'))