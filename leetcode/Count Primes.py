class Solution:
#     def countPrimes(self, n: int) -> int:
#         primes = []
#         count = 0
#         for i in range(2, n):
#             print(n % i)
#             if (n % i) == 0:
#                 continue
#             else:
#                 count += 1
#                 # if division
#                 #     break
#             # primes.append(i)
            
#         return count
    
    def countPrimes(self, n: int) -> int:
        primes = []
        
        if n == 0 or n == 1:
            return 0
        
        for i in range(2, n):
            primes.append(i)
            for j in range(2, i):
                if i % j == 0:
                    primes.remove(i)
                    break

        return len(primes)