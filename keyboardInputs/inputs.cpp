#include <stdio.h>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string message;
    cout << "Enter your message :" << endl;
    getline(cin, message); // accepts multiple line inputs. I just dont know how to take multi line inputs.
    cout << "Message recieved is :" << message << endl;
    return 0;
}