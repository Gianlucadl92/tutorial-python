def my_function(n): 
    return lambda a : a * n

my_doubler = my_function(2)
print(my_doubler(11))