# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.


class MyHashSet:

    def __init__(self):
        self.MAX_LEN = 100000
        self.set = [[] for i in range(self.MAX_LEN)]

    # return the bucket index for specific key
    def get_index(self, key: int) -> int:
        return key % self.MAX_LEN

    # search the key in the specific bucket
    def get_pos(self, index: int, key: int) -> int:
        bucket_list = self.set[index]
        if bucket_list is None:
            return -1
        for bucket_index in range(len(bucket_list)):
            if bucket_list[bucket_index] == key:
                return bucket_index
        return -1
        
    def add(self, key: int) -> None:
        index = self.get_index(key)
        pos = self.get_pos(index, key)
        if pos == -1:
            if self.set[index] is None:
                self.set[index].append([])
            self.set[index].append(key)
            
    def remove(self, key: int) -> None:
        index = self.get_index(key)
        pos = self.get_pos(index, key)
        if pos != -1:
            self.set[index].remove(self.set[index][pos])
            
    def contains(self, key: int) -> bool:
        index = self.get_index(key)
        pos = self.get_pos(index, key)
        if pos != -1:
            return True
        return False
    
    

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

myHashSet = MyHashSet();
print(myHashSet.add(1));      # set = [1]
print(myHashSet.add(2));      # set = [1, 2]
print(myHashSet.contains(1)); # return True
print(myHashSet.contains(3)); # return False, (not found)
print(myHashSet.add(2));      # set = [1, 2]
print(myHashSet.contains(2)); # return True
print(myHashSet.remove(2));   # set = [1]
print(myHashSet.contains(2)); # return False, (already removed)
