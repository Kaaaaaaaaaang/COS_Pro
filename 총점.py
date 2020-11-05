class Solution {
    public int func_a(int[] s) {
        int ret = 0;
        for(int i = 0; i < s.length; ++i)
            if(s[i] > ret)
                ret = s[i];
        return ret;
    }

    public int func_b(int[] s) {
        int ret = 0;
        for(int i = 0; i < s.length; ++i)
            ret += s[i];
        return ret;
    }

    public int func_c(int[] s){
        int ret = 101;
        for(int i = 0; i < s.length; ++i)
            if(s[i] < ret)
                ret = s[i];
        return ret;
    }

    public int solution(int[] scores) {
        int sum = func_b(scores);
        int max_score = func_a(scores);
        int min_score = func_c(scores);
        return sum - max_score - min_score;
    }
}
