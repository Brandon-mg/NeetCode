def maxWater(heights):
    l=0
    r=len(heights)-1
    maxW=0
    while l<r:
        maxW = max(maxW, min(heights[l],heights[r])*(r-l))
        if heights[l]>heights[r]:
            r-=1
        else:
            l+=1
    return maxW

if __name__ == '__main__':
    height = [1,8,6,2,5,4,8,3,7]
    print("height = [1,8,6,2,5,4,8,3,7]")
    print(maxWater(height))