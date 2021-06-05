#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

/*
    add code for struct here.
*/

typedef struct Student
{
    int age;
    std::string firstName;
    std::string lastName;
    int standard;
};


int main() {
    Student st;
    
    cin >> st.age >> st.firstName >> st.lastName >> st.standard;
    cout << st.age << " " << st.firstName << " " << st.lastName << " " << st.standard;
    
    return 0;
}