#include<iostream>
using namespace std;

int main(){
    int n = 10;
    int arr[10];
    int count[11]={0};
    for(int i=0; i<n; i++){
        cin>>arr[i];
        count[arr[i]]++;
    }
    for(int i=1; i<=10; i++){
        while(count[i]>0){
            cout<<i<<" ";
            count[i]--;
        }
    }
}