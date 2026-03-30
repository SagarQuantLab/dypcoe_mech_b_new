# sample for loop
for i in range(0, 5, 2):
    print(i)

# for loop
my_string = "students"

# call each element of string
for i in my_string:
    print(i)

# call each index of string
for i in range(len(my_string)):
    print(i)

# call index and value together
for i, each_char in enumerate(my_string):
    print(i, each_char)


my_list = ["Apple", "banana", "Mango"]
for each in my_list:
    print(each)

for i, each in enumerate(my_list):
    print(i, each)

for i in range(len(my_list)):
    print(my_list[i])


my_dict = {
    "Name": "Rohan",
    "Age": 35,
    "Gender": "Male"
}

# print each key
for each_key in my_dict.keys():
    print(each_key)

# print each value
for each_value in my_dict.values():
    print(each_value)

# print both keys and value
for each_key in my_dict.keys():
    print(each_key, my_dict[each_key])

for each_k_v in my_dict.items():
    print(each_k_v)