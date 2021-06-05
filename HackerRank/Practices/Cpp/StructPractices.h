//
// Created by SevkiBekir on 5.06.2021.
//

#ifndef CODINGINTERVIEW_STRUCTPRACTICES_H
#define CODINGINTERVIEW_STRUCTPRACTICES_H

#include <string>
#include <Utils/cpp/BaseRunner.h>

typedef struct Student
{
    int age;
    std::string firstName;
    std::string lastName;
    int standard;
} Student;

class StructPractices : public BaseRunner {
public:
    StructPractices();

protected:
    void problemInit() override;
    void problemRun() override;

private:

};


#endif //CODINGINTERVIEW_STRUCTPRACTICES_H
