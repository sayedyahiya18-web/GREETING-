import sys
if len(sys.argv) > 1:
    celsius = float(sys.argv[1]) 
    print("User provided temperature:") 
else:
    celsius = 25  
    print("No input given - using default temperature:")
fahrenheit = (celsius * 9/5) + 32
print("Script Name:", script_name) print("Celsius:", celsius) print("Fahrenheit:", fahrenheit)
