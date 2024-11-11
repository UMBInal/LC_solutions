class Solution:
    def fib(self, n: int) -> int:

        # Bottom Up DP (eliminates recursion):
        # O(n) space and time

        if n ==0:
            return 0
        if n == 1:
            return 1

# We can memoize the top down approach too,
# since we only need the last 2 entries in the array

        prev = 0
        cur = 1

        for i in range(2, n+1):
            prev, cur = cur, prev+cur

        return cur

        # time: O(n)
        # space: O(1)


'''        dp = [0 for i in range(n+1)]
        
        dp[1] = 1 

        for i in range(2, n+1):
            dp[i]= dp[i-2] + dp[i-1]

        return dp[n]

Tabulation: 

If you have the sequence:
0   1   1   2   3   5   8   ...
0   1   2   3   4   5   6   ...

Thus, you can follow the bottom up - tabulation approach
to find f(n).
Start with an array of 0's and base cases:
      0   1   2   3 ...
dp = [0, 1, 0, 0, 0, 0 ...]

dp[i] = dp[i-2] + dp[i-1]



        # Top Down DP (uses recursion):
        # need a memo, start with base cases:

        memo = {0:0, 1:1}

        def f(x):
            if x in memo:
                return memo[x]
            else:
                memo[x] = f(x-1) + f(x-2)
                return memo[x]

        return f(n)

        # O(n) solution

        # DP:
        # recursive solution:
      
if n == 0:
            return 0

        if n == 1:
            return 1 

        return self.fib(n-2) + self.fib(n-1)


        # DP approach:
        n = 6:
        f(6)
        |   |
    f(5)    f(4)
    |   |       |   |
f(4)    f(3)    f(3)    f(2)

==> these problems repeat:
    Overlapping Subproblems
 
Note the left side set of problems includes 
every problem mentioned elsewhere in the tree 

There are 2^n tree levels => the standard recursive approach will therefore
be O(2^n)

 

    # Alternatively, we could use:
    # Top Down Dynamic Programming == Memoization:

        f(6)
        |  
    f(5)  
    |   
f(4)    


is all we need to compute, once.


# use a dictionary to store the solutions to subproblems:
# memo_dict = {n=0: 0, n=1:1, n=2: 1, n= 3: 2, ...} 

        n = 6:
        f(6)
        |   |
    f(5)    f(4)
    |   |       |   |
f(4)    f(3)    f(3)    f(2)
            ...         |   |
                        f(1) f(0)

memo_dict = {n=0: 0, n=1:1, n=2: 1, n= 3: 2, ...} 

        n = 6:
        f(6)
        |   |
    f(5)    3                ==> thus, we don't need the repetitive function calls
    |   |       |   |
f(4)    f(3)    2    1
            ...         |   |
                        1    0

In conclusion, these are substituted with the actual values
we computed:
        f(6)
        |   |
    f(5)    f(4)
    |   |       |   |
f(4)    f(3)    f(3)    f(2)
            ...         |   |
                        f(1) f(0)

once, here:
        f(6)
        |  
    f(5)  
    |   
f(4)    

This is O(n).
'''
