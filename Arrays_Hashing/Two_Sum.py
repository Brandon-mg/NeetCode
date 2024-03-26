def twoSumBrute(nums, target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j] == target:
                return [i,j]
    return []

def twoSumCompMap(nums, target):
    numMap = {}
    for i, n in enumerate(nums):
        comp = target - n
        if comp in numMap:
            return [numMap[comp], i]
        numMap[n] = i
    return []


if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print('nums = [2,7,11,15], target = 9')
    print(twoSumBrute(nums,target))
    print(twoSumCompMap(nums,target))
    nums = [3,2,4]
    target = 6
    print("nums = [3,2,4], target = 6")
    print(twoSumBrute(nums,target))
    print(twoSumCompMap(nums,target))