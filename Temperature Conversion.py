def CtoF(celsius):
    return (celsius * 9/5) + 32

def FtoC(fahrenheit):
    return (fahrenheit - 32) * 5/9

def temperature_converter():
  
    temp = float(input("Enter the temperature value: "))
    conversion_unit = input("Enter the unit to convert into (F for Fahrenheit C for Celsius) ").upper()

   
    if conversion_unit == 'F':
        converted_temperature = CtoF(temp)
        print(f"{temp} degrees Celsius is {converted_temperature:.2f} degrees Fahrenheit.")
    elif conversion_unit == 'C':
        converted_temperature = FtoC(temp)
        print(f"{temp} degrees Fahrenheit is {converted_temperature:.2f} degrees Celsius.")
    else:
        print("Invalid unit of measurement. Please enter 'C' for Celsius or 'F' for Fahrenheit.")

temperature_converter()

