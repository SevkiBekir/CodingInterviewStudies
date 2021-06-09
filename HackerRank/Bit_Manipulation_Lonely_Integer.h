//
// Created by SevkiBekir on 8.06.2021.
//

#ifndef CODINGINTERVIEW_BIT_MANIPULATION_LONELY_INTEGER_H
#define CODINGINTERVIEW_BIT_MANIPULATION_LONELY_INTEGER_H


#include <Utils/cpp/BaseRunner.h>
#include <vector>

class Bit_Manipulation_Lonely_Integer : public BaseRunner {
public:
    Bit_Manipulation_Lonely_Integer();

protected:
    void problemInit() override;
    void problemRun() override;

private:
    std::vector<int> input;

    void hashMapSolution();
    void bitMapSolution();
};


#endif //CODINGINTERVIEW_BIT_MANIPULATION_LONELY_INTEGER_H
