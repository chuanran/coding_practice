class MyHashMap:

    def __init__(self):
        self.MAX_LENGTH = 100000
        self.map = [[] for i in range(self.MAX_LENGTH)]
        
    def get_index(self, key: int) -> int:
        return key % self.MAX_LENGTH
    
    def get_pos(self, index: int, key: int) -> int:
        bucket_list = self.map[index]
        if not bucket_list:
            return -1
        for map_index, key_value_pair in enumerate(bucket_list):
            if key == key_value_pair[0]:
                return map_index
        return -1
        
    
    def put(self, key: int, value: int) -> None:
        index = self.get_index(key)
        bucket_pos = self.get_pos(index, key)
        if bucket_pos == -1:
            self.map[index].append([key, value])
        self.map[index][bucket_pos][1] = value
        
        
    def get(self, key: int) -> int:
        index = self.get_index(key)
        bucket_pos = self.get_pos(index, key)
        if bucket_pos == -1:
            return -1
        return self.map[index][bucket_pos][1]
        

    def remove(self, key: int) -> None:
        index = self.get_index(key)
        bucket_pos = self.get_pos(index, key)
        if bucket_pos == -1:
            return None
        self.map[index].remove(self.map[index][bucket_pos])
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)