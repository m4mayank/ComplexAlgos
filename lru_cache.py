#!/home/cloud_user/.local/share/virtualenvs/algo-9u7x6JDZ/bin/python3

# Design and implement a data structure for LRU (Least Recently Used) cache. It should support the following operations: get and set.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# set(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting the new item.
# The LRU Cache will be initialized with an integer corresponding to its capacity. Capacity indicates the maximum number of unique keys it can hold at a time.

# Definition of “least recently used” : An access to an item is defined as a get or a set operation of the item. “Least recently used” item is the one with the oldest access time.

# Example :
# Input : 
#          capacity = 2
#          set(1, 10)
#          set(5, 12)
#          get(5)        returns 12
#          get(1)        returns 10
#          get(10)       returns -1
#          set(6, 14)    this pushes out key = 5 as LRU is full. 
#          get(5)        returns -1 

class LRUCache:

    # @param capacity, an integer
    def __init__(self, capacity):
        self.llist = []
        self.cap = capacity
        self.dict = {}

    # @return an integer
    def get(self, key):
        if key in self.dict:
            val = self.dict[key]
            del self.dict[key]
            self.dict[key] = val
            return val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dict:
            del self.dict[key]
            self.dict[key] = value
        else:
            if len(self.dict) == self.cap:
                val = list(self.dict)[0]
                del self.dict[val]
                self.dict[key] = value
            else:
                self.dict[key] = value

lru = LRUCache(4)
lru.set(5, 13)
lru.set(9, 6)
lru.set(4, 1)
print(lru.get(4))
lru.set(6, 1)
lru.set(8, 11)
print(lru.get(13))
print(lru.get(1))
lru.set(12, 12)
print(lru.get(10))
lru.set(15, 13)
lru.set(2, 13)
lru.set(7, 5)
lru.set(10, 3)
print(lru.get(6))
print(lru.get(10))
lru.set(15, 14)
lru.set(5, 12)
print(lru.get(5))
print(lru.get(7))
print(lru.get(15))
print(lru.get(5))
print(lru.get(6))
print(lru.get(10))
lru.set(7, 13)
print(lru.get(14))
lru.set(8, 9)
print(lru.get(4))
lru.set(6, 11)
print(lru.get(9))
lru.set(6, 12)
print(lru.get(3))