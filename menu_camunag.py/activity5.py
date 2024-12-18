print("FAHRENHEIT TO CELSIUS CONVERTER PROGRAM " )

print("====================================== ")

fahrenheit = eval(input("Enter temperature in Fahrenheit ---> :      "))

celsius = ((fahrenheit - 32 ) * 5) / 9

print(fahrenheit, "degrees Fahrenheit converted to celsius is" , celsius, "degrees")

print(f" {fahrenheit}degrees Fahrenheit converted to celsius is {celsius} degrees")

print(round(celsius, 2))

print(f" {fahrenheit}degrees Fahrenheit converted to celsius is {round(celsius, 2)} degrees")
