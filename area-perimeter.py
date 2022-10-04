import random


def area(width, height):
    return width*height


def perimeter(width, height):
    return width+height


def main(width, height):
    print(f"Perimeter of rectangle: {perimeter(width, height)}")
    print(f"Area of rectangle: {area(width, height)}")


for i in range(3):
    main(random.randint(1, 100), random.randint(1, 100))
