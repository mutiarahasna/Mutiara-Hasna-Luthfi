import statistics as stats

def CtoR(celcius):
    reamur = celcius * 4/5
    return reamur

def CtoF(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit

def CtoK(celcius):
    kelvin = celcius + 273.15
    return kelvin


def main ():
    print (__name__)
    celcius = 100
    print(f"{celcius} derajat Celcius = {celcius} derajat Celcius")
    print(f"{celcius} derajat Celcius = {CtoR(celcius)} derajat Reamur")

if __name__ == "__main__":
    main()

    # print(f"{celcius} derajat Celcius = {reamur} derajat Reamur")
    # print(f"{celcius} derajat Celcius = {fahrenheit} derajat Fahrenheit")
    # print(f"{celcius} derajat Celcius = {kelvin} derajat Kelvin")