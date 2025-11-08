#James Van Dyk
#4.2
#small and/or green

choice = str(input("Enter one choice of: cherry, pea, watermelon, pumpkin. "))

if choice == "cherry" or choice == "pea":
    small = True
else:
    small = False

if choice == "pea" or choice == "watermelon":
    green = True
else:
    green = False

print("Small =", small)
print("Green =", green)