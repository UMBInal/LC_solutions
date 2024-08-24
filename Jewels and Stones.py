class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        # O(m*n) time, O(1) space solution:
        count = 0
        # for i in stones:
        #     if i in jewels:
        #         count +=1

        # alternatively, using a HASHSET, or just a SET in Python,
        # we don't have to loop through the entire jewels string n times
        # instead, using hashing we have a better solution because hashing and lookup is O(1)
        # FOR SMALLER INPUTS, THIS MAY BE SLOWER, but for large inputs, it will be faster
        # Result:
        # O(m+n) time, O(n) space, where n is the number of elements in string jewels

        for i in stones:
            if i in set(jewels): # O(1) look up instead of O(n)
                count +=1


        return count

### Alternatively:
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # precompute the set, otherwise the complexity increases!!!
        # This will avoid recalculating the set for each element in stones.
        jset = set(jewels) 
        return sum(s in jset for s in stones)