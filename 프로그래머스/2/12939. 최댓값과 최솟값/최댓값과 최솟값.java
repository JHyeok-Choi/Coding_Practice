class Solution {
    public String solution(String s) {
        String arr[] = s.split(" ");
        int min = Integer.parseInt(arr[0]);
        int max = Integer.parseInt(arr[0]);
        
        for (String num:arr) {
            Integer x = Integer.parseInt(num);
            if (min > x) {
                min = x;
            }
            if (max < x) {
                max = x;
            }
        }
        return min + " " + max;
    }
}