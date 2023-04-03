#Excericise 1
def countdown(num):
    result = []
    for i in range(num, -1, -1):
        result.append(i)
    return result
print(countdown(5))

#Excercise 2
def print_and_return(lst):
    print(lst[0])
    return lst[1]
print(print_and_return([1,2]))


#Excercise 3
def first_plus_length(lst):
    return lst[0] + len(lst)
print(first_plus_length([1,2,3,4,5]))

#Excercise 4
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    else:
        second_value = lst[1]
        new_lst = []
        for num in lst:
            if num > second_value:
                new_lst.append(num)
        print(len(new_lst))
        return new_lst
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#Excercise 5
def length_and_value(size, value):
    return [value] * size
print(length_and_value(4,7))
print(length_and_value(6,2))