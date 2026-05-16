#include<bits/stdc++.h>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        if(n==1){
            cout<<1<<endl;
        }
        else if(n==2){
            cout<<9<<endl;
        }
        else{
            int cell=n*n-1;
            int cost=cell+(n*n)+(n*n-2)+(n*n-1-n);
            cout<<cost<<endl;
        }
    }
}