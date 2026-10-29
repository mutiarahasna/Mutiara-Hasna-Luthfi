#import konversi as kv
#import konversi
import paket.konversi as kvr
# from konversi import CtoR, CtoF, CtoK

# celcius = 100
celcius = float(input("Masukkan suhu dalam Celcius: "))
reamur = kvr.CtoR(celcius)
fahrenheit = kvr.CtoF(celcius)
kelvin = kvr.CtoK(celcius)

reamur = CtoR(celcius)
fahrenheit = CtoF(celcius)

print(f"{celcius} derajat Celcius = {celcius} derajat Celcius")
print(f"{celcius} derajat Celcius = {reamur} derajat Reamur")
print(f"{celcius} derajat Celcius = {fahrenheit} derajat Fahrenheit")
#print(f"{celcius} derajat Celcius = {kelvin} derajat Kelvin")