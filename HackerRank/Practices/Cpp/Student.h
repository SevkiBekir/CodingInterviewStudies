#include <iostream>
#include <sstream>
#include <string>

const int NUMBER_OF_EXAMS = 5;


class Student{
private:
    int age;
    std::string firstName;
    std::string lastName;
    int standard;
    int *scores;


public:
    Student(){
        scores = new int[NUMBER_OF_EXAMS];
    };
    ~Student(){
        delete[] scores;
    }
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

    void input(){
        for(int i = 0; i < NUMBER_OF_EXAMS; ++i){
            std::cin >> scores[i];
        }
    };

    int calculateTotalScore(){
        int result = 0;

        for(int i = 0; i < NUMBER_OF_EXAMS; ++i){
            result += scores[i];
        }

        return result;
    }
};