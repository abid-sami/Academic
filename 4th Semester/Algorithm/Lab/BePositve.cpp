#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n, zero=0, neg=0;
        cin>>n;
        int a[n];
        for(int i=0; i<n; i++){
            cin>>a[i];
            if(a[i]==-1){
                neg++;
            }
            if(a[i]==0){
                zero++;
            }
        }
    }
    cout<<
}