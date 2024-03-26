def encode(strs):
    ret=""
    for i in strs:
        ret+=str(len(i))+":"+i
    return ret

def decode(s):
    ret=[]
    while len(s)>0:
        limiter = s.find(":")
        part = int(s[:limiter])
        print(part)
        word = s[limiter+1:part+limiter+1]
        print(word)
        ret.append(word)
        print(s[part+limiter+1:])
        s = s[part+limiter+1:]
    return ret

if __name__ == '__main__':
    s = ["we","say",":","yes"]
    print('["we","say",":","yes"]')
    encoded = encode(s)
    print(encoded)
    print(decode(encoded))