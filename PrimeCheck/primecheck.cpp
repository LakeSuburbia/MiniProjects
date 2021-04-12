#include <iostream>
#include <cmath>
#include <string>

using namespace std;

void primeCheck();

int main()
{
    string go = "Y";
    while (go[0] == 'Y' || go[0] == 'y')
    {
        primeCheck();

        cout << "Do you want to check another prime? (y/n)" << endl;
        cin >> go;

        cout << endl << endl;
    }
}

void primeCheck()
{
    int prime;
    
    cout << endl << "Which number do you want to prime-check?" << endl;
    cin >> prime;   
    
    


    for (int i = 2; i <= sqrt(prime); i++)
    {
        if (prime % i == 0)
        {
            cout << endl << endl  << prime << " is not a prime number!" << endl << endl;
            return;
        }
    }

    cout << endl << endl << prime << " is a prime number!" << endl << endl;
}