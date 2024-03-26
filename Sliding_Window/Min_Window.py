from collections import defaultdict


def minWindow(s,t):
    if len(t)>len(s):
        return ""
    tTable = defaultdict(int)
    for c in range(len(t)):
        tTable[t[c]]+=1
    minLen=-1
    r = 0
    l = 0
    count = len(t)
    while r<len(s):
        if tTable.get(s[r], 0) > 0:
            count-=1
        tTable[s[r]]-=1
        r+=1
        while count == 0:
            if r-l<minLen or minLen==-1:
                lidx=l
                minLen=r-l
            if tTable.get(s[l])==0:
                count+=1
            tTable[s[l]]+=1
            l+=1
    return "" if minLen==-1 else s[lidx:lidx+minLen]
        

if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    print('s = "ADOBECODEBANC", t = "ABC"')
    print(minWindow(s,t))