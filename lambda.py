def my_multiplier(n):
    return lambda x: x * n

double = my_multiplier(2)
print(double(5))  