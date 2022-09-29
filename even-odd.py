# Summation Variables
even_sum = 0
odd_sum = 0
# Numbers to add to sum - updated  by +2 each iteration
e = 2
o = 1

while e <= 100:
    even_sum += e
    e += 2
    odd_sum += o
    o += 2
if even_sum > odd_sum:
    print("The sum of the even numbers is greater than the sum of the odd numbers.")
else:
    print("The sum of the odd numbers is greater than the sum of the even numbers.")
print(f"The difference between the even and odd numbers is {(odd_sum-even_sum).__abs__()}")

