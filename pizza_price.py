#6
import math


def main(diameter, price):
    radius=(diameter/2)/100   #converted in meters
    area_of_pizza=math.pi* radius**2
    unit_price=price/area_of_pizza
    return unit_price    #square meters

diameter1=float(input("enter the diameter of a pizza 1:"))
price1=float(input("enter the price of a pizza 1:"))
diameter2=float(input("enter the diameter of a pizza 2:"))
price2=float(input("enter the price of a pizza 2:"))

price_for_pizza1=main(diameter1,price1)
price_for_pizza2=main(diameter2,price2)

if price_for_pizza1<price_for_pizza2:
    print(f"The price of pizza 1 is {price_for_pizza1:.2f} and has better value")
elif price_for_pizza1>price_for_pizza2:
    print(f"The price of pizza 2 is {price_for_pizza2:.2f} and has better value")





