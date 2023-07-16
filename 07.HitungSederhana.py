#konfrensi satuan temperatur

#input celcius
suhu = float(input("masukkan suhu celcius : "))
print("suhu ",suhu, " celcius")

#celcius ke reamur
reamur = (4/5) * suhu
print(reamur)

#reamur ke celcius
celcius = (5/4) * reamur
print(celcius)

#celcius ke fahrenhait
fahrenhait = (9/5) * (celcius + 32)
print(fahrenhait)

#fahrenhait ke celcius 
celcius = (5/9) * (fahrenhait - 32)
print(celcius)

#celcius ke kelvin
kelvin = celcius + 273
print(kelvin)

#kelvin ke celcius
celcius = kelvin - 273
print(kelvin)

#kelvin ke reamur
reamur = (4/5) * ( kelvin - 273 )
print(reamur)



