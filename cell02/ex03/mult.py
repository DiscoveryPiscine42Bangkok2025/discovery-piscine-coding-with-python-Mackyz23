firstnumber = int(input("Enter the first number: "))
secondnumber = int(input("Enter the second number: "))
if firstnumber * secondnumber ==0 :
    print("This number is both positive and negative.")
elif firstnumber * secondnumber < 0:
    print("This number is negative.")
elif firstnumber * secondnumber > 0:
    print("This number is positive.")