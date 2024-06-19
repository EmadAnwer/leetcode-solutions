
""""

{
    key1: [(value , time), (value , time)],
}

"""




class TimeMap:

    def __init__(self):
        self.keys = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key in self.keys:
            self.keys[key].append((value, timestamp))
        else:
            self.keys[key] = [(value, timestamp)]


    def get(self, key: str, timestamp: int) -> str:
        

        def _bs(t, values):
            l, r = 0, len(values) - 1
            while l <= r:
                m = (l + r) // 2
                if values[m][1] == t:
                    return m
                elif values[m][1] < t:
                    l = m + 1
                else:
                    r = m - 1
            return r

        if key in self.keys:
            values = self.keys[key]
            idx = _bs(timestamp, values)
            return values[idx][0] if idx >= 0 else ""
        else:
            return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)