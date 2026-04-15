#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, capacity;
    cout<<"Number of products: ";
    cin>>n;
    cout<<"Capacity: ";
    cin>>capacity;

    int product[n], weight[n], value[n], ratio[n];
    
    for(int i=0; i<n; i++){
        cin>>product[i]>>value[i]>>weight[i];
        ratio[i]=value[i]/weight[i];
    }

    for(int i=0; i<n-1; i++){
        for(int j=0; j<n-i-1; j++){
            if(ratio[j] < ratio[j+1]){
                swap(ratio[j], ratio[j+1]);
                swap(value[j], value[j+1]);
                swap(weight[j], weight[j+1]);
                swap(product[j], product[j+1]);

            }
        }
    }
    int currentW=0, totalValue=0;

    for(int i=0; i<n; i++){
        if(currentW+weight[i]<=capacity){
            currentW+=weight[i];
            totalValue+=value[i];
        }
        else{
            totalValue+=(capacity-currentW)*ratio[i];
            break;
        }
    }
    cout<<"Total value: "<<totalValue;
    return totalValue;
}