//
// Created by SevkiBekir on 5.06.2021.
//

#include "StructPractices.h"

StructPractices::StructPractices() {
    setProblemName("StructPractices");
}

void StructPractices::problemInit() {

}

void StructPractices::problemRun() {
    Student st;

    std::cin >> st.age >> st.firstName >> st.lastName >> st.standard;
    std::cout << st.age << " " << st.firstName << " " << st.lastName << " " << st.standard << std::endl;
}
