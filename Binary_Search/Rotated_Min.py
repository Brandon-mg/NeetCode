def findMin(nums):
    if nums[0]<nums[-1]:
        return nums[0]
    l=0
    r=len(nums)-1
    min_num = nums[-1]
    while l  <=  r :
        mid = (l+r) // 2
        min_num = min(min_num,nums[mid])
        
        # right has the min 
        if nums[mid] > nums[r]:
            l = mid + 1
            
        # left has the  min 
        else:
            r = mid - 1
    return min_num
            

if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    print("nums = [4,5,6,7,0,1,2]")
    print(findMin(nums))
