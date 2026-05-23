class TimeMap:

    def __init__(self):
        print("pass")
        self.keys = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keys:
            self.keys[key] = []
        self.keys[key].append((value, timestamp))


    def get(self, key: str, timestamp: int) -> str:
        
        if key in self.keys:
            return self.binary_search(0,len(self.keys[key])-1,self.keys[key],timestamp)
        return ""
        
    
    def binary_search(self, l: int, r: int, nums, target: int) -> str:
        if l > r:
            
            value, t = nums[r]
            if t > target:
                return ""
            return value
        m = l + (r - l) // 2
        value, t = nums[m]
        if t == target:
            return value
        if t < target:
            return self.binary_search(m + 1, r, nums, target)
        return self.binary_search(l, m - 1, nums, target)

