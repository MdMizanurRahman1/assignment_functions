#2
import random
def main(sides):
    return random.randint(1, sides)

result=0
max_sides=int(input("Enter the max sides: "))

while result != max_sides:
    result=main(max_sides)
    print(result)
