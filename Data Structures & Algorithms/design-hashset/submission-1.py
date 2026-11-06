class MyHashSet:
    
    def __init__(self):
        self.N = 1000001
        self.values = [None] * self.N

    def add(self, key: int) -> None:
        if self.values[key] == None:
            self.values[key] = key

    def remove(self, key: int) -> None:
        if self.values[key] == key:
             self.values[key] = None

    def contains(self, key: int) -> bool:
        return self.values[key] == key


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)