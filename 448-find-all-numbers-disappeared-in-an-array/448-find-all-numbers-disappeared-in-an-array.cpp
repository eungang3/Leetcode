class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
        for (int i = 0; i < nums.size(); i++){
            while(nums[i] != i + 1 && nums[nums[i] - 1] != nums[i]){
                swap(nums[nums[i] - 1], nums[i]);
            }
        }
        
        vector<int> returnArr;
        for (int i = 1; i <= nums.size(); i++){
            if (nums[i - 1] != i){
                returnArr.push_back(i);
            }
        }
        return returnArr;
    }
};