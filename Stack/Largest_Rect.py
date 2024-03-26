def largestRect(heights):
    ans = 0
    stack = []

    for i,h in enumerate(heights):
        print( stack)
        start=i
        while stack and stack[-1][1]>=h:
            index,hei = stack.pop()
            start = index
            ans = max(ans, (i-index)*hei)
            print((i-index)*hei)
            print(stack)
        stack.append((start,h))

    for i,h in stack:
        ans = max(ans, (len(heights)  - i) *h)

    return ans

if __name__ == '__main__':
    heights = [2,1,5,6,2,3]
    print('heights = [2,1,5,6,2,3]')
    print(largestRect(heights))