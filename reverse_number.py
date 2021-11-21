class Solution:
    def reverse(self, x: int) -> int:    
        result = ''
        number_array = []
        number_string = str(x)
        print(number_string)
        for char in number_string:
            number_array.append(char)
        
        if number_array[0] == '-':
            number_array.pop(0)
            result = '-'
            
        # print(number_array[-1])
        while number_array[-1] == '0':
            if number_array == ['0']:
                break
            number_array.pop(-1)
        for i in range(len(number_array) - 1, -1, -1):
            # print(i)
            result += number_array[i]
            
        result = int(result)
        
        if result > 2147483648 - 1 or result < -2147483648:
            return 0
        
        return result

solution = Solution()
print(solution.reverse(-1000))