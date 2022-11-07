x=int(input("Masukkan modal usaha :"))
a=0*x
b=0*x
c=0.1*x
d=0.1*x
e=0.5*x
f=0.5*x
g=0.5*x
h=0.3*x
j=[a,b,c,d,e,f,g,h]
for i in range (len(j)):
    print("laba bulan ke:",i+1,"sebesar :",j[i])
k = (a+b+c+d+e+f+g+h)
print("total laba:",k)
