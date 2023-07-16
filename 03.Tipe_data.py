#integer
data_integer = 1
print("data : ", data_integer, "bertipe" , type(data_integer))

#float(koma)
data_float= 33,3
print("data",data_float, type(data_float))

#boolean(true,false)
data_bool= False
print("datanya", data_bool , type(data_bool))

#data komplex
data_complex = complex(5,6)
print("data",complex)

#tipe data dari c (bool,char,string dll)
from ctypes import c_double
data_c_double = c_double(10.5)
print("data", data_c_double)
print("tipe datanya", type(data_c_double))