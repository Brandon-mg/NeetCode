from collections import defaultdict


def checkInclusion(s1, s2):
    if len(s1)>len(s2):
        return False
    s1Table = defaultdict(int)
    s2Table = defaultdict(int)

    for i in range(len(s1)):
        s1Table[s1[i]]+=1
        if i<len(s1)-1:
            s2Table[s2[i]]+=1
    l=0
    for j in range(len(s1)-1,len(s2)):
        s2Table[s2[j]]+=1
        f=True
        for k,v in s2Table.items():
            if v>0:
                if s1Table.get(k,0) != v:
                    flag=False

            else:
                if s1Table[k]>0:
                    flag=False
            if flag:
                return True
        s2Table[s2[l]]-=1
        l+=1
    return False


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print('s1 = "ab", s2 = "eidbaooo"')
    print(checkInclusion(s1,s2))