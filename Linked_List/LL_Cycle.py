import LL_Lib

def hasCycle(head):
    fast=head.next
    slow=head
    while fast.next:
        if fast==slow:
            return True
        fast=fast.next.next
        slow=slow.next
        if fast==None:
            break
    return False

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    head = LL_Lib.makeLL(nums)
    print(LL_Lib.readLL(head))
    head.next.next.next.next.next=head.next
    print(hasCycle(head))
    nums = [1,2,3,4,5]
    head = LL_Lib.makeLL(nums)
    print(hasCycle(head))
