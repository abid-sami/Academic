#include <iostream>
using namespace std;

void readAndDisplay(int a[10][10], int m, int n)
{
    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cin >> a[i][j];
        }
    }

    for(int i = 0; i < m; i++)
    {
        for(int j = 0; j < n; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}

int main()
{
    int m, n;
    cin >> m >> n;

    int matrix[10][10];

    readAndDisplay(matrix, m, n);

    return 0;
}
