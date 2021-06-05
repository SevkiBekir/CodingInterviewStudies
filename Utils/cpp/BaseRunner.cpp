//
// Created by SevkiBekir on 5.06.2021.
//

#include <iostream>
#include "BaseRunner.h"

void BaseRunner::init() {
    printSeperator();
    printTitle();
    std::cout << "Initializing..." << std::endl;
    problemInit();
}

void BaseRunner::run() {
    init();

    std::cout << "Running..." << std::endl;
    problemRun();
}

void BaseRunner::printTitle() {
    std::cout << "Problem name: " << problemName << std::endl;
}

void BaseRunner::printSeperator() {
    std::cout << "---------------------------------" << std::endl;

}

const std::string &BaseRunner::getProblemName() const {
    return problemName;
}

void BaseRunner::setProblemName(const std::string &problemName) {
    BaseRunner::problemName = problemName;
}
