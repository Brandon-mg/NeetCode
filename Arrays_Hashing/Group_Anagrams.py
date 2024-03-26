from collections import defaultdict


def groupAnagramsCharCount(strs):
    hashMap = defaultdict(list)
    for word in strs:
       count = [0] * 26

       for c in word:
           count[ord(c)-ord("a")] += 1

       hashMap[tuple(count)].append(word)
    return hashMap.values()

def groupAnagramsSortMatch(strs):
    hashMap = defaultdict(list)
    for word in strs:
        sorted_str = ''.join(sorted(word))
        hashMap[sorted_str].append(word)
    res = []
    for _,value in hashMap.items():
        res.append(value)
    return hashMap.values()

if __name__ == '__main__':
    strs = ["eat","tea","tan","ate","nat","bat"]
    print('strs = ["eat","tea","tan","ate","nat","bat"]')
    print(groupAnagramsCharCount(strs))
    print(groupAnagramsSortMatch(strs))