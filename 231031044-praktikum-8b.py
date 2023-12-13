import os 
os.system ('cls')

pwd_benar='si23b'
a = True
i = 0 
limit =  3
while a:
    i += 1
    pwd = input ('Masukan Pasword: ')
    if pwd == pwd_benar:
        print('selamat anda login!')
        a = False

    else:
        if i == limit: 
            a = False 
            print('anda kehabisan kesempatan')
        else: 
            print ('password salah, coba lagi') 
            print (f'kesempatan anda tersisa {limit-1} kali')