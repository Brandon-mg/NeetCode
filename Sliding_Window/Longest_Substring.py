def longestSub(s):
    chars=set()
    l = 0
    r = 0
    longest = 1
    for r in range(len(s)):
        if s[r] not in chars:
            chars.add(s[r])
            longest = max(longest, r-l+1)
        else:
            while s[r] in chars:
                chars.remove(s[l])
                l+=1
            chars.add(s[r])
    return longest