#Menghitung Suhu Fahrenheit ke Celcius
def FtoC(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius  

#Contoh pemanggilan fungsi
suhu_fahrenheit = 86
suhu_celsius = FtoC(suhu_fahrenheit)
print(f"Suhu dalam Celsius: {suhu_celsius}")


#Menghitung Suhu Celcius ke Fahrenheit
def CtoF(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

#Contoh pemanggilan fungsi
suhu_celsius = 30
suhu_fahrenheit = CtoF(suhu_celsius)
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit}")


#Menghitung Suhu Fahrenheit ke Reamur
def FtoR(fahrenheit):
    reamur = (fahrenheit - 32) * 4/9
    return reamur   

#Contoh pemanggilan fungsi
suhu_fahrenheit = 86
suhu_reamur = FtoR(suhu_fahrenheit)
print(f"Suhu dalam Reamur: {suhu_reamur}")  


#Menghitung Suhu Reamur ke Fahrenheit
def RtoF(reamur):
    fahrenheit = (reamur * 9/4) + 32
    return fahrenheit

#Contoh pemanggilan fungsi
suhu_reamur = 24
suhu_fahrenheit = RtoF(suhu_reamur)
print(f"Suhu dalam Fahrenheit: {suhu_fahrenheit}")


#Menghitung Suhu Celcius ke Reamur
def CtoR(celsius):
    reamur = celsius * 4/5
    return reamur

#Contoh pemanggilan fungsi
suhu_celsius = 30
suhu_reamur = CtoR(suhu_celsius)
print(f"Suhu dalam Reamur: {suhu_reamur}")


#Menghitung Suhu Reamur ke Celcius
def RtoC(reamur):
    celsius = reamur * 5/4
    return celsius

#Contoh pemanggilan fungsi
suhu_reamur = 24
suhu_celsius = RtoC(suhu_reamur)
