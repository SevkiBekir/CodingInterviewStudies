#include <iostream>
#include <sstream>
#include <string>
using namespace std;

class Student{
    private:
        int age;
        std::string firstName;
        std::string lastName;
        int standard;

    public:
        void set_age(const int age){
            this->age = age;
        };

        void set_standard(const int standard){
            this->standard = standard;
        };

        void set_first_name(const std::string first_name){
            this->firstName = first_name;
        };

        void set_last_name(const std::string last_name){
            this->lastName = last_name;
        };

        int get_age() {
            return age;
        };

        int get_standard() {
            return standard;
        };

        const std::string& get_first_name(){
            return firstName;
        };

        const std::string& get_last_name(){
            return lastName;
        };

        std::string to_string(){
            std::string result = std::to_string(age) + "," + firstName + "," + lastName + "," + std::to_string(standard);
            return result;
        };
};

int main() {
    int age, standard;
    string first_name, last_name;
    
    cin >> age >> first_name >> last_name >> standard;
    
    Student st;
    st.set_age(age);
    st.set_standard(standard);
    st.set_first_name(first_name);
    st.set_last_name(last_name);
    
    cout << st.get_age() << "\n";
    cout << st.get_last_name() << ", " << st.get_first_name() << "\n";
    cout << st.get_standard() << "\n";
    cout << "\n";
    cout << st.to_string();
    
    return 0;
}