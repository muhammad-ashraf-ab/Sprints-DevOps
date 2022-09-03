def __list_mean(even_nums):
    return sum(even_nums) / len(even_nums)
    
    
def __float_max(floats):
    return max(floats)
    
    
def MyFunc(lst):
    even_nums = [x for x in lst if type(x)==int and x%2 == 0]
    mean = __list_mean(even_nums) if len(even_nums) > 0 else 0
    
    floats = [x for x in lst if type(x)==float]
    max_float = __float_max(floats) if len(floats) > 0 else 0
    
    return mean, max_float

