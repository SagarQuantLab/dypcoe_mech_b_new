## function normal syntax

# def my_function():
#     pass

def my_decorator(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise ValueError(f"First num should be integer, but passed '{args[0]}'")
        if not isinstance(args[1], int):
            raise ValueError(f"Second num should be integer, but passed '{args[1]}'")
        

        if len(kwargs) > 0:
            key_list = list(kwargs.keys())
            if not isinstance(kwargs[key_list[0]], int):
                raise ValueError(f"C should be integer, but passed '{kwargs[key_list[0]]}'")
            if not isinstance(kwargs[key_list[1]], int):
                raise ValueError(f"D should be integer, but passed '{kwargs[key_list[1]]}'")
        else:
            kwargs.setdefault('c', 0)
            kwargs.setdefault('d', 0)
        
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def addition(first_num, second_num, c=0, d=0):
    sum = first_num + second_num + c + d
    return sum

sum_num = addition(2,3)
#sum_num = addition(2, 'b')
sum_num = addition(2, 3, c=4, d = 5)

#sum_num = addition(2, 3, c='c', d=5)
print(sum_num)