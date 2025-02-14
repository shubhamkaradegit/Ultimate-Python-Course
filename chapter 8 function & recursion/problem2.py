def ctof(c):
    return (c*9/5) + 32

c = int(input("Enter temperature in Celsius: "))

print("Temperature in Fahrenheit is: ", ctof(c))

def ftoc(f):
    return (f-32) * 5/9

f = int(input("Enter temperature in Fahrenheit: "))
print("Temperature in Celsius is: ", ftoc(f))