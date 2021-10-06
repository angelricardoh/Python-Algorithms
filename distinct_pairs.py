# def distinct_pairs(input, k):
#     result = 0
#     for i in range(len(input)):
#         for j in range(i + 1, len(input)):
#             if abs(input[i] - input[j]) == k:
#                 result += 1

#     return result

def binarySearch(arr, low, high, x):
 
    if (high >= low):
     
        mid = low + (high - low)//2
        if x == arr[mid]:
            return (mid)
        elif(x > arr[mid]):
            return binarySearch(arr, (mid + 1), high, x)
        else:
            return binarySearch(arr, low, (mid -1), x)
     
    return -1

# def distinct_pairs(input, k):

#     result = 0
#     input.sort()
    
#     for i in range(0, len(input) - 1):
#         if binarySearch(input, i + 1, len(input) - 1, input[i] + k) != -1:
#             result += 1
        
#     return result

def distinct_pairs(input, k):

    MAX = 100000
    result = 0
    hashmap = [False] * MAX
    for element in input:
        hashmap[element] = True

    for i in range(len(input)):

        x = input[i]
        if x - k >= 0 and  hashmap[x - k]:
            result += 1
        if x + k < MAX and hashmap[x + k]:
            result += 1

        hashmap[x] = False

    return result



if __name__ == '__main__':
    input = [1, 5, 4, 1, 2]
    k = 0
    result = distinct_pairs(input, k)
    print(result)

    input = [1, 5, 3]
    k = 2
    result = distinct_pairs(input, k)
    print(result)

    input = [1, 5, 3, 4, 2]
    k = 3
    result = distinct_pairs(input, k)
    print(result)

    input = [8, 12, 16, 4, 0, 20]
    k = 4
    result = distinct_pairs(input, k)
    print(result)
