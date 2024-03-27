import LL_Lib

def mergeTwoLists(list1, list2):
    if not list2:
        return list1
    if not list1:
        return list2
    head=LL_Lib.ListNode(0)
    dummy=head
    while not( list1 == None or list2 == None):
        if list1.val <= list2.val:
            dummy.next=list1
            list1=list1.next
        else:
            dummy.next = list2
            list2 = list2.next
        dummy = dummy.next
    if list1 == None:
        dummy.next=list2
    if list2 == None:
        dummy.next=list1
    return head.next

if __name__ == "__main__":
    nums1 = [1,2,4]
    nums2 = [1,3,4]
    head1 = LL_Lib.makeLL(nums1)
    head2 = LL_Lib.makeLL(nums2)
    print(LL_Lib.readLL(head1))
    print(LL_Lib.readLL(head2))
    newHead = mergeTwoLists(head1,head2)
    print(LL_Lib.readLL(newHead))