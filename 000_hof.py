def increment(x):
    return x + 1

increment_v2 = lambda x: x + 1

def high_ord_func(x, func):
    return x + func(x)

high_ord_func_2 = lambda x, func: x + func(x)

result = high_ord_func(2, increment)
print(result)

result_v2 = high_ord_func_2(2, increment_v2)
print(result_v2)