//
// Created by SevkiBekir on 5.06.2021.
//

#ifndef CODINGINTERVIEW_BASERUNNER_H
#define CODINGINTERVIEW_BASERUNNER_H


#include <string>
#include <iostream>

class BaseRunner {
public:
    void init();
    void run();

    const std::string &getProblemName() const;
    void setProblemName(const std::string &problemName);

protected:
    virtual void problemInit() = 0;
    virtual void problemRun() = 0;



private:
    void printTitle();
    void printSeperator();

    std::string problemName;

};


#endif //CODINGINTERVIEW_BASERUNNER_H
