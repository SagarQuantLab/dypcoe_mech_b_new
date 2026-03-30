# DICT
# {}, keys, Mutable, No-duplicate, ordered

my_dict = {
    "Name" : "Rohan",
    "Age" : 35,
    "Gender": "Male",
    "Name": "Sohan"
}

# access name
print(my_dict["Name"])

# access all keys
print(my_dict.keys())

# access values
print(my_dict.values())

# No duplicates allowed (will update value)
print(my_dict)

# change value
my_dict["Gender"] = "Female"
print(my_dict)

# {}, keys, Mutable, No-duplicate, ordered
################################################
# Items     Symbol     Calling       Mutable       Duplicates      Ordered
# List        []        Index           Y               Y            Y
# Dict        {}        Keys            Y               N            Y
# Tuple       ()        Index           N               Y            Y
# Set         {}        -               N               N            N