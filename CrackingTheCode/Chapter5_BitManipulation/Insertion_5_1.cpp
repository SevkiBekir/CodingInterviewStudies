//
// Created by SevkiBekir on 8.06.2021.
//

#include "Insertion_5_1.h"

Insertion_5_1::Insertion_5_1() {
    setProblemName("Insertion 5_1");
}

void Insertion_5_1::problemInit() {
    M = 19;
    N = 1024;
    j = 6;
    i = 2;
}

void Insertion_5_1::problemRun() {
    /**
     * 1000 00000 00
     * head place tail
     *
     * 1000 11001 00
     *
     */
    uint32_t headN = N;
    uint32_t tailN = 0;
    for(int k = 0; k <= j; ++k){
        headN = (headN >> 1);
    }
    uint32_t mask = 0;
    uint8_t bit = 0;
    for(int k = i-1; k >= 0; --k){
        mask = 1 << k;
        bit = (N & mask);
        tailN += bit;
        if(k == 0){
            continue;
        }
        tailN = tailN << 1;
    }


    uint32_t updatedN = headN;
    updatedN = (updatedN << (j-i+1)) | M;
    updatedN = (updatedN << i) | tailN;

    std::cout << "The result is " << updatedN << std::endl;


}
