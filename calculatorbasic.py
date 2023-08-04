# making calculator using simple method

# input first number
first_number=float(input("enter first number; "))

#input operator
operator=input("enter operator(+,-,*,/); ")

#input second number
second_number=float(input("enter secound number; "))

# enter condition and print accordingly
if operator== "+":
    print(first_number + second_number)

elif operator== "-":
    print(first_number - second_number)

elif operator== "*":
    print(first_number * second_number)


elif operator=="/":
    print(first_number / second_number)

else:
    print("invalid opperation")

