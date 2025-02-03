# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        total = []

        for linked in lists:
            if linked is not None: 
                while linked.next != None:
                    total.append(linked.val)
                    linked = linked.next
                if linked.next == None:
                    total.append(linked.val)
        
        total = sorted(total)
        
        if len(total) > 1:
            for i in range(len(total)):
                if i < len(total) -1 :
                    total[i] = ListNode(total[i], ListNode(total[i+1]))
                else:
                    total[i] = ListNode(total[i], None) 

            final = []

            for i in range(1, len(total)):
                total[-i-1].next = total[-i]
                final.append(total[-i-1])

            result = None
            for i in final:
                result = i
        elif len(total) == 1:
            result = None
            for i in total:
                result = i
            
            result = ListNode(result, None)
        else:
            return None

        return result

        
