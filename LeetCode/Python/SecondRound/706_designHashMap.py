class Bucket:
    def __init__(self):
        self.buckets = []
    
    def put(self, key, value):
        found = False
        for i, kv in enumerate(self.buckets):
            if key == kv[0]:
                self.buckets[i] = (key, value)
                found = True
        if not found:
            self.buckets.append((key, value))
    def get(self, key):
        for (k, v) in self.buckets:
            if key == k:
                return v
        return -1
    def remove(self, key):
        for i, kv in enumerate(self.buckets):
            if key == kv[0]:
                del self.buckets[i]
                break


class MyHashMap(object):
    def __init__(self):
        self.key_space = 2069
        self.hash = [Bucket() for i in range(self.key_space)]
    
    def put(self, key, value):
        hash_key = key % self.key_space
        self.hash[hash_key].put(key, value)
    def remove(self, key):
        hash_key = key % self.key_space
        self.hash[hash_key].remove(key)
    def get(self, key):
        hash_key = key % self.key_space
        return self.hash[hash_key].get(key)