//
// Created by SevkiBekir on 6.06.2021.
//

#include <set>
#include "FindingEfficientBuildingProblem.h"

FindingEfficientBuildingProblem::FindingEfficientBuildingProblem() {
    setProblemName("FindingEfficientBuildingProblem");
}

void FindingEfficientBuildingProblem::problemInit() {
    Block block = {
            {"gym",    true},
            {"school", true},
            {"store",  false}
    };

    blocks.emplace_back(block);

    block = {
            {"gym",    true},
            {"school", false},
            {"store",  false}
    };

    blocks.emplace_back(block);

    block = {
            {"gym",    false},
            {"school", true},
            {"store",  false}
    };

    blocks.emplace_back(block);

    block = {
            {"gym",    false},
            {"school", true},
            {"store", true}
    };

    blocks.emplace_back(block);

}

void FindingEfficientBuildingProblem::problemRun() {
    std::vector<std::string> requirements = {"gym", "school", "store"};

    std::map<std::string, std::set<int>> facilityWrtBlockNo;
    int counter = 0;
    for(const auto& block: blocks){
        for (const auto& pair: block){
            if(pair.second){
                // find the facility type
                auto isFoundFacilityInSet = facilityWrtBlockNo.find(pair.first);
                if(isFoundFacilityInSet != facilityWrtBlockNo.end()){
                    // found, add it
                    facilityWrtBlockNo[pair.first].insert(counter);

                    continue;
                }

                //not found, add first facility then add the building no
                facilityWrtBlockNo.insert({pair.first,{counter}});

            }
        }

        counter++;
    }

    int theClosestBuildingTotalCost = INT32_MAX;

    std::map<int, int> theClosestBuildingInfo;

    int blockSize = blocks.size();
    for (int i = 0; i < blockSize; ++i){
        int totalCost = 0;
        for(const auto& requirement: requirements){
            int metric = INT32_MAX;
            //check exist or not in the set
            auto isFound = facilityWrtBlockNo[requirement].find(i);
            if(isFound != facilityWrtBlockNo[requirement].end()){
                continue;
            }

            // not exist
            // start the closest distance for the facility
            for(const auto& nearBuildingNo: facilityWrtBlockNo[requirement]){
                int distance = std::abs((nearBuildingNo-i));
                if(metric > distance){
                    metric = distance;
                    continue;
                }

                break;
            }

            totalCost += metric;

        }

        theClosestBuildingInfo.insert({totalCost,i});

        if(theClosestBuildingTotalCost > totalCost){
            theClosestBuildingTotalCost = totalCost;
        }
    }

    std::cout << "The result is building no:"  << theClosestBuildingInfo.begin()->second <<
                " The cost:" << theClosestBuildingInfo.begin()->first << std::endl;


}
