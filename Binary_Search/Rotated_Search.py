def findTarget(nums, target):
    l=0
    r=len(nums)-1
    while l<=r:
        mid = r+l//2
        if nums[mid]==target:
            return mid
        if nums[mid]>=nums[l] :
            if nums[mid]<target or nums[l]<target:
                l=mid+1
            else:
                r=mid-1
        else:
            if nums[mid]>target or target>nums[r]:
                r=mid-1
            else:
                l=mid+1
    return -1

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    target = 0
    print("nums = [4,5,6,7,0,1,2], target = 0")
    print(findTarget(nums,target))