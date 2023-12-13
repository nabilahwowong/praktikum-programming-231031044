import os 
os.system ('cls')

a = True

while a: 
    jawab = input ('apakah ingin lanjutkan? (y/n)')
    if jawab == 'y': 
        os.system ('cls')
        print ('selamat datang lagi!')
        a = True 
    elif jawab == 'n':
        a = False 
        print ('sampai ketemu lagi:D')
    else: 
        print ('jangan aneh deh bjir')
        a = True 