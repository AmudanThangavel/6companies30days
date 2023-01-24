# Definition for singly-linked list.
from collections import defaultdict as dd


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeZeroSumSublists(self, head):
        end = True
        arr = []
        while end:
            if head.next is None:
                end = False

            arr.append(head.val)
            head = head.next

        l = len(arr)
        ans = []
        i = 0
        while i < l:
            add = arr[i]
            j = i + 1
            include = True
            if add
            while j < l:

                if add + arr[j] == 0:
                    include = False
                    # print("not", i, j)
                    i = j
                    break
                add += arr[j]
                j += 1
            if include:
                ans.append(arr[i])
            i += 1
        print(ans)
        cur = ListNode(t[0])
        result = cur
        for i in range(1, len(arr)):
            cur.next = ListNode(arr[i])
            cur = cur.next

        return result


obj = Solution()
testcases = [[1, 2, -3, 3, 1], [1, 2, 3, -3, 4],
             [1, 2, 3, -3, -2], [2, 0], [1, -1]]
# testcases = [[1, 2, -3, 3, 1]]

for t in testcases:
    head = ListNode(t[0])
    cur = head
    for i in range(1, len(t)):
        head.next = ListNode(t[i])
        head = head.next

    result = obj.removeZeroSumSublists(cur)
    # arr = []
    # end = True
    # while end:
    #     if result.next is None:
    #         end = False
    #     print(result.val)
    #     head = result.next
    # print(result)
