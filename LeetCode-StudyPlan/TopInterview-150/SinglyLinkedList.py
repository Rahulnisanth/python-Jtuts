# DETECT THE CYCLE OF THE LINKED LIST :
def hasCycle(self, head: Optional[ListNode]) -> bool:
    # Drive function...
    def detectCycle(prev, curr):
        if curr == None or curr.next == None:
            return False
        if prev == curr:
            return True
        return detectCycle(prev.next, curr.next.next)
    
    if head == None or head.next == None:
        return False
    
    return detectCycle(head, head.next)


# FIND THE MIDDLE ELEMENT OF THE GIVEN LINKED LIST :
def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    curr, count = head, 0
    while curr != None:
        count += 1
        curr = curr.next
    curr = head
    for i in range(count//2):
        curr = curr.next
    return curr


# ADDITION OF TWO LINKED-LISTS :
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    result = dummy
    total = carry = 0

    while l1 or l2 or carry:
        total = carry
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        
        num = total % 10
        carry = total // 10
        dummy.next = ListNode(num)
        dummy = dummy.next
    
    return result.next


# MERGING OF TWO SORTED LISTS :
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode()
    curr = dummy
    while list1 and list2:
        if list1.val < list2.val:
            curr.next = list1
            list1 = list1.next
        else:
            curr.next = list2
            list2 = list2.next
        curr = curr.next
    curr.next = list1 or list2
    return dummy.next


# REVERSE THE LINKED LIST WITHIN GIVEN BOUNDARY :
def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)

    leftPrev, curr = dummy, head
    for i in range(left - 1):
        leftPrev, curr = curr, curr.next
    
    prev = None
    for i in range(right - left + 1):
        tempNext = curr.next
        curr.next = prev
        prev, curr = curr, tempNext
    
    leftPrev.next.next = curr
    leftPrev.next = prev

    return dummy.next


# DELETE THE NTH NODE FROM THE END OF THE LIST :
def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0)
    dummy.next = head
    first, second = dummy, dummy

    for i in range(n + 1):
        first=  first.next
    
    while first is not None:
        first = first.next
        second = second.next
    
    second.next = second.next.next
    return dummy.next