# comprehensions

# List comprehension 

squares = [number ** 2 for number in range(10)]
print(squares)


numbers = [1, 2, 3, 4, 5]

doubled_numbers = [number * 2 for number in numbers]
print(doubled_numbers)


even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)



number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = [number for number in number if number % 2 == 0]
print(evens)

odds = [number for number in number if number % 2 == 1]
print(odds)



# strings = [character for character in "Hello, World!"]

names = ["Alice", "Bob", "Charlie", "David"]
uppercase_names = [name.upper() for name in names]
print(uppercase_names)


lowercase_names = [name.lower() for name in names]
print(lowercase_names)



# dictionary comprehension = A concise way to create dictionaries using a single line of code, similar to list comprehensions

name_lengths = {name: len(name) for name in names}
print(name_lengths)

squares = {number: number ** 2 for number in range(10)}
print(squares)


# set comprehension = A concise way to create sets using a single line of code, similar to list comprehensions

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unique_squares = {number ** 2 for number in numbers}
print(unique_squares)


# squares 1-20
squares = [number **2 for number in range(20)]
print(squares)

# even numbers from 1-50
even = [number for number in range (1,51) if number % 2 == 0]
print(even)

# odd numbers from 1-50
odd = [number for number in range(1,51) if number % 2 == 1]
print(odd)

# uppercase names

names = ["Alice", "Bob", "Charlie", "David"]
uppercase_name = [name.upper() for name in names]
print(uppercase_name)

# dictionary squares
squares_dict = {number: number**2 for number in range(1,100)}
print(squares_dict)

# remove duplicates set comprehension
numbers = [1, 2, 2, 3, 4, 4, 5, 5]
unique = {number for number in numbers}
print(unique)
