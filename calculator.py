# Python Calculator Project

print("==== WELCOME TO PYTHON CALCULATOR ====")

 
# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


# Display Operations
print("\nSelect Operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Divition (/)")


# Take choice from user 
choice = input("Enter your choice (1/2/3/4):")


# Perform calculator
if choice == "1":
    result = num1 + num2
    print("Addition:", result)

elif choice == "2":
    result = num1 - num2
    print("Subtraction:", result)

elif choice == "3":
    result = num1 * num2
    print("Multiplication:", result)

elif choice == "4":
    if num2 !=0:
        result = num1 / num2
        print("Divition:", result)
    else:
        print("Enter: Cannot divide by zero!")

else:
    print("Invalid choice! Please select 1, 2, 3, or 4.")
    


