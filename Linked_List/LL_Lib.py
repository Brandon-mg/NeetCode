class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def makeLL(nums):
    head=ListNode(nums[0])
    dummyHead = head
    for i in range(1, len(nums)):
        newNode=ListNode(nums[i])
        head.next=newNode
        head=head.next
    return dummyHead

def readLL(head):
    s = ""
    while head:
        s+=str(head.val)+"->"
        head=head.next
    return s+"None"

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    head = makeLL(nums)
    print(readLL(head))
