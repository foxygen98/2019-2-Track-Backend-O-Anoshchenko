class LRUCache:
    def __init__(self, capacity=10):
        self.cache = {}
        self.keys = []
        self.capacity = capacity
    
    def get_cache(self, key):
        if key in self.cache:
            return self.cache[key]
        return ''

    def set_cache(self, key, value):
        if key in self.cache:
            self.keys.remove(key)
        elif len(self.keys) == self.capacity:
            del_key = self.keys[0]
            del_cache(del_key)
        self.keys.append(key)
        self.cache[key] = value

    def del_cache(self, key):
        self.keys.remove(key)
        del self.cache[key]

cache = LRUCache(100)
cache.set_cache('Jesse', 'Pinkman')
cache.set_cache('Walter', 'White')
cache.set_cache('Jesse', 'James')
print(cache.get_cache('Jesse'))
cache.del_cache('Walter')
print(cache.get_cache('Walter'))