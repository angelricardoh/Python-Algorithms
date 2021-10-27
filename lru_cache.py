class LRUCache:

    def __init__(self, capacity: int):
        self.cache = [None] * capacity
        self.capacity = capacity

    def get(self, key):
        if not key in self.cache:
            return False
        self.cache.remove(key)
        self.cache.insert(0, key)

    def refer(self, key):
        if self.get(key) == False:
            self.put(key)

    def put(self, key):
        if len(self.cache) == self.capacity:
            self.cache.pop()
        self.cache.insert(0, key)

    def display(self):
        for item in self.cache:
            print(item, end=' ')

if __name__ == '__main__':
    cache = LRUCache(4)
    cache.refer(1)
    cache.refer(2)
    cache.refer(3)
    cache.refer(1)
    cache.refer(4)
    cache.refer(5)
    cache.display()