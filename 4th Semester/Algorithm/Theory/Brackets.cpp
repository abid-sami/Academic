#include<iostream>
using namespace std;

bool isValid(string s){
    int balance=0;
    for(char c:s){
        if(c=='(') balance++;
        else balance--;
        if(balance<0) return false;
    }
    return balance==0;
}

int main(){
    string s;
    cin>>s;
    int n=s.size();

    for(int i=0;i<n;i++){
        for(int j=i+1;j<n;j++){
            if(s[i]=='(' && s[j]==')'){
                string t="";
                for(int k=0;k<n;k++){
                    if(k!=i && k!=j) t+=s[k];
                }
                if(isValid(t)){
                    cout<<"Valid";
                    return 0;
                }
            }
        }
    }
    cout<<"Invalid";
}
