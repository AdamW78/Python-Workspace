def area(width, height):
    return int(width)*int(height)


def perimeter(width, height):
    return int(width) + int(height)


def main(width, height):
    print(f"Perimeter of rectangle: {perimeter(width, height)}")
    print(f"Area of rectangle: {area(width, height)}")


main(input("Input width of the rectangle: "), input("Input height of the rectangle: "))
