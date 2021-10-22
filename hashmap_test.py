class Node:
	value = None
	key = None

	def __init__(self, value, key):
		self.value = value
		self.key = key

class HashMap:
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

if __name__ == '__main__':
    map = HashMap()
    map['2'] = 'a'
    map['2'] = 'b'
    map['2'] = 'c'
    print(map['2'])