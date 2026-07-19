print("=== Exception Handling Practice ===")

try:
    age = int(input("Enter your age: "))

    if age < 0:
        print("Age cannot be negative.")
    else:
        print(f"You are {age} years old.")

except ValueError:
    print("Please enter a valid number.")