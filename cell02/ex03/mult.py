n1 = int(input("Enter the first number:\n"))
n2 = int(input("Enter the second number:\n"))

mult = n1 * n2

print(n1, "x", n2, "=", mult)

if (mult < 0):
    print("The result is negative.")

elif (mult > 0):
    print("The result is positive.")

elif (mult == 0):
    print("The result is both negative and positive.")
