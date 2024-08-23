class Solution {
    public int findClosestNumber(int[] nums) {

        // constant space because we are creating a single integer variable 
        // and constant time because we are only looking at the 1st element of the array
        int k = nums[0];

        // linear time because we are iterating through n values in the array
        // constant space because we are modifying the variable in place
        // contant time/space because we are adding and modifying a single variable `a`;
        for (int i = 0; i<nums.length; i++){

            if (k < 0){

                if (nums[i] < 0){
                   int a = -nums[i];
                
                    if (a < -k){
                        k = nums[i];
                    }

                }
                else{
                    if (nums[i] < -k){
                        k = nums[i];
                    }
                }
            }

            else{
                if (nums[i]<0){
                    int a = -nums[i];
                    
                    if (a < k){
                        k = nums[i];
                              }
                }
                else{
                    if (nums[i] < k){
                        k = nums[i];
                    }
                }
            }
        }        


        if (k<0){
            boolean in = false;
        
        // linear time because we are iterating through n values in the array
            for (int j = 0; j<nums.length; j++){
                if (nums[j] == -k){
                    in = true;
                }
            }
            if (in == true){
                k = -k;
            }
        }

    return k;
    }

    /*
    
    Time Complexity: O(2 + 2n) = O(n)
    Space Complexity: O(1)

    */

}
