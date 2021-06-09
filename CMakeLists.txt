cmake_minimum_required(VERSION 3.9)

if (POLICY CMP0042)
    cmake_policy(SET CMP0042 NEW) # CMake 3.0
endif ()

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_GENERATOR "Unix Makefiles" CACHE INTERNAL "" FORCE)

set(PROJECT_NAME CodingInterview)
project(${PROJECT_NAME})

message(STATUS "Generator: \t\t"    ${CMAKE_GENERATOR})
message(STATUS "Language version: \tC++ "  ${CMAKE_CXX_STANDARD})
message(STATUS "CMake version: \t"  ${CMAKE_VERSION})

set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_SUPPRESS_REGENERATION true) #disables ZERO_MAKE
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall -Werror -march=native")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -march=native")
set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR} ${CMAKE_MODULE_PATH})
set(CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR} ${CMAKE_PREFIX_PATH})
set(PROJECT_DIR     ${CMAKE_CURRENT_LIST_DIR})

set(LIB_POSTFIX ${CMAKE_DEBUG_POSTFIX})
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0 -fPIC  -D_GNU_SOURCE")
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -g -O0  -D_GNU_SOURCE")


# Get header files
file(GLOB_RECURSE HEADERS
        "${PROJECT_DIR}/LeetCode/*.h"
        "${PROJECT_DIR}/CrackingTheCode/*.h"
        "${PROJECT_DIR}/HackerRank/*.h"
        "${PROJECT_DIR}/Others/*.h"
        "${PROJECT_DIR}/Utils/*.h"
        )

# Get source files
file(GLOB_RECURSE SOURCES
        "${PROJECT_DIR}/HackerRank/*.cpp"
        "${PROJECT_DIR}/CrackingTheCode/*.cpp"
        "${PROJECT_DIR}/LeetCode/*.cpp"
        "${PROJECT_DIR}/Others/*.cpp"
        "${PROJECT_DIR}/Utils/*.cpp"
        )



## Get main source files
file(GLOB MAIN_SOURCES
        "${PROJECT_DIR}/main.cpp"
        )


# Set linked files
link_directories(
        /usr/local/lib
        /usr/lib
        /usr/lib/x86_64-linux-gnu
)


source_group("include" FILES
        ${HEADERS}
        )
source_group("src" FILES
        ${SOURCES}
        )
add_executable(${PROJECT_NAME}
        ${HEADERS}
        ${SOURCES}
        ${MAIN_SOURCES}
        )


list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake/Modules")

# Set Link Libraries
target_link_libraries(${PROJECT_NAME})

message(STATUS "C_FLAGS: \t\t"          ${CMAKE_C_FLAGS})
message(STATUS "CXX_FLAGS: \t\t"        ${CMAKE_CXX_FLAGS})