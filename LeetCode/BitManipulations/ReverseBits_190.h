//
// Created by SevkiBekir on 5.06.2021.
//

#ifndef CODINGINTERVIEW_REVERSEBITS_190_H
#define CODINGINTERVIEW_REVERSEBITS_190_H


#include <Utils/cpp/BaseRunner.h>

class ReverseBits_190 : public BaseRunner{
public:
    ReverseBits_190();

protected:
    void problemInit() override;
    void problemRun() override;
private:
    uint32_t reverseBits(uint32_t number);
};


#endif //CODINGINTERVIEW_REVERSEBITS_190_H
