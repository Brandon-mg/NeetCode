import LL_Lib

def reorder(head):
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    prev = slow.next = None
    while second:
        tmp = second.next
        second.next = prev
        prev = second
        second = tmp
    
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first, second = tmp1, tmp2

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    head = LL_Lib.makeLL(nums)
    print(LL_Lib.readLL(head))
    reorder(head)
    print(LL_Lib.readLL(head))