import LL_Lib

def reverseLL(head):
    prev = None
    
    while head:
        temp=head.next
        head.next=prev
        prev = head
        head = temp
    return prev


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    head = LL_Lib.makeLL(nums)
    print(LL_Lib.readLL(head))
    newHead = reverseLL(head)
    print(LL_Lib.readLL(newHead))
