#include <iostream>
using namespace std;

int factorial(int n) {
    // Base cases
    if (n < 0) {
        cout << "Factorial is not defined for negative numbers" << endl;
        return -1;  // Error indicator
    }
    else if (n == 0 || n == 1) {
        return 1;
    }
    // Recursive case
    else {
        return n * factorial(n - 1);
    }
}

int main() {
    // Test cases
    cout << "Factorial of 5: " << factorial(5) << endl;    // Should print 120
    cout << "Factorial of 0: " << factorial(0) << endl;    // Should print 1
    cout << "Factorial of 3: " << factorial(3) << endl;    // Should print 6
    cout << "Factorial of -1: ";                          // Should print error message
    factorial(-1);
    
    return 0;
}