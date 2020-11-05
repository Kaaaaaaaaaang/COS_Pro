class Solution {
    public int[] func_a(int[] arr, int n){
        int[] ret = new int[arr.length-1];
        int idx = 0;
        for(int i = 0; i < arr.length; ++i)
            if(arr[i] != n)
                ret[idx++] = arr[i];
        return ret;
    }
    public int func_b(int a, int b){
        if (a >= b)
            return a - b;
        else
            return b - a;
    }
    public int func_c(int[] arr){
        int ret = -1;
        for (int i = 0; i < arr.length; ++i){
            if(ret < arr[i] )
                ret = arr[i];
        }
        return ret;
    }

    public int solution(int[] visitor) {
        int max_first = func_c(visitor);
        int[] visitor_removed = func_a(visitor, max_first);
        int max_second = func_c(visitor_removed);
        int answer = func_b(max_first, max_second);
        return answer;
    }
}
