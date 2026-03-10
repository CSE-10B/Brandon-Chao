# Celsius to Fahrenheit
c = float(input("Enter temperature in Celsius: "))
f = (c * 9/5) + 32
print(c, "°C is", int(f), "in Fahrenheit")                  #takes user input in the form of a float in celcius and converts it to farenheit. 

# Fahrenheit to Celsius
f = float(input("Enter temperature in Fahrenheit: "))#reverses the process by requesting a user input in farenheit and converts it to celcius.
c = (f - 32) * 5/9
print(f, "°F is", int(c), "in Celsius")