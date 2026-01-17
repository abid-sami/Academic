// Rewrite the previous problem to make the row parameter of the matrix as a default argument.

#include<iostream>
using namespace std;

void matrix(int n, int a[10][10], int m=2){
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cin>>a[i][j];
        }
    }
    cout<<"Your "<<m<<"x"<<n<<" Matrix: "<<endl;
    for(int i=0; i<m; i++){
        for(int j=0; j<n; j++){
            cout<<a[i][j]<<" ";
        }
        cout<<endl;
    }
}

int main(){
    int n;
    cout<<"Enter Matrix size: ";
    cin>>n;
    int a[10][10];
    matrix(n, a);   
}