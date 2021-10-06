# trying to populate index 1
# index of 360 in line 20 array = 2
# index of 1 in line 22 array = 0

# trying to populate index 2
# index of 360 in line 20 array = 3
# index of 1 in line 22 array = 1

# Input: {1, _, 3, 4, 5, 6}
# Output:{720, 360, _, _, _, _}

# Input: {1, 2, _, 4, 5, 6}
# Output:{720, 360, 240, _, _, _}

# Input: {1, 2, 3, _, 5, 6}
# Output: {720, 360, 240, 180]

# Input: {1, 2, 3, 4, _, 6}

# Input: {1, 2, 3, 4, 5, _}

# 2x3x4x5x6 1
# 1x3x4x5x6 2
# 1x2x4x5x6

# Input:  n > 0  All positive integers

# def multiplication(input):
#     result = []

#     list_result = []
#     for i in range(len(input)):
#         result = 0
#         for j in range(len(input)):
#             if i == j:
#                 continue
#             else:
#                 if result == 0:
#                     result = input[j]
#                 else:
#                     result *= input[j]

#         list_result.append(result)
#     return list_result


def multiplication(input):
    result = []

    list_result = []
    forward_list = []
    backward_list = []
    result = 1
    for i in range(len(input)):
        result *= input[i]
        forward_list.append(result)
    result = 1
    for i in range(len(input) - 1,-1,-1):
        result *= input[i]
        backward_list.insert(0, result)
    for i in range(len(input)):
        if i - 1 < 0:
            list_result.append(backward_list[i + 1])
        elif i >= len(input) - 1:
            list_result.append(forward_list[i - 1])
        else:
            list_result.append(forward_list[i - 1] * backward_list[i + 1])
    # print(forward_list)
    # print(backward_list)
    return list_result

if __name__ == '__main__':
    # input = [2, 1, 3, 4]
    input = [1, 2, 3, 4, 5, 6]
    print(multiplication(input))