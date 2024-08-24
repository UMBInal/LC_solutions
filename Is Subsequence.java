class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0, j = 0;

        // Iterate over t and check characters in order
        while (i < s.length() && j < t.length()) {
            if (s.charAt(i) == t.charAt(j)) {
                i++;
            }
            j++;
        }

        // If we've matched all characters of s, return true
        return i == s.length();
    }
}
