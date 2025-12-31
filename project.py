#UNIT CONVERTER FROM any another to another
def meter_to_kilometer(meter):
    Km=meter/1000
    print(meter, " meters =", Km, "kilometers")

def meter_to_yards(meter):
    yards = meter * 1.09361
    print(meter, " meters =", yards, "yards")

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print(celsius, " Celsius =", fahrenheit, "Fahrenheit")

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    print(celsius, " Celsius =", kelvin, "Kelvin")

def kilogram_to_grams(kg):
    grams = kg * 1000
    print(kg, " kilograms =", grams, "grams")

def kilogram_to_pounds(kg):
    pounds = kg * 2.20462
    print(kg, " kilograms =", pounds, "pounds")

def liters_to_milliliters(liters):
    milliliters = liters * 1000
    print(liters, " liters =", milliliters, "milliliters")

def liters_to_gallons(liters):
    gallons = liters * 0.264172
    print(liters, " liters =", gallons, "gallons")

def kilometers_to_miles(km):
    miles = km * 0.621371
    print(km, " kilometers =", miles, "miles")

def USD_to_INR(USD):
    inr = USD * 90
    print(USD, " USD =", inr, "INR")

def EURO_to_INR(EURO):
    INR = EURO * 100
    print(EURO, " EURO =", INR, "INR")

def joules_to_calories(joules):
    calories = joules * 0.239006
    print(joules, " joules =", calories, "calories")

def watts_to_horsepower(watts):
    horsepower = watts * 0.00134102
    print(watts, " watts =", horsepower, "horsepower")

def pascal_to_atmosphere(pascal):
    atmosphere = pascal * 9.86923e-6
    print(pascal, "pascals =", atmosphere, "atmospheres")

def bar_to_psi(bar):
    psi = bar * 14.5038
    print(bar,"bar=",psi,"psi")

def JPY_to_INR(JPY):
    INR = JPY * 0.67
    print(JPY,"YEN=", INR,"Indian Rupees")

def RUB_to_INR(RUB):
    INR = RUB * 1.12
    print(RUB,"Russian Ruble",INR,"Indian Rupees")

#CALLING OUT ALL THE FUNCTIONS 
meter_to_kilometer(5000)
meter_to_yards(1000)
celsius_to_fahrenheit(37)
celsius_to_kelvin(25)
kilogram_to_grams(5)
kilogram_to_pounds(10)
liters_to_milliliters(3)
liters_to_gallons(3)
kilometers_to_miles(10)
USD_to_INR(100)
EURO_to_INR(50)
joules_to_calories(500)
watts_to_horsepower(1000)
pascal_to_atmosphere(1000)
bar_to_psi(2)
JPY_to_INR(1000)
RUB_to_INR(1000)

print("Thank You")
