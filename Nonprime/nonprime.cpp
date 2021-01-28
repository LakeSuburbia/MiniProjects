#include <iostream>

using namespace std;

int main()
{
    int getal;
    cout << "Geef me een max getal: ";
    cin >> getal;
    cout << endl;

    for (int i = 4; i <= getal; i++)
    {
        bool prime = true;
        //cout << i << endl;

        for (int j = 2; j < i; j++)
        {
            if(i % j == 0)
            {
                prime = false;
            }
        }
        if (prime)
        {
            cout << 3*i << endl;
        }
    }
}