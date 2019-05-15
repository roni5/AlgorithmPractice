class LRU_Cache(object):

    def __init__(self, capacity = 5):
        self.capacity = capacity
        #To Track Least Recently Used cache, use queue
        self.q = []
        #Dictionary for the cache
        self.cache = {}

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if self.cache.get(key) is not None:
            return self.cache.get(key)
        else:
            return -1


    def set(self, key, value):
        #If reached the full capacity, remove the oldest item
        if len(self.q) >= self.capacity:
            #Retrieve the oldest key
            removed = self.q.pop(0)
            #Remove that key, value pair from the cache
            self.cache.pop(removed)
            #Add the new key to the queue and cache
            self.q.append(key)
        
        self.cache[key] = value
        self.q.append(key)
   

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(5, 5)
print(our_cache.get(1))       # returns 1
our_cache.set(6, 6)


print(our_cache.get(2))       # returns 2
print(our_cache.get(3))       # return 3
print(our_cache.get(4))       # return 4
print(our_cache.get(5))       # return 5
print(our_cache.get(6))       # return 6
print(our_cache.get(1))       # return -1
