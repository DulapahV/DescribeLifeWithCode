#include <iostream>
#include <iomanip>

using namespace std;

const double EPS = 0.000001;

int main() {
    double a = 0.0248330035844995;
    double b = 0.9751669964155007;
    double result = a + b;

    cout << result << endl;
    cout << setprecision(50) << result << endl; 

    // Wrong way
    if (result == 1)
        cout << "Equal to 1" << endl;
    else
        cout << "Not equal to 1" << endl;

    // Correct way
    if (abs(1 - result) < EPS)
        cout << "Equal to 1" << endl;
    else
        cout << "Not equal to 1" << endl;
}