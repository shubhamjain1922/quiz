#include<bits/stdc++.h>
using namespace std;
int main()
{
  vector<int>v = {1,2,3,4,5};
  int target = 3;
  sort(v.begin(),v.end());
  int i = 0, j=v.size()-1;
  while(i<j)
  {
    if(v[i]+v[j]==target)
    {
      break;
    }
    else if(v[i]+v[j]>target)
    {
      j--;
    }
    else
    {
      i++;
    }
  }
  cout<<target<<endl;
}
