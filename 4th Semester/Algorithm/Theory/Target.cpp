#include<iostream>
using namespace std;

int main(){
    int n, target;
    cout<<"Enter Target: "<<endl;
    cin>>target;
    cout<<"Enter array size: "<<endl;
    cin>>n;
    int a[n];
    cout<<"Enter array elements: "<<endl;
    for(int i=0; i<n; i++){
        cin>>a[i];
    }
    for(int i=0; i<n; i++){
        for(int j=i+1; j<n; j++){
            if(a[i]+a[j]==target){
                cout<<"Two Numbers: "<<a[i]<<" "<<a[j]<<endl;
            }
        }
    }
}