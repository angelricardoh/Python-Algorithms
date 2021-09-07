def binarySearch(number_list, key, low, high):
    if low > high:
        return -1

    middle = int(high - low / 2)

    if number_list[middle] == key:
        return middle
    
    if number_list[middle] > key:
        return binarySearch(number_list, key, low, middle - 1)
    else:
        return binarySearch(number_list, key, middle + 1, high)

number_list = [1, 2, 5, 6, 7, 8, 10]

print(binarySearch(number_list, 7, 0, len(number_list) - 1))