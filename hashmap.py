class Node:
	value = None
	key = None

	def __init__(self, value, key):
		self.value = value
		self.key = key

class HashMap:
	def __init__(self, capacity):
		self.capacity = capacity
		self.buckets = [[]] * capacity

	def __getitem__(self, key):
		bucket_number = hash(key) % self.capacity
		current_bucket = self.buckets[bucket_number]
		for node in current_bucket:
			if key == node.key:
				return node.value
		return None

	def __setitem__(self, key, value):
		bucket_number = hash(key) % self.capacity
		node = Node(value, key)
		self.buckets[bucket_number].append(node)

	def __len__(self):
		return len(self.buckets)

if __name__ == '__main__':
    map = HashMap(capacity=100)
    map['hello'] = 'world'
    print(map['hello'])