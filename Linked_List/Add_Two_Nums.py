import LL_Lib

def addTwo(l1, l2):
    carry=0
    head=LL_Lib.ListNode(0)
    dummy = head
    while l1 and l2:
        res=l1.val+l2.val+carry
        carry=res//10
        res=res%10
        head.next=LL_Lib.ListNode(res)
        head=head.next
        l1=l1.next
        l2=l2.next
    while l1:
        res=l1.val+carry
        carry=res//10
        res=res%10
        head.next=LL_Lib.ListNode(res)
        head=head.next
        l1=l1.next
    while l2:
        res=l2.val+carry
        carry=res//10
        res=res%10
        head.next=LL_Lib.ListNode(res)
        head=head.next
        l2=l2.next
    if carry>0:
        head.next=LL_Lib.ListNode(carry)
    return dummy.next


if __name__ == "__main__":
    nums1 = [9,9,9,9,9,9,9]
    nums2 = [9,9,9,9]
    head1 = LL_Lib.makeLL(nums1)
    head2 = LL_Lib.makeLL(nums2)
    print(LL_Lib.readLL(head1))
    print(LL_Lib.readLL(head2))
    newHead = addTwo(head1,head2)
    print(LL_Lib.readLL(newHead))