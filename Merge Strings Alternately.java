class Solution {
    public String mergeAlternately(String word1, String word2) {

        // time complexity: O(n + (m-n)) = O(n+m)
//         int minLength = (word1.length() < word2.length()) ? word1.length() : word2.length();
        String s = "";

        if (word1.length() < word2.length()){
            for (int i = 0; i< word1.length(); i++){
                s = s+word1.charAt(i);
                s = s+word2.charAt(i);
            }

            for (int j = word1.length(); j <word2.length(); j++){
                s = s + word2.charAt(j);
            }
        }
        else if (word1.length() > word2.length()){
                for (int i = 0; i< word2.length(); i++){
                s = s+word1.charAt(i);
                s = s+word2.charAt(i);
                }
                for (int j = word2.length(); j <word1.length(); j++){
                s = s + word1.charAt(j);
            }
            }
        else{
            for (int i = 0; i< word2.length(); i++){
                s = s+word1.charAt(i);
                s = s+word2.charAt(i);
        }
        }

        return s;
    }
}