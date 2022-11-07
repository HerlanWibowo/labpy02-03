a = int(input("Masukkan bilangan ke-1 :"))
b = int(input("Masukkan bilangan ke-2 :"))
c = int(input("Masukkan bilangan ke-3 :"))

if (a<b<c):
    print("bilangan yg terbesar :",c)
elif (a<c<b):
    print("bilangan yg terbesar :",b)
else :
    print("Bilangan yg terbesar :",a)