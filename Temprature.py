while True:
    temp = input("Choose the unit to change into :\n 1.Fahrenheit(f)\n 2.Celsius(c)\n 3.from Celsius to Kelvin(c to k)\n 4.from Fahrenheit to Kelvin(f to k)\n 5.Quit(q)\n")

    if temp == "f":
        c = float(input("Enter Teprature : "))
        f = 9*c/5+32
        print("The Temprature is : {} F".format(f))

    elif temp == "c":
        f = float(input("Enter Teprature : "))
        c = 5*(f-32)/9
        print("The Temprature is : {} C".format(c))

    elif temp == "c to k":
        c = float(input("Enter Teprature in Celsius : "))
        Kelvin = c+273
        print("The Temprature is : {} K".format(Kelvin))

    elif temp == "f to k":
        f = float(input("Enter Teprature in Fahrenheit : "))
        c = 5*(f-32)/9
        kelvin = c+273
        print("The Temprature is : {} K".format(kelvin))
     
    elif temp == "q":
        break
