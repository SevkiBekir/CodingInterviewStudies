//
// Created by SevkiBekir on 5.06.2021.
//

#include <iostream>
#include "ReverseBits_190.h"

void ReverseBits_190::problemInit() {

}

void ReverseBits_190::problemRun() {
    uint32_t input = 11;
    uint32_t output = reverseBits(input);
    std::cout << output << std::endl;
}
uint32_t ReverseBits_190::reverseBits(uint32_t number) {
    uint8_t size = sizeof(number) * 8;
    uint32_t output = 0;
    for (int i = 0; i < size; ++i) {
        uint8_t bit = number & 1;
        number = number >> 1;
        if(i != 0){
            // except for first bit
            output = output << 1;
        }
        output += bit;

    }

    return output;
}
ReverseBits_190::ReverseBits_190() {
    setProblemName("ReverseBit");
}
