"""
	Implement a basic Dictioanry/Map that supports getting and setting items. You may assume the key is hashtable.
	The __getitem__ and __setitem__ methods should have an average time complexity of O(1). You do not need to worry
	about memory usage.

	Example usage:

	d = Dict()

	(1)
	d["hello"] = "world"
	print(d["hello"]) => prints "world"
"""

class Node:
	value = None
	key = None

	def __init__(self, value, key):
		self.value = value
		self.key = key

class Dict:
	buckets = [None] * 100

	def __init__(self):
		for i in range(0, 100):
			self.buckets[i] = []
		pass

	def __getitem__(self, key):
		bucket_number = hash(key) % 100
		current_bucket = self.buckets[bucket_number]
		for node in current_bucket:
			if key == node.key:
				return node.value
		return None

	def __setitem__(self, key, value):
		bucket_number = hash(key) % 100
		node = Node(value, key)
		self.buckets[bucket_number].append(node)

	def __len__(self):
		return len(self.buckets)

"""
    Given a list of integers `nums` find the length of the longest subarray whose product
    is positive.

    Example:
    
    (1)
    nums = [1, 2, 3, 4, -5]
    max length = 4, because [1, 2, 3, 4] is the longest subarray with a positive product (1 * 2 * 3 * 4 = 24 > 0)

    (2)
    nums = [-1, -4, 0, 3]
    max length = 2, because [-1, -4] has positive product -1 * -4 = 4 > 0

    (3)
    nums = [-2, 3, -4, 8, -6, 2, 0, 1]
    max length = 5, because [3, -4, 8, -6, 2] has positive product (3 * -4 * 8 * -6 * 2 > 0)
    
    (4)
    nums = [1, -1, 2]

"""


def max_positive_product_length(nums):
    max_length = 0
    for i in range(len(nums)):
        current_product = nums[i]
        
        if current_product > 0 and max_length == 0:
            max_length = 1
        
        for j in range(i + 1, len(nums)):
            if current_product * nums[j] == 0:
                break
            current_product *= nums[j]
            if current_product < 0:
                continue
            
            if j - i + 1 > max_length:
                max_length = j - i + 1
            
    return max_length
