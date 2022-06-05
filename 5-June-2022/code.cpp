#include <iostream>

using namespace std;

const double EPS = 0.000001;

int main() {
    double a = 0.0248330035844995;
    double b = 0.9751669964155007;
    double result = a + b;

    if (abs(1 - result) < EPS)
        cout << "Equal to 1" << endl;
    else
        cout << "Not equal to 1" << endl;
}

// https://floating-point-gui.de/errors/comparison/

// #include <iostream>

// using namespace std;

// int main() {
//     double a = 0.0248330035844995;
//     double b = 0.9751669964155007;
//     double result = a + b;

//     cout << result << endl;
// }

// #include <iostream>
// #include <iomanip>

// using namespace std;

// int main() {
//     double a = 0.0248330035844995;
//     double b = 0.9751669964155007;
//     double result = a + b;

//     cout << setprecision(50) << result;
// }