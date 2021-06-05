//
// Created by SevkiBekir on 6.06.2021.
//

/**
 * Description: Find a effective building to move from the given buildings wrt the requirements.
 * The question was asked into Google Interview.
 * The given building list can be:
 * Blocks = {
 *          "gym":true
 *          "school":true
 *          "store":false
 *      },
 *      {
 *          "gym":true
 *          "school":false
 *          "store":false
 *      },
 *      {
 *          "gym":false
 *          "school":true
 *          "store":false
 *      },
 *      {
 *          "gym":false
 *          "school":true
 *          "store":true
 *      }
 *
 *  Find the effective building block if the given requirement:
 *  Requirement = ['gym', 'school', 'store']
 *
 *  The output the third item (second index):
 *   {
 *          "gym":false
 *          "school":true
 *          "store":false
 *   },
 *
 *   and the output is '2'
 *
 *   Explanation: It is 2 because the second item is the closest to the given facilities (requirements).
 */
#ifndef CODINGINTERVIEW_FINDINGEFFICIENTBUILDINGPROBLEM_H
#define CODINGINTERVIEW_FINDINGEFFICIENTBUILDINGPROBLEM_H


#include <Utils/cpp/BaseRunner.h>
#include <vector>
#include <map>

using Block = std::map<std::string,bool>;

class FindingEfficientBuildingProblem : public BaseRunner{
public:
    FindingEfficientBuildingProblem();

protected:
    void problemInit() override;
    void problemRun() override;

private:
    std::vector<Block> blocks;
};


#endif //CODINGINTERVIEW_FINDINGEFFICIENTBUILDINGPROBLEM_H
