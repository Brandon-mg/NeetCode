def binSearch(nums, target):
    l=0
    r=len(nums)-1
    while l<=r:
        mid = (r+l)//2
        if nums[mid]==target:
            return mid
        if nums[mid]>target:
            r=mid-1
        else:
            l=mid+1
    return -1


if __name__== '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    print("nums = [-1,0,3,5,9,12], target = 9")
    print(binSearch(nums,target))