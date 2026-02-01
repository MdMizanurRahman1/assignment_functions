#3
#Write a function that gets the quantity of gasoline in American gallons
# and returns the number converted to litres.
# Write a main program that asks for a volume in gallons from the user
# and converts the value to liters. The conversion must be done by using the function.
# Conversions continue until the user inputs a negative value.

def american_gasoline(gallons):
    return gallons*3.78541
#print(american_gasoline(100))

user=float(input("Enter a volumn in gallons: "))

while user >=0:
    conversion = american_gasoline(user)
    print(f"{conversion:.3f}", "liters of gasoline")
    user=float(input("Enter a volumn in gallons: "))

