# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

### EXTRACTING VALUES FROM THE LIST NODES:
        a = []
        b = l1
        while b != None:
            a.append(b.val)
            b = b.next

        x = []
        y = l2
        while y != None:
            x.append(y.val)
            y = y.next

### EXPRESSING THE VALUES AS POWERS OF 10:
        for k in range(0,len(a)):
            a[k] = a[k] * (10**k)

        for m in range(0,len(x)):
            x[m] = x[m] * (10**m)


### REVERSING THE ORDER OF THE VALUES:
        c = []
        d = []

        for i in range(1,len(a)+1):
            c.append(a[-i])
        
        for j in range(1,len(x)+1):
            d.append(x[-j]) 

### SUMMING THEM UP:        
        sum= 0
        for n in range(len(x)):
            sum += x[n]

        for m in range(len(a)):
            sum += a[m]

        sum = str(sum)

### FINAL SUM RESULT:
        final = []

        for r in sum:
            final.append(r)

        z = []

### REVERSING THE ORDER OF THE FINAL SUM IN THE ARRAY Z:
        for i in range(1,len(final)+1):
            z.append(int(final[-i]))


### CREATING THE FINAL LISTNODE OBJECT:
        p = []

        for i in z:
            q = ListNode(val = i)
            p.append(q)

        for i in range(len(p)):
            if i < (len(p) - 1):
                p[i].next = p[i+1]
            else:
                p[i].next = None
        
        return p[0]