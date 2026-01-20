#include <iostream>
#include <string>
using namespace std;

int main() {
    string s;
    cin >> s;
    
    int count = 0;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '<') {
            count++;
        }
    }
    
    int L = count;
    int R = count+ 2;

    cout << "Output: " << (count + 1);

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == '<') {
            cout << " " << L;
            L--;
        } else {
            cout << " " << R;
            R++;
        }
    }
    cout << endl;
    
    return 0;
}