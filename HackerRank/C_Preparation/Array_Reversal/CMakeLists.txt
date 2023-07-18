cmake_minimum_required(VERSION 3.21)
project(${PROJECT_NAME} C)

set(CMAKE_C_STANDARD 99)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
set(CMAKE_SUPPRESS_REGENERATION true) #disables ZERO_MAKE
set(CMAKE_MODULE_PATH ${CMAKE_BINARY_DIR} ${CMAKE_MODULE_PATH})
set(CMAKE_PREFIX_PATH ${CMAKE_BINARY_DIR} ${CMAKE_PREFIX_PATH})

set(PROJECT_DIR     ${CMAKE_CURRENT_LIST_DIR})
set(PARENT_DIR     ${PROJECT_DIR}/..)
set(UTILS_DIR ${PARENT_DIR}/utils)


# Get header files
file(GLOB_RECURSE HEADERS
        "${UTILS_DIR}/*.h"
        )

# Get source files
file(GLOB_RECURSE SOURCES
        "${UTILS_DIR}/*.c"
        )

## Get main source files
file(GLOB MAIN_SOURCES
        "${PROJECT_DIR}/main.c"
        )

source_group("include" FILES
        ${HEADERS}
)

source_group("src" FILES
        ${SOURCES}
)

message("HEADERS: ${HEADERS}")
message("SOURCES: ${SOURCES}")


include_directories(SYSTEM
        ${UTILS_DIR}
        )

add_executable(${PROJECT_NAME}
        ${HEADERS}
        ${SOURCES}
        ${MAIN_SOURCES}
        )


list(APPEND CMAKE_MODULE_PATH "${CMAKE_CURRENT_LIST_DIR}/cmake/Modules")

# Set Link Libraries
target_link_libraries(${PROJECT_NAME})
