def containsDuplicateBrute(nums):
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j]:
                return True
    return False

def containsDuplicateSort(nums):
    nums=sorted(nums)
    for i in range(len(nums)-1):
        if nums[i]==nums[i+1]:
            return True
    return False

def containsDuplicateSet(nums):
    num_set = set()
    for i in nums:
        if i in num_set:
            return True
        else:
            num_set.add(i)
    return False

if __name__ == '__main__':
    x=[1,2,3,1]
    print(x)
    print(containsDuplicateBrute(x))
    print(containsDuplicateSort(x))
    print(containsDuplicateSet(x))
    x=[1,2,3,4]
    print(x)
    print(containsDuplicateBrute(x))
    print(containsDuplicateSort(x))
    print(containsDuplicateSet(x))