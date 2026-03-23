# STRING SLICING
my_string = "Hello this is mechanical students"

# access first letter
print(my_string[0])

# access 'hello'
print(my_string[0:5])

# access 'Hlo'
print(my_string[0:5:2])

# last letter of string
print(my_string[-1])

# reverse string
print(my_string[::-1])

# access student in reverse
print(my_string[:-9:-1])

# upper case
print(my_string.upper())

# lower case
print(my_string.lower())

# replace
updated_string= my_string.replace("s", "X")
print(updated_string)