def common_elements():
    list_3 = list(range(0, 100, 3))
    list_5 = list(range(0, 100, 5))
    common =set(list_3) & set(list_5)
    return common
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print('OK')