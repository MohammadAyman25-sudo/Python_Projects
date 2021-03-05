while True:
    temp = input("Choose the unit to change into :\n 1.Fahrenheit(f)\n 2.Celsius(c)\n 3.from Celsius to Kelvin(c to k)\n 4.from Fahrenheit to Kelvin(f to k)\n 5.Quit(q)\n")

    if temp == "f":
        c = float(input("Enter Teprature : "))
        f = 9*c/5+32
        print(f"The Temprature is : {f} F")

    elif temp == "c":
        f = float(input("Enter Teprature : "))
        c = 5*(f-32)/9
        print(f"The Temprature is : {c} C")

    elif temp == "c to k":
        c = float(input("Enter Teprature in Celsius : "))
        Kelvin = c+273
        print(f"The Temprature is : {k} K")

    elif temp == "f to k":
        f = float(input("Enter Teprature in Fahrenheit : "))
        c = 5*(f-32)/9
        kelvin = c+273
        print(f"The Temprature is : {k} K")
     
    elif temp == "q":
        break
