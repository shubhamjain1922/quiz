#include<bits/stdc++.h>
using namespace std;

int dec_to_anybase(int num,int base){

	int rem=0;
	int p =1;
	int n =0;

	while(num > 0){

		//cout << "num" << n << endl;
		rem = num%base;
		//cout<<rem<<endl;
		n += rem*p;

		p *= 10;

		num = num/base;

	}

	return n;

}

void inv(int arr[], int n){
	int temp=0;
	int a[n];

	for(int i=0;i<n;i++){
	  
	 //  int x = arr[i];

	 //  temp = arr[x]; 
	 //  arr[x] = i;
	 //  arr[i] = temp;

	 //  for(int i=0;i<n;i++){
	 // 	cout << arr[i] << " ";
	 // }
	 // 	cout << endl;
		int x = arr[i];
		a[x]=i;

	}

	for(int i=0;i<n;i++){
		cout << a[i] << " ";
	}

}


int main(){

	//cout << dec_to_anybase(634,8);
	int arr[] = {3,4,1,0,2,5};
	inv(arr,6);

	

}