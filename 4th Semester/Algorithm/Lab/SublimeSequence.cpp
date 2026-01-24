#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    while(t--){
        int a, b;
        cin>>a>>b;
        if(b%a==0){
            cout<<0;
        }
        else{
            cout<<a;
        }
    }
}