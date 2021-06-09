//
// Created by SevkiBekir on 8.06.2021.
//

#include <map>
#include "Bit_Manipulation_Lonely_Integer.h"

Bit_Manipulation_Lonely_Integer::Bit_Manipulation_Lonely_Integer() {
    setProblemName("Bit_Manipulation_Lonely_Integer");
}

void Bit_Manipulation_Lonely_Integer::problemInit() {
    input = {0,0,2,1,2,5,95,95,1};
}

void Bit_Manipulation_Lonely_Integer::problemRun() {
    bitMapSolution();
    hashMapSolution();
}

void Bit_Manipulation_Lonely_Integer::bitMapSolution() {
    int result = 0;
    for(auto item: input){
        result = result ^ item;
    }

    std::cout << "result: " << result << std::endl;

}

void Bit_Manipulation_Lonely_Integer::hashMapSolution(){
    std::map<int, int> map;
    for(auto item : input){
        if(map.find(item) != map.end()){
            // exist
            map[item]++;
            continue;
        }

        map.insert({item,1});
    }

    int uniqueNumber = -1;
    for(const auto& pair: map){
        if(pair.second == 1){
            uniqueNumber = pair.first;
        }
    }

    std::cout << "result: " << uniqueNumber << std::endl;
}
