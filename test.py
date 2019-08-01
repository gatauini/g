# meminta input dari user

angka = int(input("Masukkan angka: "))

# mengecek bilangan prima selalu lebih besar dari 1

if angka > 1:

   # mengecek faktor pembagi dengan operasi modulus

   for i in range(2,angka):
       if (angka % i) == 0:
           print ("\033[91m",angka,"bukan bilangan prima")
       
           break
   else:
       print ("\033[92m",angka,"adalah bilangan prima")

# keluaran jika sebuah bilangan kurang dari atau sama dengan 1

else:
   print ("\033[91m",angka,"bukan bilangan prima")