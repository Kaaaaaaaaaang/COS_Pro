class Solution {
    public int solution(int[] height, int k) {
        int answer = 0;
        int n = height.length;
        for(int i = 0; i < n; ++i)
            if(height[i] > k)
                answer++;
        return answer;
    }
}
