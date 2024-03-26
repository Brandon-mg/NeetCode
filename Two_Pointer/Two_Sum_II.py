def twoSum(numbers, target):
    r=len(numbers)-1
    l=0
    while l!=r:
        if (numbers[l]+numbers[r])==target:
            return [l+1,r+1]
        if (numbers[l]+numbers[r])<target:
            l+=1
        if (numbers[l]+numbers[r])>target:
            r-=1

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print('nums = [2,7,11,15], target = 9')
    print(twoSum(nums,target))
    nums = [3,2,4]
    target = 6
    print("nums = [3,2,4], target = 6")
    print(twoSum(nums,target))