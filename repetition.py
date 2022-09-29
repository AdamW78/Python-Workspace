import keyboard

for counter in range(10):
    print(counter+1)
while 2 > 10:
    i = 0
    print(i)
    i += 1
i = 0
print("Would you like to run an infinite loop? Press q at any time to quit once initiated.")
infinite = input("Please enter \"yes\" (\"y\") or \"no\" (\"n\")\n").casefold()
loopinfinite = False
if infinite == "y" or infinite == "ye" or infinite == "yes":
    loopinfinite = True
elif infinite != "n" or infinite != "no":
    print("Error: unable to parse your response, skipping infinite loop")
while loopinfinite:
    try:
        if keyboard.read_key() == 'q':
            loopinfinite = False
            break
    except:
        loopinfinite = False
        break
    print(i)
    i += 1
counter = 1
while counter <= 12:
    print (counter)
    counter += 1