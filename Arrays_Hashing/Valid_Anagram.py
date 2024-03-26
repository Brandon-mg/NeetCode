def isAnagramMap(self, s, t):
    if len(s) != len(t):
        return False
    sMap,tMap = {},{}
    for i in s:
        if sMap.get(i):
            sMap[i]+=1
        else:
            sMap[i]=1
    
    for i in t:
        if tMap.get(i):
            tMap[i]+=1
        else:
            tMap[i]=1
    for i in sMap.keys():
        if tMap.get(i):
            if tMap[i] != sMap[i]:
                return False
        else:
            return False
    return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    print('s = "anagram", t = "nagaram"')
    print(isAnagramMap(s,t))