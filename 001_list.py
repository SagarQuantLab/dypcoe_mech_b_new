#LIST
# [], index, Mutable, duplicate, ordered

my_list = [3, 4, 2, 1, 3]

# access first element
print(my_list[0])

# first two element access
print(my_list[0:2])

# access first three element with gap 2
print(my_list[0:3:2])

# last element
print(my_list[-1])

# reverse list
reversed_list = my_list.reverse()
print(my_list)

# replace in list
my_list[0] = 300
print(my_list)

# sort list
my_list.sort()
print(my_list)