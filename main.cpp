//
// Created by SevkiBekir on 5.06.2021.
//
#include <iostream>
#include <LeetCode/BitManipulations/ReverseBits_190.h>
#include <HackerRank/Practices/Cpp/StructPractices.h>
#include <HackerRank/Practices/Cpp/ClassPractices.h>
#include <HackerRank/Practices/Cpp/ClassesObjectsPractices.h>
#include <Others/FindingEfficientBuildingProblem.h>
#include <CrackingTheCode/Chapter5_BitManipulation/Insertion_5_1.h>
#include <HackerRank/Bit_Manipulation_Lonely_Integer.h>

void printSectionSeperator(){
    std::cout << "##############################################" << std::endl;

}
void runHackerRankSection(){
    printSectionSeperator();
    std::cout << "Hacker Rank Section Running!" << std::endl;

    // It is solved, but closed the input reason
//    StructPractices structPractices;
//    structPractices.run();

//    ClassPractices classPractices;
//    classPractices.run();

//    ClassesObjectsPractices classesObjectsPractices;
//    classesObjectsPractices.run();

    Bit_Manipulation_Lonely_Integer bitManipulationLonelyInteger;
    bitManipulationLonelyInteger.run();
}

void runLeetCodeSection(){
    printSectionSeperator();
    std::cout << "Leet Code Section Running!" << std::endl;

    ReverseBits_190 reverseBits190;
    reverseBits190.run();
}

void runCrackingTheCodeSection(){
    printSectionSeperator();
    std::cout << "Cracking the Code Section Running!" << std::endl;

    Insertion_5_1 insertion51;
    insertion51.run();
}

void runOthersSection(){
    printSectionSeperator();
    std::cout << "Others Section Running!" << std::endl;

    FindingEfficientBuildingProblem findingEfficientBuildingProblem;
    findingEfficientBuildingProblem.run();

}
int main(int argc, char* argv[]) {
    std::cout << "Hello Cpp Practices Main!" << std::endl;

    runLeetCodeSection();
    runHackerRankSection();
    runCrackingTheCodeSection();
    runOthersSection();

}