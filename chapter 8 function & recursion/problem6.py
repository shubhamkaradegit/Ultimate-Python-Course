#wirte function to convert inches to centimeters

def inch_to_cm(inch):
    return inch * 2.54

inch = float(input("Enter the length in inches: "))

print("Length in centimeters: ", inch_to_cm(inch))