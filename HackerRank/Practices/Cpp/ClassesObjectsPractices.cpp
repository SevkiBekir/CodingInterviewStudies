//
// Created by SevkiBekir on 5.06.2021.
//

#include "ClassesObjectsPractices.h"
#include "Student.h"

ClassesObjectsPractices::ClassesObjectsPractices() {
    setProblemName("ClassesObjectPractices");
}

void ClassesObjectsPractices::problemInit() {

}

void ClassesObjectsPractices::problemRun() {
    int n; // number of students
    std::cin >> n;
    Student *s = new Student[n]; // an array of n students

    for(int i = 0; i < n; i++){
        s[i].input();
    }

    // calculate kristen's score
    int kristen_score = s[0].calculateTotalScore();

    // determine how many students scored higher than kristen
    int count = 0;
    for(int i = 1; i < n; i++){
        int total = s[i].calculateTotalScore();
        if(total > kristen_score){
            count++;
        }
    }

    // print result
    std::cout << count << std::endl;
}
