// To read a matrix of size m*n from the  keyboard and display the same on the screen using the function. 

#include<iostream>
using namespace std;

void matrix(int m, int n, int a[10][10]){
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
    int m,n;
    cout<<"Enter Matrix size: ";
    cin>>m>>n;
    int a[10][10];
    matrix(m,n,a);
}