def trap(height):
    l=0
    r=len(height)-1
    lmax=0
    rmax=0
    res=0

    while l<r:
        if height[l]<height[r]:
            if height[l]<lmax:
                res+=lmax-height[l]
            else:
                lmax=height[l]
            l+=1
        else:
            if height[r]<rmax:
                res+=rmax-height[r]
            else:
                rmax=height[r]
            r-=1
    return res

if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    print("height = [0,1,0,2,1,0,1,3,2,1,2,1]")
    print(trap(height))