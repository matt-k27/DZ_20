print('DZ20')


def find_unique_value(some_list):
    tempData = {}
    for item in some_list:
        tempData[item] = tempData.get(item, 0) + 1

    for key, value in tempData.items():
        if value == 1:
            return key

# print(find_unique_value([1, 2, 1, 1]))


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

print('Thank you for using')
