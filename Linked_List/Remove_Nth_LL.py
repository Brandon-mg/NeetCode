import LL_Lib

def removeNthFromEnd(head, n):
        dummy = LL_Lib.ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next

if __name__ == "__main__":
    nums = [1,2,3,4,5]
    n=2
    head = LL_Lib.makeLL(nums)
    print(LL_Lib.readLL(head))
    newHead = removeNthFromEnd(head, n)
    print(LL_Lib.readLL(newHead))