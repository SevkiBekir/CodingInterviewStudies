//
// Created by SevkiBekir on 5.06.2021.
//

#include "ClassPractices.h"
#include "Student.h"

ClassPractices::ClassPractices() {
    setProblemName("Class Practices");
}

void ClassPractices::problemInit() {

}

void ClassPractices::problemRun() {
    int age, standard;
    std::string first_name, last_name;

    std::cin >> age >> first_name >> last_name >> standard;

    Student student;
    student.set_age(age);
    student.set_standard(standard);
    student.set_first_name(first_name);
    student.set_last_name(last_name);

    std::cout << student.get_age() << "\n";
    std::cout << student.get_last_name() << ", " << student.get_first_name() << "\n";
    std::cout << student.get_standard() << "\n";
    std::cout << "\n";
    std::cout << student.to_string() << "\n";

}
