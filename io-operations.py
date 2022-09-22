userAge = input("Please enter your age: ")
print("In 1 year, you will be:", end = ' ')
try:
    int(userAge)
except ValueError:
    try:
        float(userAge)
    except ValueError:
        print("Error: Please enter your age as a number")
    else:
        print(float(userAge)+1.0)
else:
    print(int(userAge)+1)