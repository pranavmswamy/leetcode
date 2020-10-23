#include <iostream>
#include <vector>
#include <bits/stdc++.h>
using namespace std;

// The ides is to start from the end and track the max sofar and the frequencey. We will increment the freq when we encounter the max element again.

void printVec(vector<int>& vec)
{
    for(auto a:vec) cout<<a<<",";
    cout<<endl;
}

vector<int> freqencyOfMaxValue(vector<int>& nums, vector<int>& queries)
{
    vector<int> maxFreqVec(nums.size(),0);
    
    int maxSoFar=INT_MIN;
    int maxFreq=0;
    for(int i=nums.size()-1;i>=0;i--) // Starting from the end
    {
        if(nums[i]>maxSoFar)  // If curr element is greater than the maxSofar, reset the maxSofar and maxFreq
        {
            maxSoFar=nums[i];
            maxFreq=1;
        }
        else if(nums[i]==maxSoFar) // if curr==maxSofar increment our maxFreq
        {
            maxFreq++;
        }
        
        maxFreqVec[i]=maxFreq;
    }
    
    vector<int> ret;
    
    for(auto q:queries) ret.push_back(maxFreqVec[q-1]);
    return ret;
    
}

int main()
{

    vector<int> nums={5,4,5,3,2};
    vector<int> queries={1,2,3,4,5};
    auto res=freqencyOfMaxValue(nums,queries);
    printVec(res);
    
    nums={5,5,5,5,5,5};
    queries={1,2,3,4,5,6};
    res=freqencyOfMaxValue(nums,queries);
    printVec(res);


    return 0;
}
