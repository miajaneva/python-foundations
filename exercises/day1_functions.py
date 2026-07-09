# function = A block of reusable code place() after the function name to invoke it


print("Hello World")  # this is a function that prints "Hello World" to the console


def happy_birthday():
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print("Happy Birthday dear friend")
    print("Happy Birthday to you")

happy_birthday()  # this is a function call that invokes the happy_birthday function


# function with arguments = A block of reusable code that takes in parameters to customize its behavior
# the position of the arguments matters, the first argument will be assigned to the first parameter, the second argument will be assigned to the second parameter, and so on
def happy_birthday_with_name(name):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")
    print("Happy Birthday to you")

happy_birthday_with_name("Alice")  # this is a function call that invokes the happy_birthday_with_name function with the argument "Alice"


# function with multiple arguments = A block of reusable code that takes in multiple parameters to customize its behavior
def happy_birthday_with_name_and_age(name, age):
    print("Happy Birthday to you")
    print("Happy Birthday to you")
    print(f"Happy Birthday dear {name}")
    print(f"You are now {age} years old")
    print("Happy Birthday to you")

happy_birthday_with_name_and_age("Bob", 30)  # this is a function call that invokes the happy_birthday_with_name_and_age function with the arguments "Bob" and 30



def display_invoice(customer_name, amount_due):
    print(f"Invoice for {customer_name}")
    print(f"Amount Due: ${amount_due:.2f}")
    print("Thank you for your business!")

display_invoice("Charlie", 150.75)  # this is a function call that invokes the display_invoice function with the arguments "Charlie" and 150.75


# return statement = A statement that allows a function to send a value back to the caller
def add_numbers(num1, num2):
    return num1 + num2  # this is a return statement that sends the sum of num1 and num2 back to the caller

result = add_numbers(5, 10)  # this is a function call that invokes the add_numbers function with the arguments 5 and 10, and assigns the returned value to the variable result


print(f"The sum of 5 and 10 is {result}")


def subtract_numbers(num1, num2):
    return num1 - num2  # this is a return statement that sends the difference of num1 and num2 back to the caller

result = subtract_numbers(10, 5)  # this is a function call that invokes the subtract_numbers function with the arguments 10 and 5, and assigns the returned value to the variable result

print(f"The difference of 10 and 5 is {result}")


def multiply_numbers(num1, num2):
    return num1 * num2

result = multiply_numbers(5, 10)

print(f"The product of 5 and 10 is {result}")



def divide_numbers(num1, num2):
    return num1 / num2

result = divide_numbers(10, 5)

print(f"The quotient of 10 and 5 is {result}")



def create_name(first_name, last_name):
    first_name = first_name.capitalize()
    last_name = last_name.capitalize()
    return f"{first_name} {last_name}"

full_name = create_name("john", "doe")
print(full_name)


#default arguments = A feature that allows a function to have default values for its parameters, which can be overridden by the caller if desired
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice")  # this is a function call that invokes the greet function with the argument "Alice" and uses the default value for the greeting parameter
greet("Bob", "Hi")  # this is a function call that invokes the greet function with the arguments "Bob" and "Hi", overriding the default value for the greeting parameter



#keyword arguments = A feature that allows a function to be called with arguments specified by name, rather than by position
def greet_with_keyword_arguments(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_with_keyword_arguments(name="Alice")  # this is a function call that invokes the greet_with_keyword_arguments function with the argument "Alice" and uses the default value for the greeting parameter
greet_with_keyword_arguments(name="Bob", greeting="Hi")  # this is a function call that invokes the greet_with_keyword_arguments function with the arguments "Bob" and "Hi", overriding


# *args = A feature that allows a function to accept an arbitrary number of positional arguments, which are collected into a tuple
def greet_with_args(*args):
    for name in args:
        print(f"Hello, {name}!")

greet_with_args("Alice", "Bob", "Charlie")  # this is a function call that invokes the greet_with_args function with the arguments "Alice", "Bob", and "Charlie"




# *kwargs = A feature that allows a function to accept an arbitrary number of keyword arguments, which are collected into a dictionary
def greet_with_kwargs(**kwargs):
    for name, greeting in kwargs.items():
        print(f"{greeting}, {name}!")

greet_with_kwargs(Alice="Hello", Bob="Hi", Charlie="Hey")  # this is a function call that invokes the greet_with_kwargs function with the keyword arguments Alice="Hello", Bob="Hi", and Charlie="Hey"


def student_info(*kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_info(name="Mia", age=25, major="Computer Science") # this is a function call that invokes the student_info function with the keyword arguments name="Mia", age=25, and major="Computer Science"



def calculate_average(*args):
    total = sum(args)
    count = len(args)
    return total / count

average = calculate_average(10, 20, 30)
print(f"The average of 10, 20, and 30 is {average}")

def create_profile(*kwargs):
    profile = {}
    for key, value in kwargs.items():
        profile[key] = value
    return profile

profile = create_profile(name="John", age=30, city="New York")
print(profile)

def discount(price, percentage=10):
    return price - (price * (percentage / 100))

discounted_price = discount(100)  # uses default percentage of 10%
print(f"The discounted price is ${discounted_price:.2f}")




















