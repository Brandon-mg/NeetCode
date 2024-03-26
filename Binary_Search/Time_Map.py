class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key, value, timestamp):
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append([timestamp,value]) 

    def get(self, key, timestamp):
        timestamps=sorted(self.time_map.get(key,[]))
        l=0
        r=len(timestamps)-1
        while l<=r:
            mid = (r+l)//2
            if timestamps[mid][0]==timestamp:
                return timestamps[mid][1]
            if timestamps[mid][0]>timestamp:
                r=mid-1
            else:
                l=mid+1
        return ""

if __name__ == "__main__":
    timeMap =TimeMap()
    timeMap.set("foo", "bar", 1)
    print(timeMap.get("foo", 1))
    print(timeMap.get("foo", 3))
    timeMap.set("foo", "bar2", 4)
    print(timeMap.get("foo", 4))
    print(timeMap.get("foo", 5))    