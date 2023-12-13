pendapatan = int(input('pendapatan:'))

if pendapatan> 5001:
    presentase = 50

elif pendapatan > 4000:
    presentase = 40 

elif pendapatan >3000:
    presentasi = 20 

elif pendapatan >2000:
    presentasi = 20

elif pendapatan >1000:
    presentase = 10

else : 
    presentase = 10 

bonus = pendapatan*(presentase/100)
total_pendapatan = pendapatan + bonus 

print ('pendapatan', pendapatan)
print ('pendapatan', presentase)
print ('bonus', bonus)
print ('total pendapatan', total_pendapatan)