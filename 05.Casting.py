#casting ( merubah ke tipedata lain)
data_integer = 80
print("datanya ",  data_integer, type(data_integer))

#to CAST

#float
data_float = float(data_integer)
print(data_float)

#string
data_string= str(data_integer)
print(data_string)

#boolean
data_boolean = bool(data_integer)
print(data_boolean)

#complex
data_complex = complex(data_boolean,data_integer)
print(data_complex)

