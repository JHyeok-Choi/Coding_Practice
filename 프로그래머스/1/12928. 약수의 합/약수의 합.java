class Solution {
    public int solution(int n) {
        int answer = 0;
        for (var i=1;i <= n;i++) {
            if (n % i == 0) {
                answer += i;
            }
        }
        return answer;
    }
}