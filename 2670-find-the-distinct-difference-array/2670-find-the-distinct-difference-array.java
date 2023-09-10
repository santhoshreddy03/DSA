class Solution {
    public int[] distinctDifferenceArray(int[] nums) {
        int[] ans = new int[nums.length];
        for(int i=0;i<nums.length;i++){
            int left=find_unique_bef(nums,i);
            int right=find_unique_aft(nums,i);
            ans[i]=left-right;
        }
        return ans;
    }
    public int find_unique_bef(int[] arr,int k){
        int n=arr.length;
        Set<Integer> s = new HashSet<>();
        for(int i=0;i<=k;i++){
            s.add(arr[i]);
        }
        return s.size();
    }
    public int find_unique_aft(int[] arr,int k){
        int n=arr.length;
        Set<Integer> s = new HashSet<>();
        for(int i=k+1;i<n;i++){
            s.add(arr[i]);
        }
        return s.size();
    }
}