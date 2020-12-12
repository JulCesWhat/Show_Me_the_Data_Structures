

class Cache_Item(object):
    def __init__(self, data, pos):
        self.data = data
        self.pos = pos


class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.dic = dict()
        self.lis = list()
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.dic:
            value = self.dic[key]
            del self.lis[value.pos]
            self.lis.append(value)
            value.pos = len(self.lis) - 1
            # print(value.data)
            return value.data
        else:
            # print(-1)
            return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if key in self.dic or self.capacity > len(self.dic):
            # self.dic[key] = Cache_Item(value)
            self.lis.append(key)
            self.dic[key] = Cache_Item(value, len(self.lis) - 1)
        else:
            rem_key = self.lis[0]
            del self.lis[0]
            del self.dic[rem_key]
            self.lis.append(key)
            self.dic[key] = Cache_Item(value, len(self.lis) - 1)


if __name__ == "__main__":
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1);
    our_cache.set(2, 2);
    our_cache.set(3, 3);
    our_cache.set(4, 4);

    value_1 = our_cache.get(1)
    print(value_1)
    # returns 1

    value_2 = our_cache.get(2)
    value_9 = our_cache.get(9)
    print(value_9)
    # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)

    value_3 = our_cache.get(3)
    print(value_3)
    # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
