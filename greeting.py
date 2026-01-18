import sys

if len(sys.argv) == 2:
    celsius = float(sys.argv[1])
else:
    celsius = 25

fahrenheit = (celsius * 9/5) + 32
print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
