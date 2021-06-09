//
// Created by SevkiBekir on 8.06.2021.
//

#ifndef CODINGINTERVIEW_INSERTION_5_1_H
#define CODINGINTERVIEW_INSERTION_5_1_H


#include <Utils/cpp/BaseRunner.h>

class Insertion_5_1 : public BaseRunner {
public:
    Insertion_5_1();
protected:
    void problemInit() override;
    void problemRun() override;

private:
    uint32_t M;
    uint32_t N;
    uint8_t j;
    uint8_t i;
};


#endif //CODINGINTERVIEW_INSERTION_5_1_H
