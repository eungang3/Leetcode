class Solution {
public:
    int thirdMax(vector<int>& nums) {
       set<int> top3;
    for (int i = 0; i < nums.size(); i++){
        top3.insert(nums[i]);
        if (top3.size() > 3){
            top3.erase(top3.begin());
        }
    }
    return top3.size() == 3 ? *top3.begin() : *top3.rbegin();
    }
};