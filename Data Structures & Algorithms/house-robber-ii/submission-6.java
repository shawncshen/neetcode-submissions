class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0 || nums == null) {
            return 0;
        }

        if (nums.length == 1) {
            return nums[0];
        }

        if(nums.length == 2) {
            return Math.max(nums[0], nums[1]);
        }
        int max1 = helper(Arrays.copyOfRange(nums, 0, nums.length - 1));
        int max2 = helper(Arrays.copyOfRange(nums, 1, nums.length));

        return Math.max(max1, max2);
    }

    private int helper (int[] nums) {
        int rob1 = 0;
        int rob2 = 0;
        for (int n : nums) {
            int newRob = Math.max(rob1 + n, rob2);
            rob1 = rob2;
            rob2 = newRob;
        }
        return rob2;
    }
}