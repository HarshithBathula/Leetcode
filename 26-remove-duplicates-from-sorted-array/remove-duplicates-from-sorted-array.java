class Solution {
    public int removeDuplicates(int[] nums) {
        boolean unique = true;
        int position = 0;
        for(int i = 1; i<nums.length; i++){
            if(nums[i]>nums[i-1]){
                unique = true;
            }
            if(nums[i]==nums[i-1]){
                unique = false;
            }
            if(unique){
                nums[position+1]=nums[i];
                position++;
            }
        }
        return position+1;
    }
}