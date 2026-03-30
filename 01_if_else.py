my_age = 17

# if function
if my_age > 18:
    print("Adult")

# if else
if my_age > 18:
    print("Adult")
else:
    print("Minor")

# if elif else
if my_age > 18:
    print("Adult")
elif my_age == 18:
    print("Turing Adult")
else:
    print("Minor")

# 
my_age = 19.0
msg = "Non Integer"
if isinstance(my_age, int):
    msg = "Integer"
print(msg)